#This is custom exception library used in the framework

class FrameworkException(Exception):
    """Base class for all framework exceptions"""
    pass


class ElementNotFoundException(FrameworkException):
    pass


class ElementNotClickableException(FrameworkException):
    pass


class TextNotFoundException(FrameworkException):
    pass