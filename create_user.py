import os
import getopt
import sys
import hashlib



def creer_usager(nom_usager, mot_de_passe):
    # Création d'un salt unique pour le nouveau usager
    salt = os.urandom(32)
    # Hashage du mot de passe
    mot_de_passe_hash = hashlib.pbkdf2_hmac('sha256',mot_de_passe.encode('utf-8'),salt, 100000, dklen=128)

    # Insertion des informations dans la table usager de la base de données
    # colonne : valeur
    # nom_usager : nom_usager
    # mot_de_passe : mot_de_passe_hash
    # salt : salt


    # Afficher message de confirmation



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