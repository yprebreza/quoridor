"""
Ce programme, à condition d'être correctement réalisé, permet d'implémenter une IA qui s'entraine à atteindre un haut
niveau de propabilité de gagner grâce au learning strategies. Pour s'entrainer  elle jouera contre l'IA fournie sur l'UV.

(NB : Pour le moment j'ai encore des difficultés en programmation et je travaille pour y remédier en suivant des cours
en ligne, mais pour l'instant je m'en sort pas avec les projets, je suis désolée du niveau de ce travail,
je ferai mieux pour le reste du projet de l'année.)

Nom : Prebreza
Prénom : Yllke
Matricule : 000475617
"""
import random
import numpy as np

def makeMove(moves, s, color, NN, eps, learning_strategy = None): #return new_s
    pass

def endGame(s, won, NN, learning_strategy): #return None
    pass

def sigmoid(x):
    p =  1/(1 + np.exp(-x))
    return p

def createNN(n_input, n_hidden): #creates a network of neurons
    W_int = np.shape((n_hidden),(n_input))
    W_out = np.shape((n_hidden),1)
    NN = (W_int,W_out)
    return NN

def forwardPass(s, NN): #return p_out
    pass

def backpropagation(s, NN, delta, learning_strategy = None):
    pass