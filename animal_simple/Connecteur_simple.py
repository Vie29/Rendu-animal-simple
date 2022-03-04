import mysql.connector as mysql

#creation de la Classe Connexion
class Connexion:
    __host = 'localhost'
    __port = '8081'
    __database = 'animal'
    __user = 'root'
    __password = 'root'

    __curseur = None

#methode de connexion a la bdd
    @classmethod
    def ouvrir_connexion(cls):
        if cls.__curseur == None :
            cls.__bdd = mysql.connect(user = cls.__user,
                                    password = cls.__password,
                                    host = cls.__host,
                                    port = cls.__port,
                                    database = cls.__database)
            cls.__curseur = cls.__bdd.cursor()

#Methode pour alimenter la page d'accueil avec la liste d'aninaux a partir de la table animal  
    @classmethod
    def lister_animaux(cls):
        cls.ouvrir_connexion()
        requete = "SELECT * FROM animal;"
        cls.__curseur.execute(requete)
        result = cls.__curseur.fetchall()

        # liste_animaux = []
        # for element in cls.__curseur :
        #     liste_animaux.append(element)

        return result
        cls.fermer_connexion()

#Methode pour alimenter la page de portrait aninal avec description animal
    @classmethod
    def decrire_animal(cls, animal_name):
        cls.ouvrir_connexion()
        requete_animal = f'''
        SELECT animal_vernaculaire, animal_taxome, animal_description, photo
        FROM animal
        WHERE idAnimal = '{animal_name}' ;
        '''
        cls.__curseur.execute(requete_animal)
        result = cls.__curseur.fetchall()

        cls.fermer_connexion() 
        return result

#Methode pour alimenter la page de portrait aninal avec description habitat
# montrer habitat
    @classmethod
    def decrire_habitat(cls, animal_name):
        cls.ouvrir_connexion()
        requete_animal_habitat = f'''
        SELECT habitat_nom, habitat_description
        FROM habitat
        JOIN animal_habitat
        ON animal_habitat.idHabitat = habitat.idHabitat
        WHERE idAnimal = '{animal_name}';
        '''
        cls.__curseur.execute(requete_animal_habitat)
        result = cls.__curseur.fetchall()

        cls.fermer_connexion() 
       
        print(f"\n=================\n {animal_name} \n==============\n ")

        return result

# méthode pour fermer la connexion à la bdd
    @classmethod
    def fermer_connexion(cls):
        cls.__curseur.close()
        cls.__bdd.close()
        cls.__curseur = None
