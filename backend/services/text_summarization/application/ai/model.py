from simplet5 import SimpleT5


class T5Model:
    def __init__(self, model_type, model_name):
        self.model = SimpleT5()
        self.model.from_pretrained(model_type=model_type,
                                   model_name=model_name)
