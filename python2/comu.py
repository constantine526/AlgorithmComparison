#!/usr/bin/env python

def cree_reseau(tab_amis):
    """
    Cette fonction construit un dictionnaire représentant un réseau à partir d'un tableau.

    La fonction prend en paramètre une liste 'amis' contenant des prénoms, et retourne un dictionnaire où chaque 
    prénom est une clé, et la valeur associée est la liste des prénoms qui lui sont liés (ses amis).

    Arguments :
        amis -- tableau contenant les interactions du réseau  (list)

    Retourne :
        dict : Un dictionnaire où chaque clé est un prénom et la valeur associée est une liste de ses amis.

    Exemple:
        Si on a amis = ['Alice', 'Bob', 'Alice', 'Charlie'],
        la fonction retournera {'Alice': ['Bob', 'Charlie'], 'Bob': ['Alice'], 'Charlie': ['Alice']}
    """
    reseau = {}  # On initialise le dictionnaire
    i = 0
    while i < len(tab_amis):  
        prenom = tab_amis[i]  # La variable 'prenom' aura le prénom courant
        ami = tab_amis[i+1]   # La variable 'ami' aura le prénom d'après (donc l'ami de 'prenom')
        
        if prenom not in reseau:   # Si le prénom n'est pas une clé existante du dictionnaire
            reseau[prenom] = []   # Alors on crée cette clé, qui aura pour valeur un tableau (vide, qu'on remplira) 
            
        reseau[prenom].append(ami)  # On ajoute dans le tableau de valeur de 'prenom', l'ami
        
        if ami not in reseau:  # Si l'ami (le prénom d'après) n'est pas une clé existante du dictionnaire
            reseau[ami] = []    # Alors on l'a crée également
            
        reseau[ami].append(prenom)  # On ajoute dans le tableau de valeur de 'ami', le prenom  (car ils sont amis mutuellement)
        
        i += 2  # On s'occupera du réseau 2 par 2, donc on passe directement à la paire suivante
    return reseau



def liste_personnes(reseau):
    """
    Cette fonction retourne la liste des personnes présentes dans un réseau.

    Arguments :
        reseau -- dictionnaire représentant le réseau d'amitiés (dict)

    Retourne :
        list : Une liste contenant tous les prénoms des personnes du réseau.

    Exemple:
        Si on a reseau = {'Alice': ['Bob', 'Dan'], 'Bob': ['Alice', 'Carl', 'Dan'], 'Carl': ['Bob'], 'Dan': ['Alice', 'Bob']},
        alors liste_personnes(reseau) retournera ['Alice', 'Bob', 'Carl', 'Dan'].
    """
    return list(reseau.keys())   # Retourne toutes les clés du dictionnaire 'reseau'


def sont_amis(reseau, pers1, pers2):
    """
    Cette fonction vérifie si deux personnes sont amies dans un réseau donné.

    Arguments :
        reseau -- dictionnaire représentant le réseau d'amitiés (dict)
        pers1 -- prénom de la première personne (str)
        pers2 -- prénom de la seconde personne (str)

    Retourne :
        bool : True si les deux personnes sont amies, sinon False.

    Exemple:
        Si on a reseau = {'Alice': ['Bob', 'Dan'], 'Bob': ['Alice', 'Carl', 'Dan'], 'Carl': ['Bob'], 'Dan': ['Alice', 'Bob']},
        alors :
        - sont_amis(reseau, 'Alice', 'Bob') retournera True
        - sont_amis(reseau, 'Alice', 'Carl') retournera False
    """
    return pers1 in reseau and pers2 in reseau[pers1]  # Retourne True si pers1 est dans 'reseau' et que pers2 est dans le tableau d'amis de pers1


