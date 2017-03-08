## Justin FlicK 
## Twitter Content Analysis 
## Licensed under MIT License 

import sys ## import for exiting
import subprocess ##runs the command line tool for scraping tweets 
import easygui as g ##import for GUI

##Opens a GUI on start

version = 'Twitter Data Scraper 0.3'

options = ['Start', 'Developer Page', 'Exit']

button = g.buttonbox('Welcome to Twitter Data Scraper' + '\n' + '\n'  + '\n' + '\n' + '\n' + 'Created by Justin Flick, Copyright 2016' , title = version, choices = options)

if button == options[0]:
    pass 
if button == options[1]:
    webbrowser.open('https://github.com/Jflick58/Twitter-Conent-Analysis', new=0, autoraise=True)
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
limit = fieldValues[3]
output = fieldValues[4]

subprocess.Popen('twitterscraper ' + query + '%20since%3A' + starting_date + "%20until%3A" + ending_date + " --limit " + limit + " --output=/desktop/" + output + ".json")
