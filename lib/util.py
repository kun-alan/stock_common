"""
    Common functions that being used in watcher recommender and advisor
"""

import pandas_datareader.data as web


def get_quote(symbols):
    """
    Get the current price of symbol(s) from Yahoo Finance

    Args:
        symbols (list or str): 'AAPL', ['AAPL', 'F']

    Returns:
        dict
    """

    return web.get_quote_yahoo(symbols)
