#import de la bibliotheque
from cgitb import html
from flask import Flask, render_template
from Connecteur_simple import Connexion

#appel du constructeur de flask pour l'appli
app = Flask(__name__)

#page d'accueil, le / appelle le nom de domaine
@app.route('/')
def index() :
    liste = Connexion.lister_animaux()
    html = render_template('base.html') + '''
    <H1>Bienvenue sur la liste des animaux!</H1>
    <p></p>
    <h2>Description</h2><ul>'''
    for item in liste:
        animal_name = item[2]
        id_animal = item[0]
        html += f'''
        <li> <a href = "/fiche_animal/{id_animal}">{animal_name}</a></li>
        '''
    html += '</ul>'
    return html

# page pour visualiser les portraits des animaux
@app.route('/fiche_animal/<animal_fiche>')
def voir_animal(animal_fiche):
    liste_decrire_animal = Connexion.decrire_animal(animal_fiche)
    liste_decrire_habitat = Connexion.decrire_habitat(animal_fiche)
    photo = liste_decrire_animal[0][-1]
    html = render_template('base.html') + f'''
    <H1>Portrait de l'animal que vous avez choisi</H1>
    <p>{liste_decrire_animal}</p>
    <p>{liste_decrire_habitat}</p>
    <button> <a href="/">Retour à l'Accueil</a></button>
    <img src="\static\{photo}">;
    '''
    return html
    
if __name__ == "__main__":
    app.run(debug=True)

#lien pour retourner au menu index
#<li> <a href = "/">Retour à l'Accueil</a></li>
   