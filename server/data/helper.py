"""
helper.py
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session

from server.config import Config


class ConnectionHelper(object):
    """
    Connection helper class
    """

    def __init__(self):
        self.__host = Config.DATABASE_HOST
        self.__port = Config.DATABASE_PORT
        self.__database = Config.DATABASE_NAME
        self.__user = Config.DATABASE_USER
        self.__password = Config.DATABASE_PASSWORD


    def get_connection(self):
        """
        Establish and provide connection
        """

        try:
            connection_uri = 'mysql+pymysql://' + self.__user + ':' + self.__password + '@' + self.__host + '/' + self.__database
            engine = create_engine(connection_uri,
                                   isolation_level='AUTOCOMMIT')
            conn = engine.connect()

        except:
            raise

        return conn


    def get_session(self):
        """
        Establish and provide a session
        """

        try:
            connection_uri = "mysql+pymysql://" + self.__user + ":" + self.__password + "@" + self.__host + "/" + self.__database
            engine = create_engine(connection_uri, 
                                    pool_size=5, 
                                    max_overflow=1000)
            #session = scoped_session(sessionmaker(bind=engine))
            session = Session(sessionmaker(bind=engine, autocommit=True))
        except:
            raise
        
        return session
