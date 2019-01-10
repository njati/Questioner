"""Th"""
from flask import Flask
from app.api.v1.views.user import USERVIEW


APP = Flask(__name__)


APP.register_blueprint(USERVIEW)