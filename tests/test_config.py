"""
    Unittest for conf/config.py
"""

from stock_common.conf.config import Config


def test_get_configs():
    """
        Test get configs method in Config class
    """

    CONFIGS = Config.get_configs()

    assert CONFIGS.ENV == 'prod'


def test_get_logging():

    CONFIGS = Config.get_configs()

    assert CONFIGS.get_logging() is not None
