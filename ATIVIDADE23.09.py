
class Quadrado:
    def init(self,lado_1):
        self.lado_1 = lado_1
    def str(self):
        return f"area:{self.area()} perimetro:{self.perimetro()}"
    def area(self):
        return self.lado_1 * self.lado_1
    def perimetro(self):
        return 4 * self.lado_1

class Retangulo(Quadrado):
    def init(self,lado1,lado2):
        self.lado1 = lado1
        self.lado2 = lado2
    def str(self):
        return f"area:{self.area()} perimetro:{self.perimetro()}"
    def area(self):
        return self.lado1 * self.lado2
    def perimetro(self):
        return self.lado2 * self.lado1 / 2



print(Quadrado(5))
print(Retangulo(2,4))