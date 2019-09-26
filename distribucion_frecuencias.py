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


def frecuencia(token):
    listaGeneral = []
    listaNumero = []
    listaPalabra = []
    longitud = len(token)
    primera = token[0]
    listaPalabra.append(primera)
    listaNumero.append(1)
    print(longitud)

    contador = 0
    while(contador < longitud -1):
        if(primera == token[contador + 1]): #PRIMERA PALABRA ES IGUAL A LA QUE SIGUE? recorrer
            listaNumero[0] = listaNumero[0] + 1
        elif(token[contador + 1] in listaPalabra):  #palabra se encuentra en la lista? responde con V F
            indice = listaPalabra.index(token[contador + 1])#
            listaNumero[indice] = listaNumero[indice] + 1
        else:
            listaPalabra.append(token[contador + 1]) #
            listaNumero.append(1)
        contador = contador + 1 # sino se le suma 1 al contador el while se queda ciclado
        #unir listaPalabra y listaNumero en listaGeneral
    for i in range (len(listaPalabra)):
        listaGeneral.append((listaNumero[i],listaPalabra[i])) # i funciona contador

    listaGeneral.sort(reverse = True)
    return listaGeneral



tokens= tokenizar('practica3.txt')
muestra = frecuencia(tokens)
print(tokens)
print(muestra)


#muestra = frecuencia(listaGeneral)
#print(listaGeneral)

