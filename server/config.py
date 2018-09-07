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
    DATABASE_NAME = 'db_microtransaction'
    DATABASE_USER = ''
    DATABASE_PASSWORD = ''

    ELASTICSEARCH_HOST = ''
    ELASTICSEARCH_PORT = 443
    ELASTICSEARCH_USE_SSL = True
    ELASTICSEARCH_VERIFY_CERT = False
    ELASTICSEARCH_HTTP_COMPRESS = False
    ELASTICSEARCH_BULK_DOC_COUNT = 500


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
    DATABASE_USER = ''
    DATABASE_PASSWORD = ''

    ELASTICSEARCH_HOST = ''
    ELASTICSEARCH_PORT = 443
    ELASTICSEARCH_USE_SSL = True
    ELASTICSEARCH_VERIFY_CERT = False
    ELASTICSEARCH_HTTP_COMPRESS = False
    ELASTICSEARCH_BULK_DOC_COUNT = 500


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
    DATABASE_USER = ''
    DATABASE_PASSWORD = ''

    ELASTICSEARCH_HOST = ''
    ELASTICSEARCH_PORT = 443
    ELASTICSEARCH_USE_SSL = True
    ELASTICSEARCH_VERIFY_CERT = False
    ELASTICSEARCH_HTTP_COMPRESS = False
    ELASTICSEARCH_BULK_DOC_COUNT = 500


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
    DATABASE_USER = 'banzee'
    DATABASE_PASSWORD = ''

    ELASTICSEARCH_HOST = ''
    ELASTICSEARCH_PORT = 443
    ELASTICSEARCH_USE_SSL = True
    ELASTICSEARCH_VERIFY_CERT = False
    ELASTICSEARCH_HTTP_COMPRESS = False
    ELASTICSEARCH_BULK_DOC_COUNT = 500


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
    DATABASE_USER = 'banzee'
    DATABASE_PASSWORD = ''


    ELASTICSEARCH_HOST = '127.0.0.1'
    ELASTICSEARCH_PORT = 9200
    ELASTICSEARCH_USE_SSL = True
    ELASTICSEARCH_VERIFY_CERT = False
    ELASTICSEARCH_HTTP_COMPRESS = True
    ELASTICSEARCH_BULK_DOC_COUNT = 500


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
