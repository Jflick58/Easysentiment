"""setup."""
import os

from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    """read file."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='easysentiment',
    version='1.1',
    # scripts=['scraper_and_analysis.py', 'scraper.py', 'sentiment_analysis.py']
    author="Justin Flick",
    description=("GUI Application for Twitter Scraping and Sentiment Analysis using Python."),
    license="MIT",
    keywords=' '.join([
        "sentiment-analysis", "twitter-sentiment-analysis", "twitter-api",
        "twitter-scraping", "big-data", "naive-bayes-classification", "twitter-content-analysis",
        "gui"
    ]),
    url="https://github.com/Jflick58/Easysentiment",
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    setup_requires=['pytest-runner'],
    install_requires=[
        'easygui==0.98.1',
        'textblob==0.12.0',
        'twitterscraper==0.2.7',
    ],
    tests_require=[
        'pytest-flake8',
        'pytest',
        'pytest-cov'
    ],
    entry_points={
        'console_scripts': [
            'easysentiment=easysentiment.cli:cli',
        ],
    }
)
