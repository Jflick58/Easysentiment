# Twitter Scraper and Sentiment Analysis

GUI Program for scraping Twitter for data and performing Naive-Bayes sentiment analysis. 

# Motivation 

As part of my undergraduate thesis at CSU Chico, I chose to do a rhetorical analysis of cybersecurity discourse. I later decided to add a quantative portion to my research, and after reading a few articles, I decided to do a sentiment analysis of #russianhacking. The problem was, I needed a program to scrape Twitter for the data, download it in a mutable format, perform a sentiment analysis, and write to a .csv for uploading to a data visualization program. 

After searching the internet and github, I couldn't find anything that fit the bill exactly. Some tools used the official Twitter API, but that only let you search back 7 days and 100 tweets at maximum. Sentiment analysis was also another difficult task, until I came across textblob which used the Naive-Bayes classification method which boasts an 80% accuracy rate when applied to social media sentiment analysis. 

I then decided to make it an all-in-one program with a simple-to-use GUI in order to help future researchers. 

# Requirements 

Python 3.5 or higher

# Use 

1. Download the repository, and unzip to your desktop. 

2. Run the following from the terminal:

```python
python (path to setup,py) install
```
3. 


