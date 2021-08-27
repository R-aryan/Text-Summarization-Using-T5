import logging
# from backend.common.logging.logger import Logger


class ConsoleLogger:
    def __init__(self, filename='logs.txt', logging_level=logging.INFO):
        # super(ConsoleLogger, self).__init__()
        if logging_level not in [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.FATAL]:
            raise Exception('Unable to instantiate logger with given exception level')

        self.filename = filename
        logging.basicConfig(filename=self.filename,
                            format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
                            datefmt="%d-%b-%Y : %H:%M:%S"
                            )

        self.logger = logging.getLogger()
        self.logger.setLevel(logging_level)
        # self.logger.addHandler()
        self.context = ""

    def debug(self, message, file_id='', context=''):
        self.logger.debug(msg='DEBUG : '+message)
        print('DEBUG: ' + message)

    def info(self, message, file_id='', context=''):
        self.logger.info(msg='INFO : ' + message)
        print('INFO: ' + message)

    def warning(self, message, file_id='', context=''):
        self.logger.warning(msg='WARNING : ' + message)
        print('WARNING: ' + message)

    def error(self, message, file_id='', context=''):
        self.logger.error(msg='ERROR : ' + message)
        print('ERROR: ' + message)

    def fatal(self, message, file_id='', context=''):
        self.logger.fatal(msg='FATAL : ' + message)
        print('FATAL: ' + message)
