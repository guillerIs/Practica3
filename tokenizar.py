import nltk
from nltk.tokenize.toktok import ToktokTokenizer
# Tokenizador TokTok (palabras)
toktok = ToktokTokenizer()
# Tokenizador de oraciones
es_tokenizador_oraciones = nltk.data.load("tokenizers/punkt/spanish.pickle")
# Obtener oraciones de un parrafo
parrafo = "Este es un texto de prueba. ¿Crees que pueda tokenizar bien cada oraci´ on? ¡Ya lo veremos!"
oraciones = es_tokenizador_oraciones.tokenize(parrafo)
# Obtener tokens de cada oraci´ on
for s in oraciones:
    print([t for t in toktok.tokenize(s)])