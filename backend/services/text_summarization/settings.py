import os
import torch
from tokenizers.implementations import BertWordPieceTokenizer


class Settings:
    PROJ_NAME = 'Text-Summarization-Using-T5'
    root_path = os.getcwd().split(PROJ_NAME)[0] + PROJ_NAME + "\\"
    APPLICATION_PATH = root_path + "backend\\services\\text_summarization\\application\\"
    # setting up logs path
    LOGS_DIRECTORY = root_path + "backend\\services\\text_summarization\\logs\\logs.txt"
