import sys

from server.messages import *


class BanzeeException(Exception):
    """
    Abstrat class for Exception and Error
    """

    def __init__(self, code, attribute=None):
        self.__code = code
        self.__attribute = attribute

    def __str__(self):
        return "%s" % (self.__attribute)

    @property
    def code(self):
        """
        """
        return self.__code

    @property
    def attribute(self):
        """
        """
        return self.__attribute

    @property
    def message(self):
        """
        """
        return get_message(self.__code)


class InvalidRequestException(BanzeeException):
    """
    InvalidRequestException class
    """

    def __init__(self, attribute=None):
        super().__init__(400, attribute=attribute)


class APIAuthenticationFailedException(BanzeeException):
    """
    APIAuthentictionFailedException class
    """

    def __init__(self, inner_exception=None):
        super().__init__(401)


class ResourceNotFoundException(BanzeeException):
    """
    ResourceNotFoundException class
    """

    def __init__(self, inner_exception=None, data=None):
        super().__init__(404)


class OperationNotAllowedError(BanzeeException):
    """
    OperationNotAllowedError class
    """

    def __init__(self, inner_exception=None):
        super().__init__(405)


class ResourceDuplicatedException(BanzeeException):
    """
    ResourceDuplicatedException class
    """

    def __init__(self, inner_exception=None):
        super().__init__(409)


class InternalServerError(BanzeeException):
    """
    InternalServerError class
    """

    def __init__(self, inner_exception=None):
        super().__init__(500)


def handle_exception(occured_exception):
    error_type, error_instance, traceback = sys.exc_info()
    print(error_type, error_instance)
