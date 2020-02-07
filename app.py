import web
from router import Router
from dbHandle import DBHandle

class App:
    """Application"""
    # Ici les instances statiques des objets de l'application
    urls = Router.urls
    app = web.application(urls, globals())
    render = web.template.render('templates/', base='layout')
    dbHandle = DBHandle()

    def __init__(self):
        pass

    def add_etudiant(self):
        """Import new etudiant in DB"""