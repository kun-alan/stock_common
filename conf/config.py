"""
    Configurations

    config.py keeps public configurations
    secret.py keeps sensitive information
    such as username and password

    By default, we alway use prod env, when you need to test your scripts
    with your local mongo during development, you can use dev env

    secret.py example:

        class SecretProd():
            MONGO_HOSTS = 'example.com'
            MONGO_USER = 'foo'
            MONGO_PASS = 'bar'
            MONGO_PORT = 27017
            MONGO_AUTH_METHOD = 'example'
            MONGO_AUTH_ENABLED = True

        class SecretDev(SecretProd):
            MONGO_HOSTS = 'localhost'
            MONGO_AUTH_ENABLED = False
"""

import os
import inspect
import logging

from stock_common.conf.secret import SecretProd, SecretDev


def get_caller_info():
    """
        Getting Filename and Path of Caller
    """

    try:
        frame = inspect.stack()[2]
        module = inspect.getmodule(frame[0])
        caller = module.__file__
        filename = os.path.splitext(os.path.basename(caller))[0]
        current_path = os.path.dirname(os.path.realpath(caller))
        return filename, current_path
    except (IndexError, AttributeError):
        return None, None


class Config():
    """
        Configuration Class
    """

    @classmethod
    def get_configs(cls, env='prod'):
        """
            Getting Configs for specific environment

        Args:
            env (str): (prod|dev), default 'prod'
        Returns:
            CONFIGS class
        """

        if env == 'prod':
            CONFIGS = cls.Prod()
        elif env == 'dev':
            CONFIGS = cls.Dev()
        else:
            raise ValueError('{env} not supported.'.format(env=env))

        CONFIGS.FILENAME, CONFIGS.CURRENT_PATH = get_caller_info()

        return CONFIGS

    class Prod(SecretProd):
        """
            Configurations For Production Environment
        """

        ENV = 'prod'

        # LOG Configs
        LOG_LEVEL = logging.INFO
        LOG_FORMAT = '%(asctime)s %(levelname)-8s %(message)s'
        LOG_DATEFORMAT = '%a, %d %b %Y %H:%M:%S'
        LOG_FILEMODE = 'a'
        LOG_BASE_PATH = os.path.expanduser('~/kun_alan/log/')

        def get_logging(self):
            """
                Setting logging module to default configurations

            Examples:
                >>> from stock_common.conf.config import Config
                >>> CONFIGS = Config.get_configs()
                >>> logging = CONFIGS.get_logging()
            """

            logging.basicConfig(
                level=self.LOG_LEVEL, format=self.LOG_FORMAT,
                datefmt=self.LOG_DATEFORMAT, filemode=self.LOG_FILEMODE,
                filename='{0}{1}.log'.format(
                    self.LOG_BASE_PATH, self.FILENAME)
            )

            return logging

    class Dev(SecretDev):
        """
            Configurations For Develop Environment
        """

        ENV = 'dev'
