"""
Copyright 2017 Grocery Heaven, Inc. or its affiliates. All Rights Reserved.

"""

import os


class ConfigBase(object):
    """
    Base class for managing configuration.
    """
    DEBUG = False

    AWS_ACCESS_KEY_ID = ''
    AWS_SECRET_ACCESS_KEY = ''
    AWS_DEFAULT_REGION = 'us-west-2'

    DATABASE_HOST = ''
    DATABASE_PORT = '3306'
    DATABASE_NAME = 'db_microtransaction'
    DATABASE_USER = 'banzee'
    DATABASE_PASSWORD = ''

    ISOLATION_LEVEL = 'AUTOCOMMIT'
    POOL_SIZE = 5
    MAX_OVERFLOW = 1000


class ProductionConfig(ConfigBase):
    """
    Configuration class for managing production environment.
    """
    DEBUG = False

    AWS_ACCESS_KEY_ID = ''
    AWS_SECRET_ACCESS_KEY = ''
    AWS_DEFAULT_REGION = 'us-west-2'

    DATABASE_HOST = ''
    DATABASE_NAME = 'db_microtransaction'
    #DATABASE_USER = ''
    DATABASE_PASSWORD = ''


class StagingConfig(ConfigBase):
    """
    Configuration class for managing staging environment.
    """
    DEBUG = False

    AWS_ACCESS_KEY_ID = ''
    AWS_SECRET_ACCESS_KEY = ''
    AWS_DEFAULT_REGION = 'us-west-2'

    DATABASE_HOST = ''
    DATABASE_NAME = 'db_microtransaction'
    #DATABASE_USER = ''
    DATABASE_PASSWORD = ''


class DevelopmentConfig(ConfigBase):
    """
    Configuration class for managing development environment.
    """
    DEBUG = True

    AWS_ACCESS_KEY_ID = ''
    AWS_SECRET_ACCESS_KEY = ''
    AWS_DEFAULT_REGION = 'us-west-2'

    DATABASE_HOST = ''
    DATABASE_NAME = 'db_microtransaction'
    #DATABASE_USER = 'banzee'
    DATABASE_PASSWORD = ''


class LocalConfig(ConfigBase):
    """
    Configuration class for managing local test environment.
    """
    DEBUG = True

    AWS_ACCESS_KEY_ID = ''
    AWS_SECRET_ACCESS_KEY = ''
    AWS_DEFAULT_REGION = 'us-west-2'

    DATABASE_HOST = '127.0.0.1'
    DATABASE_NAME = 'db_microtransaction'
    #DATABASE_USER = 'banzee'
    DATABASE_PASSWORD = 'banzee!$'


Config = None
env = os.environ.get('BANZEE_SERVER_ENVIRONMENT')
if env == 'Production':
    Config = ProductionConfig()
elif env == 'Staging':
    Config = StagingConfig()
elif env == 'Development':
    Config = DevelopmentConfig()
elif env == 'Local':
    Config = LocalConfig()
else:
    raise ValueError('Wrong BANZEE_SERVER_ENVIRONMENT value.')
