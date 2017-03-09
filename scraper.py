## Justin FlicK 
## Twitter Scraping and Sentiment Analysis  
## Copyright 2017 Licensed under MIT License 
## A GUI program for scraping twitter data without dealing with the API. Use this to get a much larger dataset spanning more dates. 

import easygui as g #library for GUI
import collections
import sys
import webbrowser
import json ## library for manipulating JSON files
from datetime import datetime
from os.path import isfile
from json import dump
import logging
from twitterscraper import query_tweets #library for scraping
from twitterscraper.query import query_all_tweets


##Opens a GUI on start

version = 'Twitter Data Scraper 1.1'

options = ['Start', 'Developer Page', 'Exit']

button = g.buttonbox('Welcome to Twitter Data Scraper Tool' + '\n' + '\n'  + '\n' + '\n' + '\n' + 'Created by Justin Flick, Copyright 2017 Licensed Under MIT License' , title = version, choices = options)

if button == options[0]:
    pass 
if button == options[1]:
    webbrowser.open('https://github.com/Jflick58', new=0, autoraise=True)
if button == options[2]:
    sys.exit()
    
msg = "Enter your query information. Output will be in the form of a .json file"
title = version
fieldNames = ["Search term (do not include the '#' mark, just the the hashtag text","Starting Date (YYYY-MM-DD)","Ending Date (YYYY-MM-DD)","Number of Tweets","Output File Name"]
fieldValues = []  # we start with blanks for the values
fieldValues = g.multenterbox(msg,title, fieldNames)

query = fieldValues[0]
starting_date = fieldValues[1]
ending_date = fieldValues[2]
limit = int(fieldValues[3])
output2 = fieldValues[4]


##Initialize JSON encoder 

class JSONEncoder(json.JSONEncoder):

    def default(self, obj):
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

##Scrape Twitter 
    
tweets = query_tweets(query +'%20since%3A' + starting_date + 'until%3A' + ending_date, limit)

with open(output2 + '.json',"w") as output:
    dump(tweets, output, cls=JSONEncoder)
    print(tweets)
    print("  ")

print('thank you for using this program')
sys.exit()
