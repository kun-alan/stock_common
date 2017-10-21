"""
    Common functions that being used in watcher recommender and advisor
"""

from pandas_datareader.yahoo import quotes
quotes._yahoo_codes = {
    'symbol': 's', 'last': 'l1', 'change_pct': 'p2', 'PE': 'r',
    'time': 't1', 'short_ratio': 's7', 'date': 'd1'
}


def get_quote(symbols):
    """
    Get the current price of symbol(s) from Yahoo Finance

    Args:
        symbols (list or str): 'AAPL', ['AAPL', 'F']

    Returns:
        dict
    """

    return quotes.YahooQuotesReader(symbols).read()
