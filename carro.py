class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.combustivel = 50  
        self.ligado = False    
        self.velocidade = 0   

    def ligar(self):
        if self.combustivel > 0:
            self.ligado = True
            return "carro ligado. :)"
        else:
            return "não há combustível suficiente para ligar o carro."

    def desligar(self):
        if self.velocidade == 0:
            self.ligado = False
            return "carro desligado. :()"
        else:
            return "o carro não pode ser desligado enquanto estiver em movimento."

    def acelerar(self):
        if self.ligado and self.combustivel > 0:
            self.velocidade += 10
            self.combustivel -= 5
            return "acelerando... tan tan tan..."
        else:
            return "não é possível acelerar. verifique se o carro está ligado e tem combustível."

    def frear(self):
        if self.velocidade >= 10:
            self.velocidade -= 10
            return "freando... caalma..."
        else:
            self.velocidade = 0
            return "o carro já está parado."

    def abastecer(self, quantidade):
        if self.combustivel + quantidade <= 100:
            self.combustivel += quantidade
        else:
            self.combustivel = 100
        return f"combustível abastecido. nível atual: {self.combustivel}"

    def buzinar(self):
        return "BI BI BI BI!"

    def status(self):
        estado = "modelo: {}, ano: {}, cor: {}, combustível: {}, velocidade: {} km/h, ligado: {}.".format(
            self.modelo, self.ano, self.cor, self.combustivel, self.velocidade, "Sim" if self.ligado else "Não"
        )
        return estado

# testando a classe:
if __name__ == "__main__":
    carro1 = Carro("impala", 1967, "preto")
    print(carro1.ligar())
    print(carro1.acelerar())
    print(carro1.abastecer(30))
    print(carro1.acelerar())
    print(carro1.status())
    print(carro1.frear())
    print(carro1.desligar())
    print(carro1.status())
