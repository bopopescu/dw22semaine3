""" Etudiant Controler """
import sys
sys.path.append('..')
import web
from web import form
from app import App
from models.Etudiant import Etudiant as model



class Etudiant:
    """Etudiant class"""
    def __init__(self):
        self.to_render = {}
        self.to_render["form"] = self.add_etudiant_form()

    def add_etudiant_form(self):
        """Form pour ajouter un étudiant"""
        vnom = form.regexp(r"[a-zA-Z]+", " Des lettres uniquement")
        vprenom = form.regexp(r"[a-zA-Z]+", " Des lettres uniquement")
        vage = form.regexp(r"[1-9][0-9]+", " Des chiffres uniquement")

        add_etudiant_form = form.Form(
            form.Textbox("nom", vnom, description="Nom de l'étudiant"),
            form.Textbox("prenom", vprenom, description="Prénom de l'étudiant"),
            form.Textbox("age", vage, description="Age de l'étudiant"),
            form.Button("valider", type="submit", description="Valider")
        )

        return add_etudiant_form

    def GET(self):
        return App.render.etudiant(self.to_render)

    def POST(self):
        if not self.to_render["form"].validates():
            App.render.etudiant(self.to_render)
        else:
            self.to_render['post'] = web.input()
        return App.render.etudiant(self.to_render)

    def init_model(self, nom, prenom, age):
        """Init le modele etudiant"""
        return model(nom, prenom, age)
