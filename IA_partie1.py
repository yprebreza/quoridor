"""
Le but de ce code est d'implémenter deux fonctions (makeMove et endGGame) qui permettrons de faire fonctionner la première
partie du projet de l'année. Ce fichier sera importer dans le fichier principal.

Nom : Prebreza
Prénom : Yllke
Matricule : 000475617
"""
from random import *

def makeMove(M, last, strategy, eps, alpha):  # choise of the move following e-greedy
    # last = [s,p]
    eps = float(input())  # float number between 0 and 1
    r = random()
    estim_of_proba = []
    list_afterstates = []

    if r >= eps:
        for i in range(len(M)):
            if M[i][1] > estim_of_proba:
                proba_to_win = M[i][1]
                move = M[i][0]  # M[i][0] gives the afterstate
            estim_of_proba.append(M[i][1])
            list_afterstates.append(M[i][0])

    if r < eps:
        sample(M, 1)  # chose a random list [s,p] in M

    if strategy == 'TD(0)':
        M[i - 1][1] = (1 - alpha) * M[i - 1][1] + alpha * M[i][1]

    if strategy == 'Q-learning':
        M[i - 1][1] = (1 - alpha) * M[i - 1][1] + alpha * M[i][1]

    return move


def endGame(won, history, strategy, alpha):
    # history, strategy and alpha are defined in main_partie1

    for i in range(len(M)):
        history = history.append(M[i][1])

        if strategy == 'TD(0)' or 'Q-learning':
            M[i - 1][1] = (1 - alpha) * M[i - 1][1] + alpha * r

    return (None)