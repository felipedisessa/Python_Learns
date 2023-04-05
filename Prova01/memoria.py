class Estudante:
        def __init__(self, ra, nome, curso):
                self.ra = ra
                self.nome = nome
                self.curso = curso

e1 = Estudante("RA1","Joao","SI")
e2 = Estudante("RA2","Maria","Turismo")
e3 = Estudante("RA3","Pedro","Matematica")        

e4 = e2
e4.curso = e1.ra
e3.nome = e3.ra
e5 = None

