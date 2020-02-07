""" Index Controler """
import sys
sys.path.append('..')
import web
from web import form
from app import App

class Index:
    """Main page of application"""
    def __init__(self):
        # select all etudiants
        pass

    def GET(self):
        di = {
            "a": "dw22",
            "b": "hello"
        }
        return App.render.index(di)
