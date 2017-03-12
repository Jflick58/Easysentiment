"""scraper and analysis module."""
# Justin FlicK
# Twitter Scraping and Sentiment Analysis
# Copyright 2017 Licensed under MIT License
# A GUI program for scraping twitter data without dealing with the API,
# and then running it through a Naive Bayes sentiment analysis
# to determine a positive or negative response.

from datetime import datetime
from json import dump
# from os.path import isfile  # imported but unused
import collections
import csv  # library for reading/writing CSV
import easygui as g  # library for GUI
import json  # library for manipulating JSON files
# import logging  # imported but unused
import sys
import webbrowser

from textblob import TextBlob  # library for sentiment analysis
from twitterscraper import query_tweets  # library for scraping
# from twitterscraper.query import query_all_tweets  # imported but unused


# Initialize JSON encoder

class JSONEncoder(json.JSONEncoder):
    """custom json encoder."""

    def default(self, obj):
        """default method."""
        if hasattr(obj, '__json__'):
            return obj.__json__()
        elif isinstance(obj, collections.Iterable):
            return list(obj)
        elif isinstance(obj, datetime):
            return obj.isoformat()
        elif hasattr(obj, '__getitem__') and hasattr(obj, 'keys'):
            return dict(obj)
        elif hasattr(obj, '__dict__'):
            return {member: getattr(obj, member)
                    for member in dir(obj)
                    if not member.startswith('_') and
                    not hasattr(getattr(obj, member), '__call__')}

        return json.JSONEncoder.default(self, obj)


def scrape_and_analyze():
    """scrape and analyze."""
    # Opens a GUI on start

    version = 'Easysentiment 1.2'

    options = ['Start', 'Developer Page', 'Exit']

    button = g.buttonbox(
        'Welcome to Easysentiment Twitter Scraper and Seniment Analyzer Version 1.2' +
        '\n' + '\n' + '\n' + '\n' + '\n' +
        'Created by Justin Flick, Copyright 2017 Licensed Under MIT License',
        title=version, choices=options
    )

    if button == options[0]:
        pass
    if button == options[1]:
        webbrowser.open('https://github.com/Jflick58', new=0, autoraise=True)
    if button == options[2]:
        sys.exit()

    msg = "Enter your query information. Output will be in the form of a .csv file"
    title = version
    fieldNames = [  # NOQA
        "Search term (do not include the '#' mark, just the the hashtag text)","From Account",
        "Starting Date (YYYY-MM-DD)", "Ending Date (YYYY-MM-DD)", "Number of Tweets",
        "Output File Name"
    ]
    fieldValues = []  # we start with blanks for the values  # NOQA
    fieldValues = g.multenterbox(msg, title, fieldNames)  # NOQA

    query = fieldValues[0]
    account = fieldValues[1]
    starting_date = fieldValues[2]
    ending_date = fieldValues[3]
    limit = int(fieldValues[4])
    output2 = fieldValues[5]

    # Scrape Twitter

    tweets = query_tweets(query + '%20from%3A' + account +'%20since%3A' + starting_date + 'until%3A' + ending_date, limit)

    with open(output2 + '.json', "w") as output:
        dump(tweets, output, cls=JSONEncoder)
        print(tweets)
        print("  ")

    # converts json to python objects and prepares it to be written to a csv

    # reads in the JSON file into Python as a string
    data_json = open(output2 + '.json', mode='r').read()
    # turns the string into a json Python object
    data_python = json.loads(data_json)

    csv_out = open('Sentiment_Analysis.csv', mode='w')  # opens csv file
    writer = csv.writer(csv_out)  # create the csv writer object

    fields = ['text', 'timestamp', 'polarity', 'subjectivity', 'sentiment']  # field names
    writer.writerow(fields)  # writes field

    for line in data_python:

        # performs the sentiment analysis and classifies it

        print(line.get('text').encode('unicode_escape'))
        analysis = TextBlob(line.get('text'))

        def get_label(analysis, threshold=0):
            if analysis.sentiment[0] > threshold:
                return 'Positive'
            elif analysis.sentiment[0] < threshold:
                return 'Negative'
            else:
                return 'Neutral'
        print(analysis.sentiment, get_label(analysis))  # print the results
        print("  ")

        # writes a row and gets the fields from the json object and the sentiment analysis
        writer.writerow([
            line.get('text').encode('unicode_escape'),  # unicode escape to fix emoji issue
            line.get('timestamp'),
            analysis.sentiment.polarity,
            analysis.sentiment.subjectivity,
            get_label(analysis)
        ])
    else:
        csv_out.close()  # saves the file and closes it
        print('Thank you for using this program')
        sys.exit('goodbye')  # end program
