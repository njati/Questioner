"""Th"""
from flask import Flask
from app.api.v1.views.user import USERVIEW
from app.api.v1.views.viewquestions import QUESTION_BLUEPRINT
from app.api.v1.views.viewmeetups import MEETUP
from app.api.v1.views.updownview import VOTES_BLUEPRINT



APP = Flask(__name__)


APP.register_blueprint(QUESTION_BLUEPRINT)
APP.register_blueprint(USERVIEW)
APP.register_blueprint(MEETUP)
APP.register_blueprint(VOTES_BLUEPRINT)

