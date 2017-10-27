"""
    Common functions that being used in watcher recommender and advisor
"""

import logging
import datetime

import pandas_datareader.data as web
from pandas_datareader.yahoo import quotes

from stock_common.conf.config import Config
from stock_common.lib.database import Database

CONFIGS = Config.get_configs()
db = Database(CONFIGS)

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


def read_data(symbols, start, end):
    """
    Args:
        symbols (list or str): 'AAPL', ['AAPL', 'F']
        start (date object)
        end (date object)
    Returns:
        panel or dataframe
    """

    pf = web.DataReader(symbols, 'google', start, end)

    return pf


def date_to_int(date):
    """
    Args:
        date (date object)
    Returns:
        int: YYYYMMDD
    """
    return int(datetime.datetime.strftime(date, '%Y%m%d'))


@db.connect('MONGO')
def insert_documents_to_mongo(
    client, db, collection, documents, delete=None, replace=None
):
    """Insert Documents into MongoDB

    Args:
        db (str): MongoDB Database name
        collection (str): Mongo Collection name
        documents (list of dicts): MongoDB documents
        delete (dict): delete documents before writing,
            eg. {'weekEnding': 20170402}
            pass in {} if want to delete all
            default None
        replace (list): replace documents based on keys
            eg. ['_id', 'otherKey'] to replace documents where
                {'_id': document[_id], 'otherKey': document[otherKey]}
            default None
    """

    if not isinstance(documents, (list, tuple)):
        documents = [documents]

    if isinstance(delete, dict):
        logging.info(
            'Removing Documents from Mongo: delete_many({delete})'.format(
                delete=delete))

        client[db][collection].delete_many(delete)

    if replace and isinstance(replace, list):
        logging.info(
            'Replacing Document Into Mongo:replace(Columns{replace})'
            .format(replace=replace)
        )

        for document in documents:

            replace_statement =\
                {replace_key: document[replace_key]
                    for replace_key in replace}

            client[db][collection].replace_one(
                replace_statement, document, True)

    else:
        logging.info(
            'Inserting Documents into Mongo {db}.{collection}'.format(
                db=db, collection=collection))
        client[db][collection].insert_many(documents)
