from common.logging.console_loger import ConsoleLogger
from services.text_summarization.application.ai.model import T5Model
from services.text_summarization.application.ai.training.src.preprocess import Preprocess
from services.text_summarization.settings import Settings


class PredictionManager:
    def __init__(self, preprocess: Preprocess, logger: ConsoleLogger):
        self.preprocess = preprocess
        self.logger = logger
        self.settings = Settings
        self.__t5_model = None
        self.__load_model()

    def __load_model(self):
        try:
            self.logger.info(message="Loading T5(text-to-text-transfer-transformer) Model for text extraction.")
            self.__t5_model = T5Model(model_name=self.settings.MODEL_NAME,
                                      model_type=self.settings.MODEL_TYPE)

            self.__t5_model.load_model(model_type=self.settings.MODEL_TYPE,
                                       use_gpu=self.settings.USE_GPU,
                                       model_path=self.settings.WEIGHTS_PATH
                                       )
            self.logger.info(message="Model Weights loaded Successfully--!!")

        except BaseException as ex:
            self.logger.error(message="Exception Occurred while loading model---!! " + str(ex))

    def __predict(self, data):
        try:
            self.logger.info(message="Performing prediction on the given data.")

        except BaseException as ex:
            self.logger.error(message="Exception Occurred while prediction---!! " + str(ex))
