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
