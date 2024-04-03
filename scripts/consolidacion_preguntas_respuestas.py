import pandas as pd
import pickle

LATINOBAROMETRO_ESP = '../datasets/Latinobarometro_2020_Esp_Stata_v1_0.dta'

preguntas_seleccionadas = {
    'P11S0037': 'En general, ¿Diría Ud. que está muy satisfecho, más bien satisfecho, no muy satisfecho o nada satisfecho con el funcionamiento de la democracia en Argentina en el año 2020?',
    'P11S0038':'En general, ¿Diría Ud. que está muy satisfecho, más bien satisfecho, no muy satisfecho o nada satisfecho con el funcionamiento de la economía en Argentina en el año 2020?',
    'P2ST':'¿Diría Ud. que Argentina en el año 2020 ...?',
    'P12ST':'En términos generales ¿Diría usted que Argentina está gobernada por unos cuantos grupos poderosos en su propio beneficio, o que está gobernado para el bien de todo el pueblo?',
    'P4STGBS': '¿Cómo calificaría en general la situación económica de Argentina en el año 2020? Diría Ud. que es...',
    'P5STGBS': '¿Considera Ud. que la situación económica de Argentina en 2020 estaba mucho mejor, un poco mejor, igual, un poco peor, o mucho peor que en 2019?',
    'P14GBS': '¿Cómo diría Ud. que es la democracia en Argentina?',
    'P9STGBS': 'Hablando en general, ¿Diría Ud. que se puede confiar en la mayoría de las personas o que uno nunca es lo suficientemente cuidadoso en el trato con los demás?',
    'P10STGBS': '¿Con cuál de las siguientes frases está Ud. más de acuerdo?',
    'P17STGBS': '¿Ud. aprueba o no aprueba la gestión del gobierno argentino que encabeza el presidente Alberto Fernandez?',
    'P18ST': 'En política se habla normalmente de "izquierda" y "derecha". En una escala dónde “00" es la “izquierda” y “10" la “derecha”, ¿Dónde se ubicaría Ud.?',
    'P19ST': '¿Cuán justa cree Ud. que es la distribución del ingreso en Argentina?',
    'P19ST_A': '¿Cuán justa cree Ud. que es el acceso a la educación en Argentina?',
    'P19N_B': '¿Cuán justa cree Ud. que es el acceso a la justicia en Argentina?',
    'P26N_A': '¿Está Ud. muy a favor, algo a favor, algo en contra o muy en contra de la integración de Argentina con los otros países de Améria Latina?',
    'P28ST': '¿Considera Ud. que la inversión extranjera es beneficiosa o es perjudicial para el desarrollo económico de Argentina o no sabe lo suficiente para opinar?',
    'P20ST_A': 'Por favor, dígame si está muy de acuerdo, de acuerdo, en desacuerdo o muy en desacuerdo, con la siguiente afirmación. La democracia puede tener problemas pero es el mejor sistema de gobierno',
    'P20ST_B': 'Por favor, dígame si está muy de acuerdo, de acuerdo, en desacuerdo o muy en desacuerdo, con la siguiente afirmación. No me importaría que un gobierno no democrático llegara al poder si resuelve los problemas',
    'P20ST_C': 'Por favor, dígame si está muy de acuerdo, de acuerdo, en desacuerdo o muy en desacuerdo, con la siguiente afirmación. La democracia permite que se solucionen los problemas que tenemos',
    'P20ST_D': 'Por favor, dígame si está muy de acuerdo, de acuerdo, en desacuerdo o muy en desacuerdo, con la siguiente afirmación. En caso de dificultades esta bien que el presidente controle los medios de comunicación',
    'P20ST_E': 'Por favor, dígame si está muy de acuerdo, de acuerdo, en desacuerdo o muy en desacuerdo, con la siguiente afirmación. Es posible erradicar la corrupción de la política',
    'P20ST_F': 'Por favor, dígame si está muy de acuerdo, de acuerdo, en desacuerdo o muy en desacuerdo, con la siguiente afirmación. Se puede pagar el precio de cierto grado de corrupción, siempre que se solucionen los problemas del país',
    'P20ST_G': 'Por favor, dígame si está muy de acuerdo, de acuerdo, en desacuerdo o muy en desacuerdo, con la siguiente afirmación. Si no denuncio un acto de corrupción que tengo conocimiento me transformo en cómplice',
    'P21STM': '¿Apoyaría Ud. a un gobierno militar en reemplazo del gobierno democrático si las cosas se ponen muy difíciles, o no apoyaría Ud. en ninguna circunstancia un gobierno militar?',
    'P29ST_A': 'Ud. está muy de acuerdo (1), de acuerdo (2), en desacuerdo (3) o muy en desacuerdo (4) con la siguiente afirmación?. Que Argentina pueda comprar bienes y servicios libremente de cualquier otro país de América Latina y que cualquier otro país pueda vender bienes y servicios en otro pais de América Latina',
    'P29ST_B': 'Ud. está muy de acuerdo (1), de acuerdo (2), en desacuerdo (3) o muy en desacuerdo (4) con la siguiente afirmación?. La libre importación de bienes y servicios favorece al consumidor',
    'P29ST_C': 'Ud. está muy de acuerdo (1), de acuerdo (2), en desacuerdo (3) o muy en desacuerdo (4) con la siguiente afirmación?. En general, los productos nacionales son de menor calidad que los productos importados',
    'P29ST_D': 'Ud. está muy de acuerdo (1), de acuerdo (2), en desacuerdo (3) o muy en desacuerdo (4) con la siguiente afirmación?. Al mismo precio prefiero comprar bienes nacionales que importados',
    'P29ST_E': 'Ud. está muy de acuerdo (1), de acuerdo (2), en desacuerdo (3) o muy en desacuerdo (4) con la siguiente afirmación?. Los robots van a quitarme mi empleo de aquí a 10 años o más',
    'P29ST_F': 'Ud. está muy de acuerdo (1), de acuerdo (2), en desacuerdo (3) o muy en desacuerdo (4) con la siguiente afirmación?. Se debe cerrar la economía al comercio exterior para evitar que los productos extranjeros compitan con los nacionales',
    'P29ST_G': 'Ud. está muy de acuerdo (1), de acuerdo (2), en desacuerdo (3) o muy en desacuerdo (4) con la siguiente afirmación?. Estoy capacitado para manejar las nuevas tecnologías en mi trabajo',
    'P29ST_H': 'Ud. está muy de acuerdo (1), de acuerdo (2), en desacuerdo (3) o muy en desacuerdo (4) con la siguiente afirmación?. La inteligencia artificial y la robótica harán desaparecer más puestos de trabajo que los que creará',
    'P22ST_A': '¿Diría Ud. que los argentinos cumplen las leyes?',
    'P22ST_B': '¿Diría Ud. que los argentinos Son exigentes de sus derechos?',
    'P22ST_C': '¿Diría Ud. que los argentinos Son concientes de sus obligaciones y deberes?',
    'P22ST_D': '¿Diría Ud. que los argentinos Son iguales ante la ley?',
    'P23N':'De la siguiente lista me podría decir ¿quienes son los que Ud. cree que cumplen con las leyes en argentina?',
    'P30ST_A': '¿Tiene Ud. una opinión muy favorable (1), algo favorable (2), algo desfavorable (3) o muy desfavorable (4) opinión sobre EEUU, Estados Unidos?',
    'P30ST_B': '¿Tiene Ud. una opinión muy favorable (1), algo favorable (2), algo desfavorable (3) o muy desfavorable (4) opinión sobre Rusia?',
    'P30ST_C': '¿Tiene Ud. una opinión muy favorable (1), algo favorable (2), algo desfavorable (3) o muy desfavorable (4) opinión sobre China?',
    'P30ST_D': '¿Tiene Ud. una opinión muy favorable (1), algo favorable (2), algo desfavorable (3) o muy desfavorable (4) opinión sobre Unión Europea?',
    'P30ST_E': '¿Tiene Ud. una opinión muy favorable (1), algo favorable (2), algo desfavorable (3) o muy desfavorable (4) opinión sobre Cuba?',
    'P30ST_F': '¿Tiene Ud. una opinión muy favorable (1), algo favorable (2), algo desfavorable (3) o muy desfavorable (4) opinión sobre Venezuela?',
    'P31ST_A': '¿Y cómo calificaría Ud. las relaciones entre Argentina y los Estados Unidos? ¿Diría Ud. que son....?',
    'P31ST_B': '¿Y cómo calificaría Ud. las relaciones entre Argentina y Rusia? ¿Diría Ud. que son....?',
    'P31ST_C': '¿Y cómo calificaría Ud. las relaciones entre Argentina y China? ¿Diría Ud. que son....?',
    'P31ST_D': '¿Y cómo calificaría Ud. las relaciones entre Argentina y la Unión Europea? ¿Diría Ud. que son....?',
    'P31ST_E': '¿Y cómo calificaría Ud. las relaciones entre Argentina y Venezuela?? ¿Diría Ud. que son....?',
    'P25N': '¿Por lo que Ud sabe o ha oido, cree Ud que la integración de argentina con otros países de la región ha aumentado mucho, ha aumentado algo, ha disminuido algo o ha disminuido mucho entre 2015 y 2020?',
    'P33N': '¿Cuál es la mayor ventaja del comercio con China?',
    'P34N': '¿Cuál es la mayor desventaja del comercio con China?',
    'P35N_A':'Tomando todo en cuenta ¿diría Ud que la influencia de EEUU en argentina es mas bien positiva, o más bien negativa?',
    'P35N_B':'Tomando todo en cuenta ¿diría Ud que la influencia de China en argentina es mas bien positiva, o más bien negativa?',
    'P41N':'¿Como evalúa Ud en general la capacidad que ha tenido argentina para combatir la pandemia durante 2020?',
    'P36N_A': '¿cuánta confianza tiene usted en Las Fuerzas Armadas de los Estados Unidos: mucha (1), algo (2), poca (3) o ninguna (4)?',
    'P36N_B': '¿cuánta confianza tiene usted en Las Fuerzas Armadas de Chinas: mucha (1), algo (2), poca (3) o ninguna (4)?',
    'P42N': 'Imagínese que el estado tiene dos soluciones y tiene que elegir una sola. Una es entregarle recursos a la policía para que ellos combatan la delincuencia. La segunda es entregarle los recursos a la gente para que cada cual pueda combatir la delincuencia en su barrio con alarmas, seguridad privada etc. ¿Cuál prefiere Ud.?',
    'P37N_A':'Por favor, para la siguiente afirmación sobre los inmigrantes,las personas de otros países que vienen a vivir a argentina deme su opinion, lo encuentra muy positivo (1), algo positivo (2), algo negativo (3), muy negativo (4): Recibir inmigrantes de países fuera de América Latina',
    'P37N_B':'Por favor, para la siguiente afirmación sobre los inmigrantes,las personas de otros países que vienen a vivir a argentina deme su opinion, lo encuentra muy positivo (1), algo positivo (2), algo negativo (3), muy negativo (4): Recibir inmigrantes de América Latina',
    'P37N_C':'Por favor, para la siguiente afirmación sobre los inmigrantes,las personas de otros países que vienen a vivir a argentina deme su opinion, lo encuentra muy positivo (1), algo positivo (2), algo negativo (3), muy negativo (4): Recibir inmigrantes de Haití',
    'P37N_D':'Por favor, para la siguiente afirmación sobre los inmigrantes,las personas de otros países que vienen a vivir a argentina deme su opinion, lo encuentra muy positivo (1), algo positivo (2), algo negativo (3), muy negativo (4): Recibir inmigrantes de Venezuela',
    'P46STGBS': '¿Cuán interesado está Ud. en la política?',
    'P47ST_A': '¿Hasta qué punto la libertad para participar en política está garantizada en Argentina?',
    'P47ST_B': '¿Hasta qué punto la libertad para elegir mi oficio/profesión está garantizada en Argentina?',
    'P47ST_C': '¿Hasta qué punto la protección del medio ambiente está garantizada en Argentina?',
    'P47ST_D': '¿Hasta qué punto la protección de la propiedad privada está garantizada en Argentina?',
    'P47ST_E': '¿Hasta qué punto la justa distribución de la riqueza está garantizada en Argentina?',
    'P47ST_F': '¿Hasta qué punto la igualdad entre hombres y mujeres está garantizada en Argentina?',
    'P47ST_G': '¿Hasta qué punto la igualdad de oportunidades sin importar el origen de cada cual está garantizada en Argentina?',
    'P47ST_H': '¿Hasta qué punto la libertad de expresión siempre y en todas partes está garantizada en Argentina?',
    'P47ST_I': '¿Hasta qué punto la libertad de profesar cualquier religión está garantizada en Argentina?',
    'P47ST_J': '¿Hasta qué punto la protección contra el crimen está garantizada en Argentina?',
    'P47ST_K': '¿Hasta qué punto la seguridad social está garantizada en Argentina?',
    'P47ST_L': '¿Hasta qué punto la solidaridad con los pobres y los necesitados está garantizada en Argentina?',
    'P47ST_M': '¿Hasta qué punto la oportunidades de conseguir trabajo está garantizada en Argentina?',
    'P48ST': '¿Quién cree Ud. que tiene más poder en Argentina?',
    'P49STGBS': '¿Hay algún partido político argentino hacia el cual se sienta usted más cercano que hacia el resto de los partidos?',
    'P60N_B': '¿Y Ud, diría que si una persona expresa públicamente sus opiniones acerca de los problemas de argentina, podría tener consecuencias negativas para ella?'
}

if __name__ == '__main__':
    reader = pd.io.stata.StataReader(LATINOBAROMETRO_ESP)
    respuestas = reader.value_labels()
    
    respuestas['P19ST']   = respuestas['P19ST_A']
    respuestas['P20ST_B'] = respuestas['P20ST_A']
    respuestas['P20ST_C'] = respuestas['P20ST_A']
    respuestas['P20ST_D'] = respuestas['P20ST_A']
    respuestas['P29ST_E'] = respuestas['P29ST_A']
    respuestas['P29ST_H'] = respuestas['P29ST_A']
    respuestas['P23N']    = respuestas['P23N_01']
    respuestas['P30ST_F'] = respuestas['P30ST_E']
    respuestas['P31ST_E'] = respuestas['P31ST_A']
    respuestas['P48ST']   = respuestas['P48ST_1']

    with open('./datasets/respuestas.pickle', 'wb') as handle:
        pickle.dump(respuestas, handle, 
                    protocol=pickle.HIGHEST_PROTOCOL)

    with open('./datasets/preguntas_seleccionadas.pickle', 'wb') as handle:
        pickle.dump(preguntas_seleccionadas, handle, 
                    protocol=pickle.HIGHEST_PROTOCOL)