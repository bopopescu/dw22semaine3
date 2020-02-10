"""Profile controler"""
import sys
sys.path.append('..')
import web
from web import form
from app import App
from models.Etudiant import Etudiant as ModelEtudiant
from models.Cours import Cours as ModelCours
from models.Note import Note as ModelNote

class Profile: 
    def __init__(self):
        self.to_render = {}
        #self.to_render['notes'] = []
        self._cours = []
        self._notes = list(range(0, 21))
        if len(ModelCours._cours_instances) > 0:
            for cours_id in ModelCours._cours_instances:
                self._cours.append(cours_id)
            self.to_render["form"] = self.add_note_form()
        else:
            self._cours = False

    def add_note_form(self):
        add_note_form = form.Form(
            form.Dropdown("cours", self._cours, value=self._cours[0]),
            form.Dropdown("note", self._notes, value=self._notes[10]),
            form.Button("valider", type="submit", description="Valider")
        )
        return add_note_form

    def GET(self, etu_id):
        self.get_notes(etu_id)
        if self._cours == False:
            self.to_render['no_cours'] = True
        else:
            self.to_render['etu'] = ModelEtudiant._etudiant_instances[etu_id]
        return App.render.profile(self.to_render)

    def POST(self, etu_id):
        self.get_notes(etu_id)
        self.to_render['etu'] = ModelEtudiant._etudiant_instances[etu_id]
        if not self.to_render["form"].validates():
            App.render.profile(self.to_render)
        else:
            self.to_render['post'] = web.input()
            post = self.to_render['post']
            self.init_model(post['note'], etu_id, post['cours'])
            self.get_notes(etu_id)
        return App.render.profile(self.to_render)

    def init_model(self, note, etu_id, cours_id):
        etudiant = ModelEtudiant._etudiant_instances[etu_id]
        cours = ModelCours._cours_instances[cours_id]
        new_note = ModelNote(note, etudiant, cours)
        App().add_note(new_note)

    def get_notes(self, etu_id):
        print('get_notes')
        _notes_etu = []
        if len(ModelNote._note_instances) > 0:
            for n in ModelNote._note_instances:
                print(n.etudiant_id)
                if n.etudiant_id == etu_id:
                    _notes_etu.append(n)
            if len(_notes_etu) > 0:
                self.to_render['notes'] = _notes_etu
                return self.to_render['notes']
        return False
