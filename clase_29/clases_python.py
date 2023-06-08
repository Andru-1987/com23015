class Rectangulo:
    __area = None
    __perimetro = None

    def __init__(self,**kwargs):
        self.alto =  kwargs["alto"]
        self.base = kwargs["base"]

    def calculo_area(self):
        self.__area = self.alto * self.base
        return self.__area

    def calculo_perimetro(self):
        self.__perimetro = (self.alto * 2) + (self.base * 2)
        return self.__perimetro

    def __str__(self):
        return f"soy un rectangulo con\naltura: {self.alto}\nbase: {self.base}"


rect = Rectangulo(alto = 14 , base = 22)
print(rect._Rectangulo__area) # una forma de entrar a los elementos de un objeto
print(rect.calculo_area())
print(rect)
