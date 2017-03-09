## Justin FlicK 
## Twitter Scraping and Sentiment Analysis  
## Copyright 2017 Licensed under MIT License 
## A GUI program for running twitter data through a Naive Bayes sentiment analysis to determine a positive or negative response. 
##This program assumes you already have your dataset as a JSON file. If not, just use scraper_and_analysis.py to do everything!

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
from textblob import TextBlob #library for sentiment analysis
import csv #library for reading/writing CSV

##Opens a GUI on start

version = 'Twitter Sentiment Analysis Tool 1.1'

options = ['Start', 'Developer Page', 'Exit']

button = g.buttonbox('Welcome to Twitter Sentiment Analysis Tool' + '\n' + '\n'  + '\n' + '\n' + '\n' + 'Created by Justin Flick, Copyright 2017 Licensed Under MIT License' , title = version, choices = options)

if button == options[0]:
    pass 
if button == options[1]:
    webbrowser.open('https://github.com/Jflick58', new=0, autoraise=True)
if button == options[2]:
    sys.exit()
    
msg = "Enter your query information. Output will be in the form of a .json file"
title = version
fieldNames = ["Input file path (use absolute path)", "Output file name"]
fieldValues = []  # we start with blanks for the values
fieldValues = g.multenterbox(msg,title, fieldNames)

input = fieldValues[0]
output = fieldValues[1]

#converts json to python objects and prepares it to be written to a csv

data_json = open(input, mode='r').read() #reads in the JSON file into Python as a string
data_python = json.loads(data_json) #turns the string into a json Python object

csv_out = open(output + '.csv', mode='w') #opens csv file
writer = csv.writer(csv_out) #create the csv writer object

fields = ['text', 'timestamp', 'polarity', 'subjectivity', 'sentiment'] #field names
writer.writerow(fields) #writes field

for line in data_python:

   #performs the sentiment analysis and classifies it
    
    print(line.get('text').encode('unicode_escape'))
    analysis = TextBlob(line.get('text'))
    
    def get_label(analysis, threshold = 0):
        if analysis.sentiment[0]>threshold:
            return 'Positive' 
        elif analysis.sentiment[0]<threshold:
            return 'Negative' 
        else:
            return 'Neutral'
    print(analysis.sentiment,get_label(analysis)) #print the results
    print("  ")

    
    #writes a row and gets the fields from the json object and the sentiment analysis 
    writer.writerow([
                     line.get('text').encode('unicode_escape'), #unicode escape to fix emoji issue
                     line.get('timestamp'),
                     analysis.sentiment.polarity,
                     analysis.sentiment.subjectivity,
                     get_label(analysis)])
else:
	csv_out.close() #saves the file and closes it 
	print('Thank you for using this program')
	sys.exit('goodbye')#end program