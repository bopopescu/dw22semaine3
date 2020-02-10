#!./env/bin/python3
"""Database Handle"""
import web
import pymysql
import mysql.connector
from models.Etudiant import Etudiant
from models.Cours import Cours
from models.Note import Note

class DBHandle:

    tables = []
    status = False

    def __init__(self):
        # Pour transaction
        self.webdb = web.database(
            dbn='mysql',
            host='localhost',
            port=3306,
            user='test',
            pw='test',
            db='quentinvinot',
        )

        # Pour créer les tables si nescessaire
        self.mysqlco = mysql.connector.connect(
            host="localhost",
            user="test",
            passwd="test",
            database="quentinvinot",
            auth_plugin="mysql_native_password"
        )

        self.cursor = self.mysqlco.cursor()
        DBHandle.status = self.table_init()
        self.load_db()


    def check_tables(self):
        self.cursor.execute("SHOW TABLES")

        for x in self.cursor:
            print(x[0])
            DBHandle.tables.append(x[0])
            print(DBHandle.tables)

        if '_etudiants' in DBHandle.tables \
        and '_etudiants' in DBHandle.tables \
        and '_cours' in DBHandle.tables:
            print('tables OK')
        else:
            print('tables not loaded')
            return False
        return True

    def table_init(self):
        if not self.check_tables():
            for line in open('./sql.sql'):
                self.cursor.execute(line)
        return True

    def info_tables(self):
        if DBHandle.status:
            info_tables = []
            for x in DBHandle.tables:
                query = "describe " + x
                print(query)
                self.cursor.execute(query)
                print(vars(self.cursor))
                info_tables.append(self.cursor)
        return info_tables

    def add_etudiant(self, etudiant):
        """ Ajouter Etudiant """
        sequence_id = self.webdb.insert('_etudiants', id=etudiant.id, \
            nom=etudiant.nom, prenom=etudiant.prenom, age=etudiant.age)
        print(sequence_id)
        return 'ok'

    def add_cours(self, cours):
        """ Ajouter Etudiant """
        sequence_id = self.webdb.insert('_cours', id=cours.id, \
            nom=cours.nom, annee=cours.annee)
        print(sequence_id)
        return 'ok'

    def add_note(self, note):
        sequence_id = self.webdb.insert('_notes', note=note.note, cours_id=note.cours_id, \
            etudiant_id=note.etudiant_id)
        print(sequence_id)
        return 'ok'

    def load_db(self):
        _etudiants = self.webdb.select('_etudiants')
        _cours = self.webdb.select('_cours')
        _notes = self.webdb.select('_notes')
        for etu in _etudiants:
            Etudiant(etu['nom'], etu['prenom'], etu['age'], etu['id'])

        for c in _cours:
            Cours(c['nom'], c['annee'], c['id'])

        for note in _notes:
            Note(note['note'], note['etudiant_id'], note['cours_id'], id_model=True)

        # Ajout de note et cours plus tard

if __name__ == "__main__":
    print('hllo')
    db = DBHandle()
    info = db.info_tables()
    print(vars(info))
