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

def recomendaciones(user_input):
    '''
    da recomendaciones de comida dependiendo de que tenga antojo el usuario
    '''
    antojo = user_input.split()
    antojo_usuario = ['carne']
    recom_bocchi = ['no estaria mal que preparas una carnita asada',
                    'que tal unos chilaquiles con bistek? xd',
                    'mmm que te parece una pechuguita empanizada con sus papitas? uwu',
                    'que tal una hamburguesa?',
                    'que tal pasta con carne?',
                    'unas empanadas de carne?';
                    'unos tacos?']
    recom_definitiva = ''
    for i in antojo:
        if i in antojo_usuario:
            recom_definitiva = random.choice(recom_bocchi)
    return recom_definitiva