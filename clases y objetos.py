class rectangulo:
    def __init__(self,longitud,ancho):
        self.longitud = longitud
        self.ancho = ancho

    def _calcular_area(self):
        self.area = self.longitud * self.ancho
        return self.area

    def _calcular_perimetro(self):
        self.perimetro =( self.longitud + self.ancho)*2
        return self.perimetro 

obj1 = rectangulo(5,4)
print(obj1._calcular_area() )
print(obj1._calcular_perimetro())
