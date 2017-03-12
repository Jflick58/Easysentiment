"""main module."""
# Justin FlicK
# Twitter Scraping and Sentiment Analysis
# Copyright 2017 Licensed under MIT License
# A GUI program for scraping twitter data without dealing with the API.
import sys

from . import cli
if __name__ == "__main__":
    cli(sys.argv[1:])
