## Justin FlicK 
## Twitter Content Analysis 
## Licensed under MIT License 

import sys ## import for exiting
import time ##import for delaying the script
import tweepy ##library to interface with Twitter API
import easygui as g ##import for GUI

##Opens a GUI on start

version = 'Twitter Search 0.1'

options = ['Start', 'Developer Page', 'Exit']

button = g.buttonbox('Welcome to Web View Automator' + '\n' + '\n'  + '\n' + '\n' + '\n' + 'Created by Justin Flick, Copyright 2016' , title = version, choices = options)

if button == options[0]:
pass 
if button == options[1]:
webbrowser.open('https://github.com/Jflick58/Twitter-Conent-Analysis', new=0, autoraise=True
if button == options[2]:
sys.exit()


 ##Opens a GUI box for the user to input their OAuth information

msg = "Enter your authentication information. Please see (insert link) on how to get this information. 
title = version
fieldNames = ["Consumer Key","Consumer Secret","Access Key","Access Secret"]
fieldValues = []  # we start with blanks for the values
fieldValues = g.multenterbox(msg,title, fieldNames)
        
consumer_key = fieldvalues[0]        
consumer_secret = fieldvalues[1]
access_key = fieldvalues [2]
access_secret = fieldvalues [3]
        
