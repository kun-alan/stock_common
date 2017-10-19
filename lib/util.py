"""
    Common functions that being used in watcher recommender and advisor
"""

from .quotes import get_quote_yahoo


def get_quote(symbols):
    """
    Get the current price of symbol(s) from Yahoo Finance

    Args:
        symbols (list or str): 'AAPL', ['AAPL', 'F']

    Returns:
        dict
    """

    return get_quote_yahoo(symbols)
