"""
Main entry point of Banzee API application

Usages:
    python app.py
"""

import os
from flask import Flask

from server.config import Config


app = Flask(__name__, static_folder=os.path.join('server', 'static'))
app.url_map.strict_slashes = False


if __name__ == '__main__':
    app.run(debug=Config.DEBUG)
