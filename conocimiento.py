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
                'Hey! que onda. Soy una IA con la que puedes hablar un poco sobre comida :p'
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
        #/////////////////////////// antojo
        {
            'intent':'hambre',
            'regex':[
                r'.*tengo antojo.*',
                r'.*me gustaria.*',
                r'.*quisiera comer.*',
                r'.*se me antoja.*'
            ],
            'respuesta':[
                'pues mira, se me ocurre que tal vez te podria gustar...'
            ]
        },
        #/////////////////////////// recomendaciones
        {
            'intent':'recomendar',
            'regex':[
                r'.*recomiendame.*',
                r'.*recomiendas.*',
                r'.*tipos de comidas.*'
            ],
            'respuesta':[
                'yo te recomendaria algo que lleve carne, mariscos o algun platillo vegetariano, porque es de lo unico que tengo conocimiento xd'
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
        #///////////////////////////desconocido
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