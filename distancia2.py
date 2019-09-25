palabra1 = input("Escribe la primera palabra:")
palabra2 = input("Escribe la seguda palabra:")



def distanciaH(palabra1,palabra2):
    longitud1 = len(palabra1)
    longitud2 = len(palabra2)
    if longitud1 == longitud2:
        distancia = 0
        for i in range(longitud1): #enumera elementos en una lista
            #distancia = distancia + longitud1[i]
            if palabra1[i] != palabra2[i]:
                distancia = distancia + 1


        return distancia

    else:
        print("las palabras deben tener la misma longitud")

print(distanciaH(palabra1,palabra2))
