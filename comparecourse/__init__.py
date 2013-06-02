import os
from flask import Flask
app = Flask(__name__)
app.config.from_object('config')

import comparecourse.schema
import comparecourse.views
