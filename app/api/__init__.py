"""Th"""
from flask import Flask
from app.api.v1.views.user import USERVIEW
from app.api.v1.views.viewquestions import QUESTION_BLUEPRINT



APP = Flask(__name__)


APP.register_blueprint(QUESTION_BLUEPRINT)
APP.register_blueprint(USERVIEW)

