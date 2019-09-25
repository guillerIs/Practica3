#funciones
#def sumar():
   # print (5+10)

#sumar()

#enviarle parámetros a esa función
#def sumarP(numero1, numero2):
    #print(numero1+numero2)

#sumarP(45,5)

class Calculadora:
    def __init__(self,num1,num2):
        self.numero1=num1
        self.numero2=num2

    def suma(self):
        resultadoSuma=self.numero1+self.numero2
        return resultadoSuma

    def resta(self):
        resultadoResta=self.numero1-self.numero2
        return resultadoResta

    def multiplicar(self):
        resultadoMultiplicar=self.numero1 * self.numero2
        return resultadoMultiplicar


    def division(self):
        #resultadoDivision=self.numero1/self.numero2
        #return resultadoDivision
        if self.numero2 == 0:
            print("Divisor 0")
        else:
            resultadoDivision=self.numero1 / self.numero2
            return resultadoDivision



    def entrada(self):
        n1=int(input("Escribe el primer número:"))
        n2=int(input("Escribe el segudo número:"))

        self.numero1=n1
        self.numero2=n2

resultados= Calculadora(15,10) #crear objeto
resultados.entrada()

resultadoSuma=resultados.suma()
resultadoResta=resultados.resta()
resultadoMultiplicar=resultados.multiplicar()
resultadoDivision=resultados.division()


print("Suma es:",resultadoSuma)
print("Resta es:",resultadoResta)
print("Multiplicación es:",resultadoMultiplicar)
print("División es:",resultadoDivision)
