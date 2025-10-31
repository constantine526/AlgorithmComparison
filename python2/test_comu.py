#!/usr/bin/env python

import comu as c

tab = ["Alice", "Bob", "Alice", "Dan", "Bob", "Carl", "Dan", "Bob"]
reseau = {'Alice': ['Bob', 'Dan'], 'Bob': ['Alice', 'Carl', 'Dan'], 'Carl': ['Bob'], 'Dan': ['Alice', 'Bob']}

def test_cree_reseau():
    assert c.cree_reseau([]) == {}
    assert c.cree_reseau(tab) == {'Alice': ['Bob', 'Dan'], 'Bob': ['Alice', 'Carl', 'Dan'], 'Dan': ['Alice', 'Bob'], 'Carl': ['Bob']}
    assert c.cree_reseau(['Alice', 'Bob']) == {'Alice': ['Bob'], 'Bob': ['Alice']}
    assert c.cree_reseau(['Alice', 'Bob', 'Alice', 'Bob']) == {'Alice': ['Bob', 'Bob'], 'Bob': ['Alice', 'Alice']}  # Test avec des doublons
    print("test cree_reseau ok")

def test_liste_personnes():
    assert c.liste_personnes(reseau) == ['Alice', 'Bob', 'Carl', 'Dan']
    assert c.liste_personnes({'Alice': ['Bob'], 'Bob': ['Alice']}) == ['Alice', 'Bob']
    assert c.liste_personnes({}) == []   # Si le dictionnaire est vide
    print("test liste_personnes ok")

def test_sont_amis():
    assert c.sont_amis(reseau, 'Alice', 'Bob')
    assert not c.sont_amis(reseau, 'Alice', 'Carl')
    assert not c.sont_amis(reseau, 'Camille', 'Bob')  # Avec une personne non présente dans le réseau
    assert not c.sont_amis(reseau, 'Bob', 'Camille')  # Test dans les 2 sens
    print("test sont_amis ok")

def test_sont_amis_de():
    assert c.sont_amis_de('Alice', ['Bob', 'Dan'], reseau)
    assert not c.sont_amis_de('Alice', ['Bob', 'Carl'], reseau)
    assert not c.sont_amis_de('Camille', ['Bob', 'Dan'], reseau)  # Si la personne n'est pas présente dans le réseau
    print("test sont_amis_de ok")

def test_est_comu():
    assert c.est_comu(['Alice', 'Bob', 'Dan'], reseau)
    assert not c.est_comu(['Alice', 'Bob', 'Carl'], reseau)
    assert not c.est_comu(['Alice', 'Camille'], reseau)
    assert c.est_comu([], reseau)  # Un groupe vide est considéré comme True
    print("test est_comu ok")

def test_comu():
    assert c.comu(['Alice', 'Bob', 'Carl', 'Dan'], reseau) == ['Alice', 'Bob', 'Dan']
    assert c.comu(['Carl', 'Dan'], reseau) == ['Carl']
    assert c.comu(['Camille', 'Bob'], reseau) == ['Bob']  # Avec une personne non présente dans le réseau
    assert c.comu(['Bob', 'Camille'], reseau) == ['Bob'] 
    assert c.comu(['Alice'], reseau) == ['Alice']  # Si la liste contient une seule personne, la communauté est juste la personne
    assert c.comu([], reseau) == []    # Si la liste est vide, la communauté est vide
    print("test comu ok")

def test_tri_popu():
    assert c.tri_popu(['Alice', 'Bob', 'Carl'], reseau) == ['Bob', 'Alice', 'Carl']
    assert c.tri_popu(['Dan', 'Alice'], reseau) == ['Dan', 'Alice']   # Test en cas d'égalité il prend le premier dans la liste
    assert c.tri_popu(['Alice', 'Dan'], reseau) == ['Alice', 'Dan']
    assert c.tri_popu(['Alice', 'Bob', 'Carl', 'Bob'], reseau) == ['Bob', 'Bob', 'Alice', 'Carl']   # Test dans le cas d'un prénom en doublon dans le tableau
    assert c.tri_popu(['Dan'], reseau) == ['Dan']  # Test avec un seul élément
    assert c.tri_popu([], reseau) == []  # Test avec un groupe vide
    print("test tri_popu ok")

def test_comu_dans_reseau():
    assert c.comu_dans_reseau(reseau) == ['Bob', 'Alice', 'Dan']
    assert c.comu_dans_reseau({'Camille': []}) == ['Camille']  # Test avec une seule personne sans amis
    assert c.comu_dans_reseau({'Alice': ['Bob'], 'Bob': ['Alice'], 'Dan': []}) == ['Alice', 'Bob']  # Test avec une personne sans amis
    assert c.comu_dans_reseau({}) == []
    print("test comu_dans_reseau ok")

def test_comu_dans_amis():
    assert c.comu_dans_amis('Alice', reseau) == ['Alice', 'Bob', 'Dan']
    assert c.comu_dans_amis('Carl', reseau) == ['Carl', 'Bob']
    assert c.comu_dans_amis('Camille', reseau) == ['Camille']
    assert c.comu_dans_amis('Dan', {}) == ['Dan']  # Test dans un réseau vide
    assert c.comu_dans_amis('Alice', {'Alice': []}) == ['Alice']  # Test avec une personne sans amis
    print("test comu_dans_amis ok")

def test_comu_max():
    assert c.comu_max(reseau) == ['Alice', 'Bob', 'Dan']
    assert c.comu_max({'Alice': []}) == ['Alice']  # Test avec une seule personne
    assert c.comu_max({}) == []  # Test du cas vide
    print("test comu_max ok")


test_cree_reseau()
test_liste_personnes()
test_sont_amis()
test_sont_amis_de()
test_est_comu()
test_comu()
test_tri_popu()
test_comu_dans_reseau()
test_comu_dans_amis()
test_comu_max()