# Twitter Scraper and Sentiment Analysis

GUI Program for scraping Twitter for data and performing Naive-Bayes sentiment analysis. 

# Motivation 

As part of my undergraduate thesis, I chose to do a rhetorical analysis of cybersecurity discourse. I later decided to add a quantative portion to my research, and after reading a few articles, I decided to do a sentiment analysis of #russianhacking. The problem was, I needed a program to scrape Twitter for the data, download it in a mutable format, perform a sentiment analysis, and write to a .csv for uploading to a data visualization program. 

After searching the internet and github, I couldn't find anything that fit the bill exactly. Some tools used the official Twitter API, but that only let you search back 7 days and 100 tweets at maximum. Sentiment analysis was also another difficult task, until I came across textblob which used the Naive-Bayes classification method which boasts an 80% accuracy rate when applied to social media sentiment analysis. 

I then decided to make it an all-in-one program with a simple-to-use GUI in order to help future researchers. 

# Requirements 

Python 3.5 or higher

# Use 

You can install via pip: 

```python
  pip install easysentiment
  ```
The program is designed to handle the scraping, sentiment analysis, and output all in one step. 
To utilize this, run scraper_and_analysis.py

Follow the fields in the GUI. Your .csv output file will be located in the folder you unzipped in step 1

If you just need to scrape Twitter for tweets, use scraper.py 

If you already have tweets in a .JSON file, and you just want to run a sentiment analysis, use sentiment_analysis.py 

# Acknowledgements 

This program could not be made possible without the use of twitterscraper by Ahmet Taspinar (https://github.com/taspinar/twitterscraper)

Sentiment analysis by Textblob. TextBlob is a Python (2 and 3) library for processing textual data. It provides a consistent API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, and more. https://github.com/sloria/textblob

# Future Plans 

I hope to use a python complier library to compile this into a standalone executable for MacOS, Windows 10, and Linux. 
