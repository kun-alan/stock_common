"""
    Database operations
"""

import logging

import wrapt
import pymongo


class Database():
    """
        Database class
    """

    def __init__(self, CONFIGS):
        """
        Attributes:
            CONFIGS: configuration class
        """
        self.configs = CONFIGS

    def connect(self, dbname):
        """Decorator for connecting database and closing connection

        Args:
            dbname (str):   'MONGO': MongoDB

        Returns:
            decorator

        Example:
            from stock_common.lib.database import Database
            from stock_common.conf.config import Config

            CONFIGS = Config.get_configs()
            db = Database(CONFIGS)

            @db.connect('MONGO')
            def pull_data(client):
                pass
        """

        @wrapt.decorator
        def with_connection(f, instance, args, kwargs):
            """Wrapping function and return the output of the origin function

            Args:
                f (function/method)
                instance : pass in self when wraping class method.
                            default is None when wraping function.
            Return:
                pass cursor into the origin function, and return the output

            """

            if dbname.upper() == 'MONGO':

                logging.info(
                    'Connecting to MONGO: %s', self.configs.MONGO_HOST)

                cursor = pymongo.MongoClient(
                    self.configs.MONGO_HOST, self.configs.MONGO_PORT)

                if self.configs.MONGO_AUTH_ENABLED:
                    cursor.admin.authenticate(
                        self.configs.MONGO_USER, self.configs.MONGO_PASS,
                        mechanism=self.configs.MONGO_AUTH_METHOD
                    )
            else:
                logging.error('%s is not supported yet', dbname)
            try:
                output = f(cursor, *args, **kwargs)

            except Exception as err:
                logging.error(err)
                raise

            finally:
                logging.info('Closing Database Cursor and Connection')
                cursor.close()

            return output

        return with_connection
