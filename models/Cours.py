"""Etudiant Model"""

class Cours:
    _cours_instances = {}

    def __init__(self, nom, annee, make_id=False):
        if make_id is False:
            self.id = self.check_if_exist(nom, annee)
        else:
            self.id = make_id
        self.nom = nom
        self.annee = annee
        Cours._cours_instances[self.id] = self

    def check_if_exist(self, nom, annee):
        check_id = nom + "_" + annee
        if check_id in Cours._cours_instances:
            raise Exception
        return check_id
