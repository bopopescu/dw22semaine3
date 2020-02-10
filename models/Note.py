"""Note Model"""
from models.Etudiant import Etudiant
from models.Cours import Cours

class Note:
    _note_instances = []

    def __init__(self, note, etudiant, cours, id_model=False):
        if id_model is not False:
            self.etudiant_id = Etudiant._etudiant_instances[etudiant].id
            self.cours_id = Cours._cours_instances[cours].id
        else:
            self.etudiant_id = etudiant.id
            self.cours_id = cours.id
        self.note = note
        Note._note_instances.append(self)
