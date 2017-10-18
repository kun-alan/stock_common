"""
    Unittest for conf/config.py
"""

from stock_common.conf.config import Config


def test_get_configs():
    """
        Test get configs method in Config class
    """

    CONFIGS = Config.get_configs()
    DEV_CONFIGS = Config.get_configs('dev')

    assert CONFIGS.ENV == 'prod'
    assert CONFIGS.MONGO_HOST

    assert DEV_CONFIGS.ENV == 'dev'
    assert DEV_CONFIGS.LOG_FILEMODE
    assert DEV_CONFIGS.MONGO_HOST


def test_get_logging():

    CONFIGS = Config.get_configs()

    assert CONFIGS.get_logging() is not None
