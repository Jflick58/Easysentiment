"""cli module."""
# Twitter Scraping and Sentiment Analysis
# Copyright 2017 Licensed under MIT License
# A GUI program for scraping twitter data without dealing with the API.
import sys
import argparse

from .scraper import scraper
from .scraper_and_analysis import scrape_and_analyze
from .sentiment_analysis import analyze_sentiment


def cli(argv=None):
    """cli entry point."""
    argv = sys.argv[1:] if argv is None else argv
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="subparser_name")
    func_dict = {
        'scrape': scraper,
        'scrape-and-analyze': scrape_and_analyze,
        'analyze-sentiment': analyze_sentiment,
    }
    subparsers.add_parser('scrape')
    subparsers.add_parser('scrape-and-analyze')
    subparsers.add_parser('analyze-sentiment')
    args = parser.parse_args(argv)
    if args.subparser_name in func_dict:
        func_dict[args.subparser_name]()


if __name__ == "__main__":
    cli()
