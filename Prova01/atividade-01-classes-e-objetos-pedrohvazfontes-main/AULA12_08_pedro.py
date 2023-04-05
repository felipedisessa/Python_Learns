class Cachorro:
    def __init__(self,cor,altura,tamanho,peso="Cachorro"):
        self.cor = cor
        self.altura = altura
        self.tamanho = tamanho
        self.peso = peso
 

    def Cachorro(self):
        print(self.Cachorro)
c1 = Cachorro('preto',"100","2","10")
c2 = Cachorro('Marrom',"060","5","5")

print(f'Cor: {c1.cor}')
print(f'altura: {c1.altura}')
print(f'tamanho: {c1.tamanho}')
print(f"peso: {c1.peso} ")
