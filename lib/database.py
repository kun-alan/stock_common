"""
    Database operations
"""

import logging

import wrapt
import pymongo


class Database():

    def __init__(self, CONFIGS):
        """
        Attributes:
            CONFIGS: configuration class
        """
        self.CONFIGS = CONFIGS

    def connect(self, dbname):
        """Decorator for connecting database and closing connection

        Args:
            dbname (str):   'MONGO': MongoDB

        Returns:
            decorator
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

                logging.info('Connecting to MONGOS: {host}'.format(
                    host=self.CONFIGS.MONGO_HOSTS))

                cursor = pymongo.MongoClient(
                    self.CONFIGS.MONGO_HOSTS, self.CONFIGS.MONGO_PORT)

                if self.CONFIGS.MONGO_AUTH_ENABLED:
                    cursor.admin.authenticate(
                        self.CONFIGS.MONGO_USER, self.CONFIGS.MONGO_PASS,
                        mechanism=self.CONFIGS.MONGO_AUTH_METHOD
                    )
            else:
                logging.error('{dbname} is not supported yet'.format(
                    dbname=dbname))
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