def sont_amis_de(pers, groupe, reseau):
    """
    Cette fonction vérifie si une personne est amie avec tous les membres d'un groupe donné.

    La fonction prend en paramètres une personne 'pers', un groupe de personnes 'groupe' et un dictionnaire 'reseau' 
    représentant le réseau d'amis. Elle retourne un booléen indiquant si chaque membre du groupe est ami avec 
    la personne 'pers'.

    Arguments :
        pers -- prénom de la personne dont on veut vérifier les amitiés (str)
        groupe -- liste de prénoms représentant le groupe à vérifier (list)
        reseau -- dictionnaire représentant le réseau d'amis (dict)

    Retourne :
        bool : True si la personne est amie avec tous les membres du groupe, sinon False.

    Exemple:
        Si on a reseau = {'Alice': ['Bob', 'Dan'], 'Bob': ['Alice'], 'Dan': ['Alice']},
        alors sont_amis_de('Alice', ['Bob', 'Dan'], reseau) retournera True,
        mais sont_amis_de('Bob', ['Alice', 'Dan'], reseau) retournera False.
    """
    if pers not in reseau:  # Vérifie si la personne (pers) existe dans le réseau
        return False
    # Vérifie que chaque membre du groupe est ami de la personne
    for membre in groupe:    # On parcourt chaque membre du groupe
        if membre not in reseau[pers]:    # Si un membre n'est pas dans la liste des amis de 'pers'
            return False     # On retourne False directement
    return True   # Sinon retourne True


def est_comu(groupe, reseau):
    """
    Cette fonction vérifie si tous les membres d'un groupe sont amis entre eux dans un réseau donné.

    La fonction prend en paramètre un groupe de personnes 'groupe' et un dictionnaire 'reseau' représentant 
    les relations d'amitié. Elle retourne un booléen indiquant si chaque membre du groupe est ami avec 
    tous les autres membres du groupe.

    Arguments :
        groupe -- liste de prénoms représentant le groupe à vérifier (list)
        reseau -- dictionnaire représentant le réseau d'amitiés (dict)

    Retourne :
        bool : True si tous les membres du groupe sont amis entre eux, sinon False.

    Exemple:
        Si on a reseau = {'Alice': ['Bob', 'Dan'], 'Bob': ['Alice', 'Carl', 'Dan'], 
                          'Carl': ['Bob'], 'Dan': ['Alice', 'Bob']},
        alors :
        - est_comu(['Alice', 'Bob', 'Dan'], reseau) retournera True
        - est_comu(['Alice', 'Bob', 'Carl'], reseau) retournera False
    """
    i = 0  # Initialise l'indice pour parcourir la liste des membres du groupe
    while i < len(groupe):
        pers = groupe[i]   # Récupère la personne actuelle
        # Vérifie que la personne est dans le réseau
        if pers not in reseau:   # Si la personne n'existe pas dans le réseau
            return False   # Retourne False directement

        j = 0     # Initialise un indice pour comparer avec les autres membres du groupe
        while j < len(groupe):
            ami = groupe[j]   # Récupère l'ami à comparer
            if ami != pers and ami not in reseau[pers]:   # Si l'ami n'est pas présent dans la liste d'amis de 'pers'
                return False     # Retourne False
            j += 1
        i += 1
    return True


def comu(groupe, reseau):
    """
    Cette fonction construit une communauté en ajoutant successivement les membres d'un groupe 
    qui sont amis avec tous les membres déjà présents dans la communauté.

    Arguments :
        groupe -- liste de prénoms représentant le groupe à analyser (list)
        reseau -- dictionnaire représentant le réseau d'amitiés (dict)

    Retourne :
        list : Une liste représentant la communauté construite.

    Exemple:
        Si on a reseau = {'Alice': ['Bob', 'Dan'], 'Bob': ['Alice', 'Carl', 'Dan'], 
                          'Carl': ['Bob'], 'Dan': ['Alice', 'Bob']},
        alors comu(['Alice', 'Bob', 'Carl', 'Dan'], reseau) retournera ['Alice', 'Bob', 'Dan'].
    """
    communaute = []  # On initialise une communauté vide
    for personne in groupe:  # Parcourt chaque membre du groupe
        if sont_amis_de(personne, communaute, reseau):  # Si la personne est amie avec toutes les personnes dans la communauté actuelle
            communaute.append(personne)  # Alors ajoute la personne à la communauté 
    return communaute


