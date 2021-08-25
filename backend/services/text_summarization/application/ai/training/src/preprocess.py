import re
import string

import pandas as pd

from services.text_summarization.settings import Settings


class Preprocess:
    def __init__(self):
        self.settings = Settings

    def clean_text(self, text):
        text = text.lower()
        text = re.sub('\[.*?\]', '', text)
        text = re.sub('https?://\S+|www\.\S+', '', text)
        text = re.sub('<.*?>+', '', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub('\n', '', text)
        text = re.sub('\w*\d\w*', '', text)
        return text

    def preprocess_data(self, data_path):
        df = pd.read_csv(data_path, encoding=self.settings.encoding, usecols=self.settings.Columns)
        # simpleT5 expects dataframe to have 2 columns: "source_text" and "target_text"
        df = df.rename(columns=self.settings.columns_dict)
        df = df[self.settings.df_column_list]
        # T5 model expects a task related prefix: since it is a summarization task, we will add a prefix "summarize: "
        df[self.settings.SOURCE_TEXT_KEY] = self.settings.SUMMARIZE_KEY + df[self.settings.SOURCE_TEXT_KEY]
