import nltk
from nltk.tokenize.toktok import ToktokTokenizer



def tokenizar(ruta):
    toktok = ToktokTokenizer()
# Tokenizador de oraciones
    es_tokenizador_oraciones = nltk.data.load("tokenizers/punkt/spanish.pickle")

#def tokens():
    with open(ruta,'r',encoding="utf8")as file:
        parrafo=file.read()

    texto = es_tokenizador_oraciones.tokenize(parrafo)
    #print(texto)

    guarda_palabras=[]

    for s in texto:

        guarda_palabras=guarda_palabras+[t for t in toktok.tokenize(s)]

    return guarda_palabras

    #print (guarda_palabras)
tokens= tokenizar('practica3.txt')

print(tokens)




