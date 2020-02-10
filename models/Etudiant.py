"""Etudiant Model"""
import random

class Etudiant:
    """Class Model Etudiant"""
    _etudiant_instances = {}

    def __init__(self, nom, prenom, age, make_id=False):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        if make_id is False:
            self.id = self.make_id()
        else:
            self.id = make_id
        Etudiant._etudiant_instances[self.id] = self

    def make_id(self):
        """
            Confectionne un id, pour la DB d'une part
            et pour le dict statique d'autre part
        """
        r1 = random.randint(0, 3)
        r2 = random.randint(0, 3)
        etudiant_id = self.nom[:r1] + self.prenom[:r2] + str(self.age)

        if etudiant_id in Etudiant._etudiant_instances:
            self.make_id()
        else:
            return etudiant_id
