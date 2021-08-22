from flask import request
from injector import inject

from backend.services.text_summarization.api.controllers.controller import Controller


class ParamsController(Controller):
    @inject
    def __init__(self):
        pass

    def post(self):
        return "Text Summarization post request"

    def get(self):
        return {'response': 'This is an API endpoint for text summarization---!!'}
