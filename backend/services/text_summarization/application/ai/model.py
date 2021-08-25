from simplet5 import SimpleT5


class T5Model:
    def __init__(self, model_type, model_name):
        self.model = SimpleT5()
        self.model.from_pretrained(model_type=model_type,
                                   model_name=model_name)

    def load_model(self, model_type, model_path, use_gpu: bool):
        try:
            self.model.load_model(
                model_type=model_type,
                model_dir=model_path,
                use_gpu=use_gpu
            )

        except BaseException as ex:
            print("error occurred while loading model ", str(ex))
