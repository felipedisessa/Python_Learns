class Conta:
    def __init__(self,nome,cpf,saldo=0,limite_saque=1000):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo
        self.limite_saque = limite_saque
        
    def mostrar_dados(self):
        print("Banco Unifafibe")
        print(f"\tnome:{self.nome}")
        print(f"\tcpf:{self.cpf}")
        print(f"\tsaldo:{self.saldo}\tlimite_saque:{self.limite_saque}")    
        
    def fazer_deposito(self,deposito):
        self.saldo = deposito + self.saldo 

    def fazer_saque(self,saque):
        self.saldo = self.saldo - saque
    
conta_omar = Conta("Omar","265.584.354-45")
conta_maria = Conta(cpf="225.514.374-15",nome="Maria")
conta_ricardo = Conta("Ricardo","165.184.351-41",5000)
conta_karina = Conta("Karina","249.594.373-19",limite_saque=300)
#Dados Iniciais
print("\nCriando Contas")

conta_omar.fazer_deposito(600)
conta_omar.fazer_saque(1000)

conta_omar.mostrar_dados()
conta_maria.mostrar_dados()
conta_ricardo.mostrar_dados()
conta_karina.mostrar_dados()
#Movimento
print("\nExemplo Movimentos")


