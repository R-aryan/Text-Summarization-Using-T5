from flask import request
from injector import inject

from backend.common.logging.console_loger import ConsoleLogger


@inject
def log_request(logger: ConsoleLogger):
    logger.info(request.method + ' request received:' + request.url)
