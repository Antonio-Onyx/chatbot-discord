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
                'Hola! soy una IA que te puede dar recomendaciones de comida Yummi! ^_^',
                'Hey! que onda. Soy una IA que te puede recomendar algo de comer si tú no tienes idea  Yey! ^_^'
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
                r'.*no s(e|é) me ocurre.*(comer|comida).*',
                r'.*estoy indeciso.*(comer|comida).*',
                r'.*no s(e|é).*(comer|comida)',
                r'.*no s(e|é) que.*',
                r'.*no s(e|é).*(elige|escoge).*'
            ],
            'respuesta':[
                ''
            ]
        },
        #/////////////////////////// recomendaciones
        {
            'intent':'recomendar',
            'regex':[
                
                r'.*recomiendas.*',
                r'.*recomendar.*',
                r'.*alguna sugerencia.*',
                r'.*tipos de comidas.*',
                
                r'.*qu(e|é) me.*(recomiendas|recomendar|recomendar(i|í)as)',
                r'.*recomi(e|é)ndame.*',
                r'.*recomendaci(o|ó)n.*',


            ],
            'respuesta':[
                'pues se me ocurren algunas cosas que podrian llevar carne, comida asiatica, mariscos o algun platillo vegetariano, porque es de lo único que sé preparar xd'
            ]
        },
        #///////////////////////////recetas
        {
            'intent':'recetas',
            'regex':[
                r'.*quiero la receta de (.*)',
                r'.*como se hace (.*)',
                r'.*receta de (.*)',
                r'.*como preparar (.*)',
                r'.*me interesa saber cómo se hace (.*)',
                r'.*dime como se hace (.*)',
                r'.*¿podrias darmela receta de (.*)?',
                r'.*se me antoja un(.*)',
                r'.*muestrame la receta(.*)',
                r'.*como hago (.*)',
                r'.*como preparo.* (.*)'
            ],
            'respuesta':[                   
                'si mi memoria no me falla, la receta de %1 seria...',
                'Mira, esto es lo que necesitas para hacer %1'
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
                ''
            ]
        },
        ########### intent para recomendar tipos de comida ################

        ########## Agregar un nuevo intent para hablar sobre comida vegetariana ###################
        {
            'intent': 'vegetariana',
            'regex': [
                r'.*comida vegetariana.*',
                r'.*recomiendame algo que no lleve carne.*',
                r'.*recomiendame algo que sea vegetariano*',
                r'.*comida sin carne.*'
            ],
            'respuesta': [
                ''
            ]
        },
        
        ############# Agregar un nuevo intent para comida mariscos #############
        {
            'intent': 'mariscos',
            'regex': [
                r'.*mariscos.*',
                r'.*recomiendame algo que lleve marisco*',
                r'.*recomiendame algo que sea de mar*',
                r'.*con pescado*',
                r'.*de pescado*',
                r'.*lleve pescado*',
                r'.*comida de mar*'
            ],
            'respuesta': [
                ''
            ]
        },  
        
        ########## recomendaciones especificas para comida que lleve carne
        {
            'intent': 'carne',
            'regex': [
                r'.*carne.*',
                r'.*carnoso.*',
                r'.*recomiendame algo que lleve carne.*',
                r'.*carnivoro.*'
            ],
            'respuesta': [
                ''
            ]
        },

        ########## Agregar un nuevo intent para solicitar comida asiatica #############
        {
            'intent': 'asiatica',
            'regex': [
                r'.*comida asiatica.*',
                r'.*recomiendame algo asiatico.*',
                r'.*comida de asia.*'
            ],
            'respuesta': [
                ''
            ]
        },
        #////////////////////aceptacion
        {
            'intent':'aceptacion',
            'regex':[
                r'.*va.*',
                r'.*eso me gusta.*',
                r'.*me parece bien.*',
                r'.*suena rico.*',
                r'.*eso suena bien.*'
            ],
            'respuesta':[
                'genial, tambien de podria dar la receta si gustas preparalo :)',
                'Perfecto! Si quieres, también puedo proporcionarte la receta para que puedas prepararlo tú mismo. :)',
                '¡Fantástico! Si estás interesado, incluso puedo compartir contigo la receta ;)'
            ]
        },
        #////////////////////desconocido
        {
            'intent':'desconocido',
            'regex':[
                r'.*'
            ],
            'respuesta':[
                'perdona pero no he entendido eso'
            ]
        }
    ]
    return conocimiento