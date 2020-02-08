""" Index Controler """
import sys
sys.path.append('..')
#import web
#from web import form
from app import App
from models.Etudiant import Etudiant

class Index:
    """Main page of application"""
    def __init__(self):
        self.to_render = {}
        pass

    def GET(self):
        if len(Etudiant._etudiant_instances) > 0:
            self.to_render['_etudiants'] = Etudiant._etudiant_instances
        return App.render.index(self.to_render)
