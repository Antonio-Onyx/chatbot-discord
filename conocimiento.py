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
                r'.*quiero saber como se hace (.*)',
                r'.*quiero hacer (.*)',
                r'.*quiero cocinar (.*)',
                r'.*receta.*',
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
                r'.*comida (vegetariana|vegana).*',
                r'.*recomiendame algo que no lleve carne.*',
                r'.*recomiendame algo que sea (vegetariano|vegano)*',
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
                r'.*comida asi(a|á)tica.*',
                r'.*recomi(e|é)ndame algo asi(a|á)tico.*',
                r'.*comida de (a|A)sia.*',
                r'.*comida china.*',
                r'.*comida japonesa.*'


                
            ],
            'respuesta': [
                ''
            ]
        },

        #/////////////////////////// recomendaciones
        {
            'intent':'recomendar',
            'regex':[
                
                r'.*recomienda.*',
                r'.*recomendar.*',
                r'.*alguna sugerencia.*',
                r'.*tipos de comidas.*',
                
                r'.*qu(e|é) me.*(recomiendas|recomendar|recomendar(i|í)as)',
                r'.*recomi(e|é)ndame.*',
                r'.*recomendaci(o|ó)n.*',


            ],
            'respuesta':[
                'Se me ocurren varias opciones que podrían incluir carne, comida asiática, mariscos o platos vegetarianos. ¿Qué tipo de comida se te antoja? ¡Dime y te daré algunos ejemplos para que elijas!'
            ]
        },

        #//////////////////////////////Bienvenida
        {
            'intent':'bienvenida',
            'regex':[
                r'.*hola.*',
                r'.*buen(a|o)s (dias|tardes|noches).',
                r'que onda'
            ],
            'respuesta':[
                'Hola! soy una IA que te puede dar recomendaciones de comida Yummi! ^_^ solo pideme recomendaciones o la receta de algo que te guste',
                'Hey! que onda. Soy una IA que te puede recomendar algo de comer si tú no tienes idea  Yey! ^_^ solo pidemelo y con gusto te recomendare platillos'
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
                r'.*si.*',
                r'.*eso suena bien.*'
            ],
            'respuesta':[
                'genial, tambien te podria dar la receta si gustas preparalo, solo pidemelo :)',
                'Perfecto! Si quieres, también puedo proporcionarte la receta para que puedas prepararlo tú mismo solo pidemelo que yo te la dire con gusto. :)',
                '¡Fantástico! Si estás interesado, incluso puedo compartir contigo la receta solo necesitas pedirmela ;)'
            ]
        },

        #//////////////////// pedir informacion nutricional
        {
            'intent':'informacion_nutricional',
            'regex':[
                r'.*informaci(o|ó)n nutricional.*',
                r'.*calor(i|í)as.*',
                r'.*nutrici(o|ó)n.*',
                r'.*informaci(o|ó)n.*',
                r'.*info*',
                r'.*nutricional.*'
            ],
            'respuesta':[
                'Claro, te puedo dar la informacion nutricional, solo dame un segundo para buscarla y te la paso'
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