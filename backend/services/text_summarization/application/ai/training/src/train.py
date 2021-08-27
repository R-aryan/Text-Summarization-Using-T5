import numpy as np
import torch

from services.text_summarization.application.ai.model import T5Model
from services.text_summarization.application.ai.training.src.preprocess import Preprocess
from services.text_summarization.settings import Settings

from sklearn.model_selection import train_test_split
import random


class Train:
    def __init__(self):
        # initialize required class
        self.settings = Settings
        self.preprocess = Preprocess()

        # initialize required variables
        self.t5_model = None

    def __initialize(self):
        try:
            self.t5_model = T5Model(model_name=self.settings.MODEL_NAME,
                                    model_type=self.settings.MODEL_TYPE)

        except BaseException as ex:
            print("error occurred while loading model ", str(ex))

    def set_seed(self, seed_value=42):
        random.seed(seed_value)
        np.random.seed(seed_value)
        torch.manual_seed(seed_value)
        torch.cuda.manual_seed_all(seed_value)

    def train(self, df):
        try:
            train_df, test_df = train_test_split(df, test_size=self.settings.TEST_SIZE)

            self.t5_model.model.train(train_df=train_df[:self.settings.train_df_len],
                                      eval_df=test_df[:self.settings.test_df_len],
                                      source_max_token_len=self.settings.source_max_token_len,
                                      target_max_token_len=self.settings.target_max_token_len,
                                      batch_size=self.settings.BATCH_SIZE, max_epochs=self.settings.EPOCHS,
                                      use_gpu=self.settings.USE_GPU)

        except BaseException as ex:
            print("error occurred while loading model ", str(ex))

    def run(self):
        try:
            print("Loading and Preparing the Dataset-----!! ")
            df = self.preprocess.preprocess_data(self.settings.TRAIN_DATA)
            print("Dataset Successfully Loaded and Prepared-----!! ")
            print("Loading and Initializing the T5 Model -----!! ")
            self.__initialize()
            print("Model Successfully Loaded and Initialized-----!! ")

            print("------------------Starting Training-----------!!")
            self.set_seed()
            self.train(df)
            print("Training complete-----!!!")

        except BaseException as ex:
            print("Following Exception Occurred---!! ", str(ex))
