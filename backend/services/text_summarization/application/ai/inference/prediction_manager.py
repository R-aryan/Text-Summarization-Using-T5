from common.logging.console_loger import ConsoleLogger
from services.text_summarization.application.ai.training.src.preprocess import Preprocess
from services.text_summarization.settings import Settings


class PredictionManager:
    def __init__(self, preprocess: Preprocess, logger: ConsoleLogger):
        self.preprocess = preprocess
        self.logger = logger
        self.settings = Settings
        self.__model = None
        self.__load_model()

    def __load_model(self):
        try:
            self.logger.info(message="Loading T5(text-to-text-transfer-transformer) Model for text extraction.")

        except BaseException as ex:
            self.logger.error(message="Exception Occurred while loading model---!! " + str(ex))