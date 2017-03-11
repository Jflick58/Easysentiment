"""test module."""
from unittest import mock

import pytest


@pytest.mark.parametrize('argv', ['scrape', 'scrape-and-analyze', 'analyze-sentiment'])
def test_cli(argv):
    """test function."""
    with mock.patch('easysentiment.cli.scrape') as m_scrape, \
            mock.patch('easysentiment.cli.scrape_and_analyze') as m_saa, \
            mock.patch('easysentiment.cli.analyze_sentiment') as m_as:
        mock_dict = {
            'scrape': m_scrape,
            'scrape-and-analyze': m_saa,
            'analyze-sentiment': m_as,
        }
        from easysentiment.cli import cli
        cli([argv])
        mock_dict[argv].assert_called_once_with()
