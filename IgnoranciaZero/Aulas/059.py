class Retangulo(object):

    def __init__(self):
        self.ladoA=0
        self.ladoB=0

    def Mudar_Lado(self,a,b):
        self.ladoA=a
        self.ladoB=b

    def Retorna_Lado(self):
        return self.ladoA,self.ladoB

    def Caucula_Aria(self):
        return self.ladoA*self.ladoB

    def Calcular_Perimetro(self):
        return 2*(self.ladoB+self.ladoA)

largura=float(input("Digete a largura do piso: "))
comprimento=float(input("Digete o comprimento do piso: "))
print("")
retangulo=Retangulo()

retangulo.Mudar_Lado(largura,comprimento)

ladoA=float(input("Digete a largura do retangulo: "))
ladoB=float(input("Digete a Comprimento do retangulo: "))

ariaTota=ladoA*ladoB
resultado=round(retangulo.Caucula_Aria()/ariaTota)

print("Serão necessários %i pisos"%resultado)