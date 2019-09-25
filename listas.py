
enteros = [1,2,3,4,5,6,7,8,9]
#numero = enteros[4]
#indice = enteros.index(5)
#print(numero)
#print(indice)

def sumatoria(lista):
    resultado = 0
    for i in range(len(lista)):
        resultado = resultado + lista[i]

    return resultado
a= sumatoria(enteros)
print (a)


#####otro for#####
def sumatoria(lista):

    for i in lista:
        resultado = resultado + lista[i]

    return resultado
a= sumatoria(enteros)
print (a)





    #numero = []
    #numero = enteros[3]
    #indice = enteros.index(5)
    #return numero

    #print(numero)

    #for i in range(enteros):
        #suma =