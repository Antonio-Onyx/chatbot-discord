import os, time, string, random, re
from random import randrange

def despedida(user_input):
    '''
    Devuelve la despedida de bocchi

    :param str user_input: El texto escrito por el usuario
    :return La despedida de glados
    :rtype str
    '''
    des = user_input.split()
    despedida_usuario = ['adios', 'bye', 'hasta luego', 'adiós']
    despedida_glados = ['Bye! espero que comas algo delicioso','Regresa pronto, pero con comida, si no no regreses juajuas']
    despedida_definitiva = ''
    for i in des:
        if i in despedida_usuario:
            despedida_definitiva = random.choice(despedida_glados)
    return despedida_definitiva