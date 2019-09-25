class Calculadora:
    def __init__(self,num1,num2):
        self.numero1 = num1
        self.numero2 = num2

    def multiplicar(self):
        contador = self.numero2
        resultadoMultiplicar = 0
        #while(contador > 0):
            #resultadoMultiplicar =  resultadoMultiplicar + self.numero1
            #contador = contador - 1
        #return resultadoMultiplicar

        ######ciclo for#######

        for i in range(contador):
            resultadoMultiplicar = resultadoMultiplicar + self.numero1
            #print("ciclo:")
            
        return resultadoMultiplicar

    def entrada(self):
        n1 = int(input("Escribe el primer número:"))
        n2 = int(input("Escribe el segudo número:"))

        self.numero1=n1
        self.numero2=n2

resultados= Calculadora(15,10) #crear objeto
resultados.entrada()

resultadoMultiplicar=resultados.multiplicar()
print("La multiplicación es:",resultadoMultiplicar)


