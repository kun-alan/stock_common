"""
    Unittest for lib/util.py
"""

from stock_common.lib import util


def test_get_quote_one():
    """
        Test get quote function in lib/util.py
    """

    df_quote = util.get_quote('AAPL')

    assert df_quote.empty is False


def test_get_quote_multiple():
    """
        Test get quote function in lib/util.py with a list of symbols
    """

    df_quote = util.get_quote(['AAPL', 'F'])

    assert df_quote.empty is False
