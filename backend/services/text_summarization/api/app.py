import os
import sys

# root_path = os.getcwd()
# sys.path.append(root_path + '/services')
# sys.path.append(root_path)
# os.environ['PYTHONPATH'] = root_path + '/services' + root_path
from backend.services.text_summarization.api import server

app = server.app

if __name__ == "__main__":
    server.run()
