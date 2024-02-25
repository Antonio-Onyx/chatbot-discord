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
                    'que tal unos chilaquiles con carne?',
                    'mmm ... que te parece una pechuga empanizada? c:',
                    'tal vez te guste una ensalada cesar',
                    'que te parece una pizza vegetariana?',
                    'que tal unos tacos con frijoles? :D',
                    'que tal un curry de verduras?',
                    'Se me ocurre unos camarones al ajillo',
                    'que tal un ceviche?',
                    'una paella no estaria nada mal',
                    'una sopa de mariscos seria buena idea',
                    'que tal un sushi?',
                    'un ramen no estaria nada mal',
                    'pollo agridulce?',
                    'rollitos primavera?',
                    'unas fajitas de carne :p',
                    'Qué opinas de hacer unas Hamburguesas caseras?'

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
    antojo_usuario = ['vegetariano','sin carne','vegano','sin productos de origen animal']
    #recomendaciones de platillos veganos
    recom_vegana_bocchi = ['tal vez te guste una ensalada cesar',
                        'que te parece si pides una pizza vegetariana?',
                        'que tal unos tacos con frijoles? son muy vegetarianos :D',
                        'que tal un curry de verduras?'
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
    antojo_usuario = ['mariscos','mar','marisco','pescado']
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

def recomendaciones_asiaticas(user_input):
    '''
    da recomendaciones de comida dependiendo de si
    el usuario quiere algo de comida asiatica
    '''

    antojo = user_input.split()
    antojo_usuario = ['asiatica','asiático','asiática','china','japonesa']
    #recomendaciones de comida asiatica
    recom_asiatica_bocchi = ['que tal un sushi?','un ramen no estaria nada mal','pollo agridulce?', 'rollitos primavera?',]
    
    recom_definitiva = ''
    for i in antojo:
        if i in antojo_usuario:
            recom_definitiva = random.choice(recom_asiatica_bocchi)
    return recom_definitiva



def obtener_receta(user_input):
    '''Funcion que te devuelve la receta del platillo que quieres'''

    recetas_veganas = {
            'ensalada cesar vegetariana': '__**Ingredientes:**__ lechuga, crutones, aderezo César vegetariano. __**Pasos:**__ mezclar todos los ingredientes en un bol y disfrutar.',
            'pizza vegetariana': '__**Ingredientes:**__ masa de pizza, tomate, mozzarella, champiñones, pimientos. __**Pasos:**__ extender la masa, agregar los ingredientes y hornear.',
            'tacos de frijoles': '__**Ingredientes:**__ tortillas de maíz, frijoles refritos, queso, salsa. __**Pasos:**__ calentar las tortillas, agregar los frijoles y los demás ingredientes, doblar y disfrutar.',
            'curry de verduras': '__**Ingredientes:**__ verduras variadas, leche de coco, curry en polvo. __**Pasos:**__ saltear las verduras, agregar la leche de coco y el curry, cocinar a fuego lento hasta que estén tiernas.'
    }
    
    recetas_mariscos = {
            'camarones al ajillo': '__**Ingredientes:**__ camarones, ajo, aceite de oliva, perejil. __**Pasos:**__ saltear los camarones con el ajo y el aceite, espolvorear con perejil y servir.',
            'ceviche': '__**Ingredientes:**__ pescado, limón, cebolla, cilantro, chile. __**Pasos:**__ marinar el pescado en limón, agregar los demás ingredientes y servir.',
            'paella': '__**Ingredientes:**__ arroz, mariscos variados, azafrán, pimiento, guisantes. __**Pasos:**__ saltear los mariscos, agregar el arroz y el resto de los ingredientes, cocinar hasta que el arroz esté listo.',
            'sopa de mariscos': '__**Ingredientes:**__ caldo de pescado, mariscos variados, verduras, ajo. __**Pasos:**__ cocinar los mariscos en el caldo con las verduras y el ajo, servir caliente.'
    }

    recetas_carne = {
            'carnita asada': '__**Ingredientes:**__ carne de res, sal, pimienta, limón. __**Pasos:**__ sazonar la carne, asarla a la parrilla y servir con limón.',
            'chilaquiles con carne': '__**Ingredientes:**__ tortillas de maíz, salsa, carne de res, crema. __**Pasos:**__ freír las tortillas, agregar la salsa y la carne, servir con crema.',
            'pechuguita empanizada': '__**Ingredientes:**__ pechugas de pollo, huevo, pan molido. __**Pasos:**__ empanizar las pechugas, freír y servir.',
            'hamburguesas caseras': '__**Ingredientes:**__ carne molida, pan para hamburguesa, lechuga, jitomate. __**Pasos:**__ formar las hamburguesas, asarlas y servir en el pan con los demás ingredientes.',
            'fajitas de carne': '__**Ingredientes:**__ carne de res, pimientos, cebolla, tortillas de harina. __**Pasos:**__ saltear la carne con los vegetales, servir en las tortillas.'
    }

    recetas_asiaticas = {
            'sushi': '__**Ingredientes:**__ arroz, alga nori, pescado, verduras. \n__**Pasos:**__ cocinar el arroz, armar los rollos con los demás ingredientes y cortar en piezas.',
            'ramen': '__**Ingredientes:**__ fideos, caldo, carne de cerdo, huevo. __**Pasos:**__ cocinar los fideos, agregar el caldo y los demás ingredientes, servir caliente.',
            'pollo agridulce':'__**Ingredientes:**__ pollo, piña, pimiento, salsa agridulce. __**Pasos:**__ saltear el pollo con los vegetales, agregar la piña y la salsa, servir con arroz.',
            'rollitos primavera': '__**Ingredientes:**__ verduras, carne de cerdo, masa de rollitos. __**Pasos:**__ armar los rollitos con los ingredientes y freír.'
    }
    
    # Busca la receta en el diccionario
    for platillo, receta in recetas_veganas.items():
        if platillo in user_input or user_input in platillo:
            return receta
        
    for platillo, receta in recetas_mariscos.items():
        if platillo in user_input or user_input in platillo:
            return receta

    for platillo, receta in recetas_carne.items():
        if platillo in user_input or user_input in platillo:
            return receta 

    for platillo, receta in recetas_asiaticas.items():
        if platillo in user_input or user_input in platillo:
            return receta  

    return 'Ni idea de como se prepare eso, pa'