def tri_popu(groupe, reseau):
    """
    Cette fonction trie un groupe de personnes par ordre décroissant du nombre d'amis 
    qu'elles ont dans un réseau donné.

    Arguments :
        groupe -- liste de prénoms à trier (list)
        reseau -- dictionnaire représentant le réseau d'amitiés (dict)

    Retourne :
        list : Le groupe trié par ordre de popularité décroissante.

    Exemple:
        Si on a reseau = {'Alice': ['Bob', 'Dan'], 'Bob': ['Alice', 'Carl', 'Dan'], 
                          'Carl': ['Bob'], 'Dan': ['Alice', 'Bob']},
        alors tri_popu(['Alice', 'Bob', 'Carl'], reseau) retournera ['Bob', 'Alice', 'Carl']
    """
    # Tri par sélection en comparant directement les nombres d'amis des personnes
    for i in range(len(groupe)):
        maxi = i  # On initialise maxi au premier élément du groupe
        for j in range(i + 1, len(groupe)):
            if len(reseau[groupe[j]]) > len(reseau[groupe[maxi]]):   # Compare directement les longueurs des listes d'amis des différentes personnes
                maxi = j  # S'il est plus grand, j devient maxi 
        groupe[i], groupe[maxi] = groupe[maxi], groupe[i]   # Echange les positions, pour mettre maxi en tête 
    return groupe


def comu_dans_reseau(reseau):
    """
    Cette fonction construit une communauté à partir du réseau complet, en triant d'abord 
    les personnes par popularité, puis en sélectionnant les membres compatibles.

    Arguments :
        reseau -- dictionnaire représentant le réseau d'amitiés (dict)

    Retourne :
        list : Une liste représentant la communauté maximale trouvée.

    Exemple:
        Si on a reseau = {'Alice': ['Bob', 'Dan'], 'Bob': ['Alice', 'Carl', 'Dan'], 
                          'Carl': ['Bob'], 'Dan': ['Alice', 'Bob']},
        alors comu_dans_reseau(reseau) retournera ['Bob', 'Alice', 'Dan'].
    """
    membres = list(reseau.keys())   # On met la liste des personnes présentes dans le reseau dans une variable 
    trie = tri_popu(membres, reseau)  # On les trie selon leur popularité en utilisant la fonction tri_popu()
    return comu(trie, reseau)   # Retourne la communauté construite avec la fonction comu()


def comu_dans_amis(pers, reseau):
    """
    Cette fonction construit une communauté maximale à partir d'une personne donnée et 
    de ses amis, en triant les amis par popularité avant de les inclure.

    Arguments :
        pers -- prénom de la personne à analyser (str)
        reseau -- dictionnaire représentant le réseau d'amitiés (dict)

    Retourne :
        list : Une liste représentant la communauté construite.

    Exemple:
        Si on a reseau = {'Alice': ['Bob', 'Dan'], 'Bob': ['Alice', 'Carl', 'Dan'], 
                          'Carl': ['Bob'], 'Dan': ['Alice', 'Bob']},
        alors comu_dans_amis('Alice', reseau) retournera ['Alice', 'Bob', 'Dan'].
    """
    communaute = [pers]  # on initialise un tableau 'communaute' avec 'pers' pour première valeur
    if pers not in reseau:
        return communaute  # Si la personne n'est pas dans le réseau, retourne uniquement la personne
    tab_amis = reseau[pers]  # Récupère la liste des amis de la personne
    amis_trie = tri_popu(tab_amis, reseau)  # Trie les amis par popularité
    fais_comu = comu(amis_trie, reseau)  # Construit une communauté à partir des amis triés
    for ami in range(len(fais_comu)):
        communaute.append(fais_comu[ami])  # Ajoute chaque ami à la communauté
    return communaute


def comu_max(reseau):
    """
    Cette fonction détermine la plus grande communauté possible dans un réseau donné.

    Arguments :
        reseau -- dictionnaire représentant le réseau d'amitiés (dict)

    Retourne :
        list : La liste des membres de la plus grande communauté.

    Exemple:
        Si on a reseau = {'Alice': ['Bob', 'Dan'], 'Bob': ['Alice', 'Carl', 'Dan'], 
                          'Carl': ['Bob'], 'Dan': ['Alice', 'Bob']},
        alors comu_max(reseau) retournera ['Alice', 'Bob', 'Dan'].
    """
    max_comu = []  # Initialise la variable pour stocker la plus grande communauté trouvée
    tab_pers = list(reseau.keys())  # Récupère la liste de toutes les personnes du réseau
    for pers in tab_pers:   # Parcourt chaque personne du réseau
        comu_actuelle = comu_dans_amis(pers, reseau)   # Construit la communauté à partir de la personne actuelle
        if len(comu_actuelle) > len(max_comu):   # Compare la taille de la communauté actuelle avec la plus grande trouvée
            max_comu = comu_actuelle   # comu_actuelle devient max_comu si elle est plus grande 
    return max_comu