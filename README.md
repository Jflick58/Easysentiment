# Easysentiment Twitter Scraper and Sentiment Analyzer 

GUI Program for scraping Twitter data and performing Naive-Bayes sentiment analysis. 

# Motivation 

As part of my undergraduate thesis, I chose to do a rhetorical analysis of cybersecurity discourse. I later decided to add a quantative portion to my research, and after reading a few articles, I decided to do a sentiment analysis of #russianhacking. The problem was, I needed a program to scrape Twitter for the data, download it in a mutable format, perform a sentiment analysis, and write to a .csv for uploading to a data visualization program. 

After searching the internet and github, I couldn't find anything that fit the bill exactly. Some tools used the official Twitter API, but that only let you search back 7 days and 100 tweets at maximum. Sentiment analysis was also another difficult task, until I came across textblob which used the Naive-Bayes classification method which boasts an 80% accuracy rate when applied to social media sentiment analysis. 

I then decided to make it an all-in-one program with a simple-to-use GUI in order to help future researchers. 

# Requirements 

Python 3.5 or higher

# Installation and Use 

You can install via pip: 

```python
  pip install easysentiment
  ```

or directly from github:

```python
    pip install git+https://github.com/Jflick58/Easysentiment
```

The program is designed to handle the scraping, sentiment analysis, and output all in one step. 
To utilize this, open terminal (on Mac/Linux) or Command Prompt (on Windows) and run `easysentiment` followed by the subcommand you want to run.

I suggest nagivating to the desktop in terminal before running the program. You can do so by typing:

```python
    cd desktop
```

Fill the fields in the GUI. The only fields that are mandatory are search term OR account AND output file name. Your .csv output file will be located in current working directory.

If you need to scrape Twitter for tweets and perform a sentiment analysis, use  the`scrape-and-analyze` subcommand. 

If you just need to scrape Twitter for tweets, use the `scrape` subcommand.

If you already have tweets in a .JSON file, and you just want to perform a sentiment analysis, run the `analyze-sentiment` subcommand.


# Screenshot

![alt tag](https://github.com/Jflick58/Easysentiment/blob/master/res/Easysentiment%201.2.png)

# Acknowledgements 

This program would not have been possible without the use of twitterscraper by Ahmet Taspinar (https://github.com/taspinar/twitterscraper)

Sentiment analysis by Textblob. TextBlob is a Python (2 and 3) library for processing textual data. It provides a consistent API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, and more. https://github.com/sloria/textblob

Special thanks to Github user Rachmadani Haryono (https://github.com/rachmadaniHaryono) for helping me package this for distribution and for writing the command line launcher. 

# Future Plans 

- Complile into standalone executable. 
- Add exclusion terms 
- Add location parameters to search query
