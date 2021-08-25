from services.text_summarization.application.ai.training.src.preprocess import Preprocess
from services.text_summarization.settings import Settings


class Train:
    def __init__(self):
        # initialize required class
        self.settings = Settings
        self.preprocess = Preprocess()

