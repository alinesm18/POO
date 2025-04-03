class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        # atributos privados
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # método para depositar dinheiro na conta
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"depósito de {valor} realizado com sucesso!")
        else:
            print("valor de depósito inválido. o valor deve ser positivo.")

    # método para sacar dinheiro da conta
    def sacar(self, valor):
        if valor > 0 and valor <= (self.__saldo + self.__limite):
            self.__saldo -= valor
            print(f"saque de {valor} realizado com sucesso!")
        elif valor > (self.__saldo + self.__limite):
            print("saldo insuficiente para realizar o saque.")
        else:
            print("valor de saque inválido. o valor deve ser positivo.")

    # método para obter o saldo atual
    def get_saldo(self):
        return self.__saldo

    # método para definir um novo limite de conta bancária
    def set_limite(self, novo_limite):
        if novo_limite >= 0:
            self.__limite = novo_limite
            print(f"novo limite de {novo_limite} definido com sucesso!")
        else:
            print("limite inválido. o limite deve ser um valor não negativo.")

    # método para obter o titular da conta (retornar o nome)
    def get_titular(self):
        return self.__titular

    # método get para pegar e retornar o saldo (alternativa ao get_saldo)
    def get_saldo_old(self):
        return self.__saldo

    # método set para definir um novo valor para o saldo
    def set_saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("valor negativo inválido!!!")

# Instanciando a classe
conta1 = ContaBancaria("aline", 1000.00, 500.00)

# Exibindo o titular da conta diretamente pelo método get_titular
print(f"titular: {conta1.get_titular()}")

# Exibindo o saldo bancário diretamente pelo método get_saldo
print(f"saldo atual: {conta1.get_saldo()}")

# Realizando um depósito
valor_deposito = float(input("digite o valor para depósito: "))
conta1.depositar(valor_deposito)
print(f"saldo após depósito: {conta1.get_saldo()}")

# Realizando um saque
valor_saque = float(input("digite o valor para saque: "))
conta1.sacar(valor_saque)
print(f"saldo após saque: {conta1.get_saldo()}")

# Modificando o limite da conta
novo_limite = float(input("digite o novo limite de crédito: "))
conta1.set_limite(novo_limite)

# Modificando o saldo com o método set_saldo
novoSaldo = float(input("digite o novo valor do saldo: "))
conta1.set_saldo(novoSaldo)
print(f"novo saldo da conta: {conta1.get_saldo()}")
