class Botao:
    def __init__(self):
        print("Sou o construtor da classe Botao")
        self.funcionalidade = None
        self.tamanho = None
        self.material = None
        
b_ligar = Botao()


class Quadrilatero:
    def __init__(self):
        self.forma = None
        self.cor = None
        self.tamanho = None
        self.contemBorda = None
q1 = Quadrilatero()
q1.forma = "quadrado"
q1.cor = "vermelho"
q1.tamanho = "mediano"
q1.contemborda = True
print(f"forma:{q1.forma}")
print(f"forma: {q1.cor}")
print(f"forma:{q1.tamanho}")
print(f"forma:{q1.contemborda}")
     
        



        