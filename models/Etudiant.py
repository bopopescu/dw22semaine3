"""Etudiant Model"""
import random

class Etudiant:
    """Class Model Etudiant"""
    _etudiant_instances = {}

    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.id = nom + prenom[:2]
        Etudiant._etudiant_instances[self.id] = self

    def make_id(self, nom, prenom, age):
        """
            Confectionne un id, pour la DB d'une part
            et pour le dict statique d'autre part
        """
        r1 = random.randint(0, 3)
        r2 = random.randint(0, 3)
        etudiant_id = nom[:r1] + prenom[:r2] + age

        if etudiant_id in Etudiant._etudiant_instances:
            self.make_id(nom, prenom, age)
        else:
            return etudiant_id
