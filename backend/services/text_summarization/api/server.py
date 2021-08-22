from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from backend.services.text_summarization.api.decorators.request_logger import log_request


class Server:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if not Server.__instance:
            Server()
        return Server.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Server.__instance:
            raise Exception("This class is a singleton!")
        else:
            Server.__instance = self

        self.app = Flask(__name__)
        self.api = Api(self.app)

        @self.app.route("/", methods=["GET"])
        def render(path=None):
            return "Text Summarization Using T5(Text to Text Transfer Transformer) root page"

        # TODO: Allow restricted origins
        cors = CORS(self.app, resources={r"/*": {"origins": "*"}})
        self.app.before_request(log_request)
        # self.app.after_request(log_request)

    def run(self):
        self.app.config['PROPAGATE_EXCEPTIONS'] = True
        # self.app.register_error_handler(Exception, global_handle_error)
        # self.app.register_error_handler(DoesNotExist, does_not_exist_handle_error)
        # self.app.run(port=8080, use_reloader=False)
        self.app.run(host='0.0.0.0', port=8080, use_reloader=False)


server = Server.getInstance()
