"""Router"""
class Router():
    """Router Class"""
    urls = (
        '/', 'controler.index.Index',
        '/add/etudiant', 'controler.etudiant.Etudiant',
        '/add/cours', 'controler.cours.Cours',
        '/profile/(.*)', 'controler.profile.Profile',
        'info/(.*)', 'controler.note.Note',
        '/suppr/(.*)', 'controler.index.Index',
        '/add/note', 'controler.index.Index'
    )
