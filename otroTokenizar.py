#from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

my_sent = "Este es un texto de prueba. ¿Crees que pueda tokenizar bien cada oración? ¡Ya lo veremos!"
tokens = word_tokenize(my_sent)

print(tokens)


