"""
    Unittest for lib/database.py
"""

import pymongo

from stock_common.lib.database import Database
from stock_common.conf.config import Config

CONFIGS = Config.get_configs()
db = Database(CONFIGS)


def test_connect_mongo():
    """
        Test decorating a function with MongoDB connection
    """

    @db.connect('MONGO')
    def pull_data(client):
        return client

    client = pull_data()

    assert type(client) is pymongo.MongoClient
