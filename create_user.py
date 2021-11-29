import getopt
import sys
# Importez la librairie bcrypt pour la gestion du mot de passe
# https://pypi.org/project/bcrypt/
import bcrypt


def creer_usager(nom_usager, mot_de_passe):
    # Création d'un salt unique pour le nouveau usager
    salt = bcrypt.gensalt()
    
    # Hashage du mot de passe
    mot_de_passe_hash = bcrypt.hashpw(mot_de_passe.encode('utf8'), salt)

    # Insertion des informations dans la table usager de la base de données
    # colonne : valeur
    # nom_usager : nom_usager
    # mot_de_passe : mot_de_passe_hash
    # salt : salt


    # Afficher message de confirmation
    print(salt)
    print(mot_de_passe_hash)


def valider_nom_usager(nom_usager):
    # Valide que le nom d'usager n'existe pas déjà dans la bd
    
    return True


def main(argv):
    """
        Procédure principale
    """

    nom_usager = ''
    mot_de_passe = ''

    try:
        opts, _ = getopt.getopt(argv,"u:p:")
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-u':
            nom_usager = arg
        elif opt == '-p':
            mot_de_passe = arg

    # Pour le debug, à supprimer
    print(f'Le nom d\'usager est : "{nom_usager}"')
    print(f'Le mot de passe est : "{mot_de_passe}"')

    if(valider_nom_usager(nom_usager)):
        creer_usager(nom_usager, mot_de_passe)



if __name__ == "__main__":
    main(sys.argv[1:])