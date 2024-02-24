#----------------------------------------------------------------------
# Base de conocimiento
# La base de conocimiento representa una lista de todos los casos o intents.
#
# Cada caso o intent es un diccionario que incluye los siguientes keys (propiedades):
# - intent: Nombre para identificar el intent
# - regex: Lista de posibles expresiones regulares asociadas al intent, donde los parámetros se obtienen del texto parentizado en la expresión regular
# - respuesta: Lista de posibles respuestas al usuario, indicando los parámetros obtenidos con la notación %1, %2, %3, etc para cada parámetro
#----------------------------------------------------------------------

def conocimientoT():
    '''
    Define la base de conocimiento de bocchi

    :return El conicimiento a mostrar
    :rtype str 
    '''
    conocimiento = [
        #//////////////////////////////Bienvenida
        {
            'intent':'bienvenida',
            'regex':[
                r'.*hola.*',
                r'.*buen(a|o)s (dias|tardes|noches).',
                r'que onda'
            ],
            'respuesta':[
                'Hola! de que tienes antojo hoy? :p',
                'Hey! que onda. Soy una IA que te puede recomendar algo de comer si tú no tienes idea :D'
            ]
        },
        #////////////////////////////Fin
        {
            'intent':'terminar',
            'regex':[
                r'.*adios.*',r'.*bye.*',r'.*hasta luego.*'
            ],
            'respuesta':[
                ''
            ]
        },
        #/////////////////////////// intent por si el usuario no tiene claro qué comer y quiere algo al azar
        {
            'intent':'hambre_indeciso',
            'regex':[
                r'.*(ni idea|tengo idea).*(comida|comer).*',
                r'.*no se me ocurre.*(comer|comida).*',
                r'.*estoy indeciso.*(comer|comida).*',
                r'.*no s(e|é).*(comer|comida)',
                r'.*no s(e|é).*(elige|escoge).*'
            ],
            'respuesta':[
                'dejame pensar en algo rico pa hacer...'
            ]
        },
        #/////////////////////////// recomendaciones
        {
            'intent':'recomendar',
            'regex':[
                r'.*recomiendame.*',
                r'.*recomiendas.*',
                r'.*recomendar.*',
                r'.*tipos de comidas.*',
                r'.*qu(e|é) me.*(recomiendas|recomendar|recomendarias)'
            ],
            'respuesta':[
                'pues se me ocurren algunas cosas que podrian llevar carne, mariscos o algun platillo vegetariano, porque es de lo único que sé preparar xd'
            ]
        },
        #///////////////////////////recetas
        {
            'intent':'recetas',
            'regex':[
                r'.*quiero la receta de (.*)',
                r'.*c(ó|o)mo se hace (.*)',
                r'.*receta de (.*)',
                r'.*c(ó|o)mo preparar (.*)',
                r'.*c(ó|o)mo hago (.*)'
            ],
            'respuesta':[                   
                'si mi memoria no me falla, la receta de %1 seria...'
            ]
        },
        ########### por si queremos que nos de otra opcion de comida
        {
            'intent': 'repetir',
            'regex': [
                r'.*(dime|no me gusta|dame|sabes).*(otr(a|o)).*',
                r'.*no me gusta.*'
            ],
            'respuesta': [
                'ok, dejame pensarrrr... '
            ]
        },
        ########### intent para recomendar tipos de comida ################

        ########## Agregar un nuevo intent para hablar sobre comida vegetariana ###################
        {
            'intent': 'vegetariana',
            'regex': [
                r'.*comida vegetariana.*',
                r'.*comida sin carne.*'
            ],
            'respuesta': [
                ''
            ]
        },
        ############ Agregar un nuevo intent para solicitar la receta de comida vegetariana #############
        {
            'intent': 'receta_vegetariana',
            'regex': [
                r'(.*)quiero la receta de (.*)',
                r'(.*)cómo se hace (.*)',
                r'.*receta de (.*)',
                r'.*cómo preparar (.*)',
                r'.*cómo hago (.*)'
            ],
            'respuesta': [
                'Aquí tienes la receta de %1: '
            ]
        },
        ############# Agregar un nuevo intent para comida mariscos #############
        {
            'intent': 'mariscos',
            'regex': [
                r'.*mariscos.*',
                r'.*comida de mar.*'
            ],
            'respuesta': [
                ''
            ]
        },  
        ########### Agregar un nuevo intent para solicitar la receta de comida de mar #############
        {
            'intent': 'receta_mariscos',
            'regex': [
                r'(.*)quiero la receta de (.*)',
                r'(.*)cómo se hace (.*)',
                r'.*receta de (.*)',
                r'.*cómo preparar (.*)',
                r'.*cómo hago (.*)'
            ],
            'respuesta': [
                'Aquí tienes la receta de %1: '
            ]
        },
        ########## recomendaciones especificas para comida que lleve carne
        {
            'intent': 'carne',
            'regex': [
                r'.*carne.*',
                r'.*carnoso.*',
                r'.*carnivoro.*'
            ],
            'respuesta': [
                ''
            ]
        },


        #////////////////////desconocido
        {
            'intent':'desconocido',
            'regex':[
                r'.*'
            ],
            'respuesta':[
                'eso se come? xd',
                'https://tenor.com/view/giga-gigacat-cat-mewing-mogging-gif-12429734670640119345'
            ]
        }
    ]
    return conocimiento