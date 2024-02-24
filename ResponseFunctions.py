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

def recomendaciones_azar():
    '''
    da recomendaciones de comida al azar
    '''
    #recomendaciones de platillos que lleven carne
    recom_comida_bocchi = ['no estaria mal que preparas una carnita asada',
                    'que tal unos chilaquiles con un filete de carne roja? UwU',
                    'mmm ... que te parece una pechuguita empanizada con sus papitas?c:',
                    'tal vez te guste una ensalada cesar',
                    'que te parece si pides una pizza? para algo rapido xd',
                    'que tal unos tacos con frijoles? :D',
                    'que tal un curry de verduras?',
                    'porque no pruebas algo que lleve leguminosas, son un buen alimento', 
                    'Se me ocurre unos camarones al ajillo',
                    'que tal un ceviche?',
                    'una paella no estaria nada mal',
                    'una sopa de mariscos seria buena idea'
    ]
    
    return random.choice(recom_comida_bocchi)


def recomendaciones_carne(user_input):
    '''
    da recomendaciones de comida dependiendo de si
    el usuario quiere algo que lleve carne
    '''
    #recomendaciones de platillos con carne
    recom_carne_bocchi = ['no estaria mal que preparas una carnita asada',
                        'que tal unos chilaquiles con un filete de carne roja? UwU',
                        'mmm ... que te parece una pechuguita empanizada con sus papitas? c:',
                        'Qué opinas de hacer unas Hamburguesas caseras?',
                        'Bro, se me ocurre que unas fajitas con tiras de carne, pimientos y cebollas bien sazonadas serían una buena ídea :p']
    
    return random.choice(recom_carne_bocchi)

def recomendaciones_veganas(user_input):
    '''
    da recomendaciones de comida dependiendo de si
    el usuario quiere algo que sea vegano
    '''

    antojo = user_input.split()
    antojo_usuario = ['vegetariano','sin carne','vegano']
    #recomendaciones de platillos veganos
    recom_vegana_bocchi = ['tal vez te guste una ensalada cesar',
                        'que te parece si pides una pizza vegetariana?',
                        'que tal unos tacos con frijoles? son muy vegetarianos :D',
                        'que tal un curry de verduras?',
                        'porque no pruebas algo que lleve leguminosas, son un buen alimento',
    ]
    
    recom_definitiva = ''
    for i in antojo:
        if i in antojo_usuario:
            recom_definitiva = random.choice(recom_vegana_bocchi)
    return recom_definitiva

def recomendaciones_mariscos(user_input):
    '''
    da recomendaciones de comida dependiendo de si
    el usuario quiere algo de mariscos
    '''

    antojo = user_input.split()
    antojo_usuario = ['mariscos','mar']
    #recomendaciones de mariscos
    recom_mariscos_bocchi = [
                            'Se me ocurre unos camarones al ajillo',
                            'que tal un ceviche?',
                            'una paella no estaria nada mal',
                            'una sopa de mariscos seria buena idea'
    ]
    
    recom_definitiva = ''
    for i in antojo:
        if i in antojo_usuario:
            recom_definitiva = random.choice(recom_mariscos_bocchi)
    return recom_definitiva

def obtener_receta(user_input):
    '''Funcion que te devuelve la receta del platillo que quieres'''

    recetas_veganas = {
            'ensalada cesar vegetariana': 'Ingredientes: lechuga, crutones, aderezo César vegetariano. Pasos: mezclar todos los ingredientes en un bol y disfrutar.',
            'pizza vegetariana': 'Ingredientes: masa de pizza, tomate, mozzarella, champiñones, pimientos. Pasos: extender la masa, agregar los ingredientes y hornear.',
            'tacos de frijoles': 'Ingredientes: tortillas de maíz, frijoles refritos, queso, salsa. Pasos: calentar las tortillas, agregar los frijoles y los demás ingredientes, doblar y disfrutar.',
            'curry de verduras': 'Ingredientes: verduras variadas, leche de coco, curry en polvo. Pasos: saltear las verduras, agregar la leche de coco y el curry, cocinar a fuego lento hasta que estén tiernas.'
        }
    
    recetas_mariscos = {
            'camarones al ajillo': 'Ingredientes: camarones, ajo, aceite de oliva, perejil. Pasos: saltear los camarones con el ajo y el aceite, espolvorear con perejil y servir.',
            'ceviche': 'Ingredientes: pescado, limón, cebolla, cilantro, chile. Pasos: marinar el pescado en limón, agregar los demás ingredientes y servir.',
            'paella': 'Ingredientes: arroz, mariscos variados, azafrán, pimiento, guisantes. Pasos: saltear los mariscos, agregar el arroz y el resto de los ingredientes, cocinar hasta que el arroz esté listo.',
            'sopa de mariscos': 'Ingredientes: caldo de pescado, mariscos variados, verduras, ajo. Pasos: cocinar los mariscos en el caldo con las verduras y el ajo, servir caliente.'
    }
    
    # Busca la receta en el diccionario
    for platillo, receta in recetas_veganas.items():
        if platillo in user_input or user_input in platillo:
            return receta
        
    for platillo, receta in recetas_mariscos.items():
        if platillo in user_input or user_input in platillo:
            return receta
        
    return 'Ni idea de como se prepare eso, pa'
