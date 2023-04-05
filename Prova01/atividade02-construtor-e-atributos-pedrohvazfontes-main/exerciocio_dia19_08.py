class Conta:
    def __init__(self,nome,cpf,saldo=None,limite_saque = None):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo
        self.limite_saque = limite_saque

def Deposito(conta):
    conta.saldo += float(input("Digite o valor do deposito: "))
    print(f"Deposito efetuado na conta de {conta.nome}, saldo atual {conta.saldo}")
print("#"*20)
saquedin = 0
def saque(conta):
    saquedin = float(input("Digite o valor do saque: "))
    if saquedin > conta.saldo and conta.limite_saque:
        print(f" O valor do saque foi excedido, digite um valor valido. \n"
              f"Saldo atual {conta.saldo} e o Limite de Saque é {conta.limite_saque}")
    else:
        conta.saldo = conta.saldo - saquedin
        print(f"Saque efetuado com sucesso, saldo atual {conta.saldo}")

def printaconta(conta):
    print(f"""
    Titular: {conta.nome},
    CPF: {conta.cpf},
    Saldo: {conta.saldo},
    Limite de Saque: {conta.limite_saque}    
    """)

print("Criando contas..")

"""conta_omar = Conta("Omar","265.584.354-45")
conta_maria = Conta(cpf="225.514.374-15",nome="Maria")
conta_ricardo = Conta("Ricardo","165.184.351-41",5000)
conta_karina = Conta("Karina","249.594.373-19",limite_saque=300)
"""

print("Criando proponente Omar")

conta_omar = Conta("","")
conta_omar.nome = input("Digite o nome do titular: ")
conta_omar.cpf = input("Digite o nº do CPF sem ponto e traço: ")
conta_omar.saldo = float(input("Digite o saldo existente na conta: "))
conta_omar.limite_saque = float(input("Digite o limite de saque da conta: "))

print("#"*20)
print("Exibição de dados do proponente Omar")
print(f"Titular {conta_omar.nome}; CPF {conta_omar.cpf}; Saldo {conta_omar.saldo}; Limite {conta_omar.limite_saque}")

print("#"*20)

print("Criando proponente Maria")

conta_maria = Conta("","")
conta_maria.nome = input("Digite o nome do titular: ")
conta_maria.cpf = input("Digite o nº do CPF sem ponto e traço: ")
conta_maria.saldo = float(input("Digite o saldo existente na conta: "))
conta_maria.limite_saque = float(input("Digite o limite de saque da conta: "))

print("#"*20)
print("Exibição de dados do proponente Maria")
print(f"Titular {conta_maria.nome}; CPF {conta_maria.cpf}; Saldo {conta_maria.saldo}; Limite {conta_maria.limite_saque}")
print("#"*20)

print("Criando proponente Ricardo")


conta_ricardo = Conta("","")
conta_ricardo.nome = input("Digite o nome do titular: ")
conta_ricardo.cpf = input("Digite o nº do CPF sem ponto e traço: ")
conta_ricardo.saldo = float(input("Digite o saldo existente na conta: "))
conta_ricardo.limite_saque = float(input("Digite o limite de saque da conta: "))

print("#"*20)
print("Exibição de dados do proponente Ricardo")
print(f"Titular {conta_ricardo.nome}; CPF {conta_ricardo.cpf}; Saldo {conta_ricardo.saldo}; Limite {conta_ricardo.limite_saque}")

print("#" *20)
print("Criando proponente Karina")


conta_karina = Conta("","")
conta_karina.nome = input("Digite o nome do titular: ")
conta_karina.cpf = input("Digite o nº do CPF sem ponto e traço: ")
conta_karina.saldo = float(input("Digite o saldo existente na conta: "))
conta_karina.limite_saque = float(input("Digite o limite de saque da conta: "))

print("#"*20)
print("Exibição de dados do proponente Karina")
print(f"Titular {conta_karina.nome}; CPF {conta_karina.cpf}; Saldo {conta_karina.saldo}; Limite {conta_karina.limite_saque}")

print("#" *20)

Deposito(conta_omar)
print("#"*20)
saque(conta_omar)
print("#"*20)
printaconta(conta_omar)



