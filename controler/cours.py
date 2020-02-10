""" Cours Controler """
import sys
sys.path.append('..')
import web
from web import form
from app import App
from models.Cours import Cours as Model


class Cours:
    """Cours class"""
    def __init__(self):
        self.to_render = {}
        self.to_render["form"] = self.add_cours_form()

    def add_cours_form(self):
        """Form pour ajouter un étudiant"""
        vnom = form.regexp(r"[a-zA-Z]+", " Des lettres uniquement")
        vannee = form.regexp(r"[1-9][0-9]{3}", " Quatres chiffres uniquement")

        add_cours_form = form.Form(
            form.Textbox("nom", vnom, description="Nom du cours"),
            form.Textbox("annee", vannee, description="Annee du cours"),
            form.Button("valider", type="submit", description="Valider")
        )
        return add_cours_form

    def GET(self):
        return App.render.cours(self.to_render)

    def POST(self):
        if not self.to_render["form"].validates():
            App.render.cours(self.to_render)
        else:
            self.to_render['post'] = web.input()
            post = self.to_render['post']
            self.init_model(post['nom'], post['annee'])
        return App.render.cours(self.to_render)

    def init_model(self, nom, annee):
        """Init le modele etudiant"""
        try:
            new_cours = Model(nom, annee)
            App().add_cours(new_cours)
        except Exception:
            self.to_render['post'] = False
