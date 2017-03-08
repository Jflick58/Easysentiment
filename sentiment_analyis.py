## Twitter Sentiment Analysis
## Author: Justin Flick
## Licensed under MIT License 




from textblob import TextBlob #library for sentiment anaylsis
import json #library for manipulating JSON files 
import csv #library for reading/writing CSV


#creates a .csv file using a Twitter .json file
#the fields have to be set manually


data_json = open('/users/justin/desktop/tweets.json', mode='r').read() #reads in the JSON file into Python as a string
data_python = json.loads(data_json) #turns the string into a json Python object

csv_out = open('tweets_out_ASCII.csv', mode='w') #opens csv file
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
    csv_out.close()

    


    
