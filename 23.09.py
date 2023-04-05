class Biblioteca_Matematica:
    	def soma(num_1, num_2):
    		return num_1 + num_2
print(Biblioteca_Matematica.soma(2,4))

class Biblioteca_Matematica1(Biblioteca_Matematica):
	def soma(num_1, num_2, num_3):
		return num_1 + num_2 + num_3
print(Biblioteca_Matematica1.soma(2,4,6))

class Biblioteca_Matematica2(Biblioteca_Matematica):
    	def soma(num_1, num_2, num_3, num_4):
		    return num_1 + num_2 + num_3 + num_4
print(Biblioteca_Matematica2.soma(2,4,6,8))
