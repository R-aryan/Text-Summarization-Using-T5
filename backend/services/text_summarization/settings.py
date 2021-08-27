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

    USE_GPU = None
    if str(DEVICE) == "cuda":
        USE_GPU = True
    else:
        USE_GPU = False

    EPOCHS = 5

    encoding = 'latin-1'
    columns_dict = {"headlines": "target_text", "text": "source_text"}
    df_column_list = ['source_text', 'target_text']
    SUMMARIZE_KEY = "summarize: "
    SOURCE_TEXT_KEY = 'source_text'
    TEST_SIZE = 0.2
    BATCH_SIZE = 8
    source_max_token_len = 128
    target_max_token_len = 50
    train_df_len = 5000
    test_df_len = 100

    WEIGHTS_PATH = APPLICATION_PATH + "ai\\weights\\SimpleT5-epoch-4-train-loss-0.6182"
    kaggle_dir = ''

    # constants
    DATA_KEY = 'data'
