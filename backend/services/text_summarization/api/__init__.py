from flask_injector import FlaskInjector
from backend.services.text_summarization.api.server import server
from backend.services.text_summarization.application.configuration import Configuration
from backend.services.text_summarization.api.controllers.params_controller import ParamsController

api_name = '/text_summarization/api/v1/'

server.api.add_resource(ParamsController, api_name + 'predict', methods=["GET", "POST"])

flask_injector = FlaskInjector(app=server.app, modules=[Configuration])
