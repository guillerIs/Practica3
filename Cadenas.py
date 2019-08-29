import sys


palabra="roma"
letra=palabra[0]
print (letra)

#len devuelve el número de caracteres de una cadena
longitud = len(palabra)
ultima = palabra[longitud-1] # ultima letra de la cadena
print(longitud)
print(ultima)

#recorrido
indice =0
while indice < len(palabra):
    letra2=palabra[indice]
    print (letra2)
    indice +=1

#comparar cadenas
# ¿dos cadenas son iguales?

if palabra == "roma":
    print("¡Quiero ir a Roma!")

#ordenar alfabeticamente
if palabra<"roma":
    print("la palabra,"+palabra+", va antes de roma")