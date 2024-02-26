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
    despedida_glados = ['Bye! espero que comas algo delicioso -‿-','Regresa pronto, pero con comida, si no no regreses juajuas -‿-']
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
    recom_comida_bocchi = ['no estaria mal que preparas una carnita asada ᕙ(`▿´)ᕗ',
                    'que tal unos chilaquiles con carne? ᕙ(`▿´)ᕗ',
                    'mmm ... que te parece una pechuga empanizada? ^_^',
                    'tal vez te guste una ensalada cesar ｡◕‿◕｡',
                    'que te parece una pizza vegetariana?',
                    'que tal unos tacos con frijoles? ^_^',
                    'que tal un curry de verduras? :o',
                    'Se me ocurre unos camarones al ajillo',
                    'que tal un ceviche? :)',
                    'una paella no estaria nada mal',
                    'una sopa de mariscos seria buena idea',
                    'que tal un sushi? ;)',
                    'un ramen no estaria nada mal ;)',
                    'pollo agridulce? (ㆆ_ㆆ)',
                    'rollitos primavera?',
                    'unas fajitas de carne :p',
                    'Qué opinas de hacer unas Hamburguesas caseras? ( ͡° ͜ʖ ͡°)'

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
    #recomendaciones de platillos veganos
    recom_vegana_bocchi = ['tal vez te guste una ensalada cesar',
                        'que te parece si pides una pizza vegetariana?',
                        'que tal unos tacos con frijoles? son muy vegetarianos :D',
                        'que tal un curry de verduras?'
    ]

    return random.choice(recom_vegana_bocchi)

def recomendaciones_mariscos(user_input):
    '''
    da recomendaciones de comida dependiendo de si
    el usuario quiere algo de mariscos
    '''

    antojo = user_input.split()
    #recomendaciones de mariscos
    recom_mariscos_bocchi = [
                            'Se me ocurre unos camarones al ajillo',
                            'que tal un ceviche?',
                            'una paella no estaria nada mal',
                            'una sopa de mariscos seria buena idea'
    ]
    
    return random.choice(recom_mariscos_bocchi)

def recomendaciones_asiaticas(user_input):
    '''
    da recomendaciones de comida dependiendo de si
    el usuario quiere algo de comida asiatica
    '''

    antojo = user_input.split()
    #recomendaciones de comida asiatica
    recom_asiatica_bocchi = ['que tal un sushi?',
                             'un ramen no estaria nada mal',
                             'pollo agridulce?', 
                             'rollitos primavera?',]
    
    return random.choice(recom_asiatica_bocchi)



def obtener_receta(user_input):
    '''Funcion que te devuelve la receta del platillo que quieres'''

    recetas_veganas = {
            'ensalada cesar vegetariana': '__**Ingredientes:**__ lechuga, crutones, aderezo César vegetariano. \n__**Pasos:**__ mezclar todos los ingredientes en un bol y disfrutar.',
            'pizza vegetariana': '__**Ingredientes:**__ masa de pizza, tomate, mozzarella, champiñones, pimientos. \n__**Pasos:**__ extender la masa, agregar los ingredientes y hornear.',
            'tacos de frijoles': '__**Ingredientes:**__ tortillas de maíz, frijoles refritos, queso, salsa. \n__**Pasos:**__ calentar las tortillas, agregar los frijoles y los demás ingredientes, doblar y disfrutar.',
            'curry de verduras': '__**Ingredientes:**__ verduras variadas, leche de coco, curry en polvo. \n__**Pasos:**__ saltear las verduras, agregar la leche de coco y el curry, cocinar a fuego lento hasta que estén tiernas.'
    }
    
    recetas_mariscos = {
            'camarones al ajillo': '__**Ingredientes:**__ camarones, ajo, aceite de oliva, perejil. \n__**Pasos:**__ saltear los camarones con el ajo y el aceite, espolvorear con perejil y servir.',
            'ceviche': '__**Ingredientes:**__ pescado, limón, cebolla, cilantro, chile. \n__**Pasos:**__ marinar el pescado en limón, agregar los demás ingredientes y servir.',
            'paella': '__**Ingredientes:**__ arroz, mariscos variados, azafrán, pimiento, guisantes. \n__**Pasos:**__ saltear los mariscos, agregar el arroz y el resto de los ingredientes, cocinar hasta que el arroz esté listo.',
            'sopa de mariscos': '__**Ingredientes:**__ caldo de pescado, mariscos variados, verduras, ajo. \n__**Pasos:**__ cocinar los mariscos en el caldo con las verduras y el ajo, servir caliente.'
    }

    recetas_carne = {
            'carnita asada': '__**Ingredientes:**__ carne de res, sal, pimienta, limón. \n__**Pasos:**__ sazonar la carne, asarla a la parrilla y servir con limón.',
            'chilaquiles con carne': '__**Ingredientes:**__ tortillas de maíz, salsa, carne de res, crema. \n__**Pasos:**__ freír las tortillas, agregar la salsa y la carne, servir con crema.',
            'pechuga empanizada': '__**Ingredientes:**__ pechugas de pollo, huevo, pan molido. \n__**Pasos:**__ empanizar las pechugas, freír y servir.',
            'hamburguesas caseras': '__**Ingredientes:**__ carne molida, pan para hamburguesa, lechuga, jitomate. \n__**Pasos:**__ formar las hamburguesas, asarlas y servir en el pan con los demás ingredientes.',
            'fajitas de carne': '__**Ingredientes:**__ carne de res, pimientos, cebolla, tortillas de harina. \n__**Pasos:**__ saltear la carne con los vegetales, servir en las tortillas.'
    }

    recetas_asiaticas = {
            'sushi': '__**Ingredientes:**__ arroz, alga nori, pescado, verduras. \n__**Pasos:**__ cocinar el arroz, armar los rollos con los demás ingredientes y cortar en piezas.',
            'ramen': '__**Ingredientes:**__ fideos, caldo, carne de cerdo, huevo. \n__**Pasos:**__ cocinar los fideos, agregar el caldo y los demás ingredientes, servir caliente.',
            'pollo agridulce':'__**Ingredientes:**__ pollo, piña, pimiento, salsa agridulce. \n__**Pasos:**__ saltear el pollo con los vegetales, agregar la piña y la salsa, servir con arroz.',
            'rollitos primavera': '__**Ingredientes:**__ verduras, carne de cerdo, masa de rollitos. \n__**Pasos:**__ armar los rollitos con los ingredientes y freír.'
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

def obtener_infoNutricional(user_input):
    '''Funcion que te devuelve la informacion nutricional del platillo que quieres'''

    infoNutricional_veganas = {
            'ensalada cesar vegetariana': 'La ensalada cesar vegetariana es baja en calorías y grasas, pero rica en fibra y vitaminas. Es una opción saludable y deliciosa para cualquier comida.',
            'pizza vegetariana': 'La pizza vegetariana es una opción baja en calorías y grasas, pero rica en fibra y vitaminas. Es una opción saludable y deliciosa para cualquier comida.',
            'tacos de frijoles': 'Los tacos de frijoles son una opción baja en calorías y grasas, pero rica en fibra y proteínas. Son una opción saludable y deliciosa para cualquier comida.',
            'curry de verduras': 'El curry de verduras es una opción baja en calorías y grasas, pero rica en fibra y vitaminas. Es una opción saludable y deliciosa para cualquier comida.'
    }
    
    infoNutricional_mariscos = {
            'camarones al ajillo': 'Los camarones al ajillo son una opción baja en calorías y grasas, pero rica en proteínas y omega-3. Son una opción saludable y deliciosa para cualquier comida.',
            'ceviche': 'El ceviche es una opción baja en calorías y grasas, pero rica en proteínas y omega-3. Es una opción saludable y deliciosa para cualquier comida.',
            'paella': 'La paella es una opción baja en calorías y grasas, pero rica en proteínas y omega-3. Es una opción saludable y deliciosa para cualquier comida.',
            'sopa de mariscos': 'La sopa de mariscos es una opción baja en calorías y grasas, pero rica en proteínas y omega-3. Es una opción saludable y deliciosa para cualquier comida.'
    }

    infoNutricional_carne = {
            'carnita asada': 'La carnita asada es una opción baja en calorías y grasas, pero rica en proteínas y hierro. Es una opción saludable y deliciosa para cualquier comida.',
            'chilaquiles con carne': 'Los chilaquiles con carne son una opción baja en calorías y grasas, pero rica en proteínas y hierro. Son una opción saludable y deliciosa para cualquier comida.',        
            'pechuga empanizada': 'La pechuga empanizada es una opción baja en calorías y grasas, pero rica en proteínas y hierro. Es una opción saludable y deliciosa para cualquier comida.',
            'hamburguesas caseras': 'Las hamburguesas caseras son una opción baja en calorías y grasas, pero rica en proteínas y hierro. Son una opción saludable y deliciosa para cualquier comida.',
            'fajitas de carne': 'Las fajitas de carne son una opción baja en calorías y grasas, pero rica en proteínas y hierro. Son una opción saludable y deliciosa para cualquier comida.'
    }

    infoNutricional_asiaticas = {
            'sushi': 'El sushi es una opción baja en calorías y grasas, pero rica en proteínas y omega-3. Es una opción saludable y deliciosa para cualquier comida.',
            'ramen': 'El ramen es una opción baja en calorías y grasas, pero rica en proteínas y omega-3. Es una opción saludable y deliciosa para cualquier comida.',
            'pollo agridulce': 'El pollo agridulce es una opción baja en calorías y grasas, pero rica en proteínas y omega-3. Es una opción saludable y deliciosa para cualquier comida.',
            'rollitos primavera': 'Los rollitos primavera son una opción baja en calorías y grasas, pero rica en proteínas y omega-3. Son una opción saludable y deliciosa para cualquier comida.'
    }

    # Busca la info nutricional en el diccionario
    for platillo, info in infoNutricional_veganas.items():
        if platillo in user_input or user_input in platillo:
            return info
        
    for platillo, info in infoNutricional_mariscos.items():
        if platillo in user_input or user_input in platillo:
            return info
        
    for platillo, info in infoNutricional_carne.items():
        if platillo in user_input or user_input in platillo:
            return info
        
    for platillo, info in infoNutricional_asiaticas.items():
        if platillo in user_input or user_input in platillo:
            return info
        
    return 'la verdad eso si no lo se, no soy nutriologa'


