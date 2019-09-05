import nltk
from nltk.tokenize.toktok import ToktokTokenizer
toktok = ToktokTokenizer()

#def tokens():
# Tokenizador de oraciones
es_tokenizador_oraciones = nltk.data.load("tokenizers/punkt/spanish.pickle")

def tokens():
    with open('C:/Users/Guiller Is/Documents/3_SEMESTRE/PLN/practica3.txt','r',encoding="utf8")as file:
        parrafo=file.read()

    texto = es_tokenizador_oraciones.tokenize(parrafo)

    guarda_palabras=[]

    for s in texto:

        guarda_palabras=guarda_palabras+[t for t in toktok.tokenize(s)]

    return guarda_palabras
    print(guarda_palabras)

