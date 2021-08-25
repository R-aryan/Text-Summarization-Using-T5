import os

import torch


class Settings:
    PROJ_NAME = 'Text-Summarization-Using-T5'
    root_path = os.getcwd().split(PROJ_NAME)[0] + PROJ_NAME + "\\"
    APPLICATION_PATH = root_path + "backend\\services\\text_summarization\\application\\"
    # setting up logs path
    LOGS_DIRECTORY = root_path + "backend\\services\\text_summarization\\logs\\logs.txt"

    MODEL_TYPE = "t5"
    MODEL_NAME = "t5-base"

    DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # training data directory
    TRAIN_DATA = APPLICATION_PATH + "ai\\data\\news_summary.csv"

    Columns = ['headlines', 'text']

    USE_GPU = True if DEVICE == "cuda" else False

    EPOCHS = 5



