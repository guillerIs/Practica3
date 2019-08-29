
import distance
#distance.hamming("roma", "bola")
#Distancia de Hamming Mide el número de posiciones con caracteres que no coinciden.


palabra1="roma"
palabra2="bola"

longitud1=len(palabra1)
longitud2=len(palabra2)

#indice =0
#diferencia=0

#función que calcule la distancia de Hamming
def distHamming(palabra1,palabra2):
    #assert len(palabra1)==len(palabra2)
    diferencia = 0
    for ch1, ch2 in zip(palabra1, palabra2):
        if ch1 != ch2:
            diferencia += 1
    return diferencia


print (distHamming(palabra1,palabra2))