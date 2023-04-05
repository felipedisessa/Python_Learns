class HOME:
    def __init__(self,perfil,nivel,atividades,nutricao,equilibrio="HOMEs"):
        self.perfil = perfil
        self.nivel = nivel
        self.atividades = atividades
        self.nutricao = nutricao
        self.equilibrio = equilibrio



    def HOME(self):
        print(self.HOME)
a1 = HOME("4Ricardo","","0","7","8")
a2= HOME("Felipe","4","5","2","7")

print(f'PERFIL: {a1.perfil}')
print(f'NIVEL: {a1.nivel}')
print(f"ATIVIDADES: {a1.atividades} ")
print(f"NUTRICAO: {a1.nutricao} ")
print(f"EQUILIBRIO: {a1.equilibrio} ")

print("+++++++++++++++++++++++++++++++++++++++++")

print(f'PERFIL: {a2.perfil}')
print(f'NIVEL: {a2.nivel}')
print(f"ATIVIDADES: {a2.atividades} ")
print(f"NUTRICAO: {a2.nutricao} ")
print(f"EQUILIBRIO: {a2.equilibrio} ")

print("+++++++++++++++++++++++++++++++++++++++++")


class EVOLUCAO:
    def __init__(self,passos,peso,tempo="EVOLUCAO"):
        self.EVOLUCAO = EVOLUCAO
        self.passos = passos
        self.peso = peso
        self.tempo = tempo

    def EVOLUCAO(self):
        print(self.HOME)
a3 = EVOLUCAO('8179',"70","1-15")
a4 = EVOLUCAO('6000',"80","2-0")

print(f'PASSOS: {a3.passos}')
print(f'PESO: {a3.peso}')
print(f'TEMPO: {a3.tempo}')

print("+++++++++++++++++++++++++++++++++++++++++")

print(f'PASSOS: {a4.passos}')
print(f'PESO: {a4.peso}')
print(f'TEMPO: {a4.tempo}')

print("+++++++++++++++++++++++++++++++++++++++++")


class VIBE:
    def __init__(self,dormir="VIBE"):
        self.VIBE = VIBE
        self.dormir = dormir


    def VIBE(self):
        print(self.HOME)
c3 = VIBE("64%")
c4 = VIBE("40%")

print(f'PORCENTAGEM: {c3.dormir}')


print("+++++++++++++++++++++++++++++++++++++++++")

print(f'PORCENTAGEM: {c4.dormir}')















