class PgInicial:
    def __init__(self,mural,atividades,pessoas,notas,materia="PgInicial"):
        self.mural = mural
        self.atividades = atividades
        self.pessoas = pessoas
        self.notas = notas
        self.materia = materia

    def PgInicial(self):
        print(self.PgInicial)
a = PgInicial('publicação1',"prova","turma1","7,8","Programação")
b = PgInicial("publicaão2","exercício","turma2","8,9","Infraestrutura")
c = PgInicial("publicaão3","avaliação","turma3","8,5","Banco de dados")

print(f'mural: {a.mural}')
print(f'atividades: {a.atividades}')
print(f'pessoas: {a.pessoas}')
print(f"notas: {a.notas} ")
print(f"materia: {a.materia} ")

print("+++++++++++++++++++++++++++++++++++++++++")

print(f'mural: {b.mural}')
print(f'atividades: {b.atividades}')
print(f'pessoas: {b.pessoas}')
print(f"notas: {b.notas} ")
print(f"materia: {b.materia} ")

print("+++++++++++++++++++++++++++++++++++++++++")

print(f'mural: {c.mural}')
print(f'atividades: {c.atividades}')
print(f'pessoas: {c.pessoas}')
print(f"notas: {c.notas} ")
print(f"materia: {c.materia} ")

class Conta:
    def __init__(self,perfil,curso,configuracao="Conta"):
        self.perfil = perfil
        self.curso = curso
        self.configuracao = configuracao


    def Conta(self):
        print(self.Conta)
a = Conta("Omar","Programação Orientada a objetos","configuração")
b = Conta("Felipe","Infraestrutura","configuração")
c = Conta("Lucas","Modelagem de software","configuração")

print(f'Perfil: {a.perfil}')
print(f'Curso: {a.curso}')
print(f'configuracao: {a.configuracao}')

print("+++++++++++++++++++++++++++++++++++++++++")

print(f'Peril: {b.perfil}')
print(f'Curso: {b.curso}')
print(f'configuracao: {b.configuracao}')

print("+++++++++++++++++++++++++++++++++++++++++")

print(f'Perfil: {c.perfil}')
print(f'Curso: {c.curso}')
print(f'configuracao: {c.configuracao}')

class Atividades:
    def __init__(self,recursos,atividades,unidade_aprendizagem,temas,data="Atividades"):
        self.recursos = recursos
        self.atividades = atividades
        self.unidade_aprendizagem = unidade_aprendizagem
        self.temas = temas
        self.data = data

    def Atividades(self):
        print(self.Atividades)
a = Atividades('participação em aula',"prova","configuração de ambiente","apresentação","5 de agosto")
b = Atividades("slides","exercício","apresentação","link","10 de agosto")
c = Atividades("extra","avaliação","python","unidade","14 de agosto")

print(f'Recursos: {a.recursos}')
print(f'atividades: {a.atividades}')
print(f'unidade_aprendizagem: {a.unidade_aprendizagem}')
print(f"temas: {a.temas} ")
print(f"Data: {a.data} ")

print("+++++++++++++++++++++++++++++++++++++++++")

print(f'Recursos: {b.recursos}')
print(f'atividades: {b.atividades}')
print(f'unidade_aprendizagem: {b.unidade_aprendizagem}')
print(f"temas: {b.temas} ")
print(f"Data: {b.data} ")

print("+++++++++++++++++++++++++++++++++++++++++")

print(f'Recursos: {c.recursos}')
print(f'atividades: {c.atividades}')
print(f'unidade_aprendizagem: {c.unidade_aprendizagem}')
print(f"temas: {c.temas} ")
print(f"Datas: {c.data} ")