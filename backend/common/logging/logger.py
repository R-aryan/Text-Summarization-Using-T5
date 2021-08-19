import abc
from abc import ABCMeta


class Logger(metaclass=ABCMeta):
    def __init__(self):
        super(Logger, self).__init__()

    @abc.abstractmethod
    def debug(self, message, file_id='', context=''):
        pass

    @abc.abstractmethod
    def info(self, message, file_id='', context=''):
        pass

    @abc.abstractmethod
    def warning(self, message, file_id='', context=''):
        pass

    @abc.abstractmethod
    def error(self, message, file_id='', context=''):
        pass

    @abc.abstractmethod
    def fatal(self, message, file_id='', context=''):
        pass
