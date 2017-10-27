"""
    Unittest for lib/util.py
"""

import datetime

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


def test_read_data():
    """
        Test read historical data
    """

    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=5)
    pf = util.read_data(['AAPL', 'F'], start_date, end_date)

    assert pf.Close.empty is False


def test_date_to_int():
    """
        Convert date object to int
    """

    assert util.date_to_int(datetime.datetime(2017, 10, 1)) == 20171001
