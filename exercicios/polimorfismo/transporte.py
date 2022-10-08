from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, nome: str, altura: int, comprimento: int, carga: int, velocidade: int):
        self.__nome = nome
        self.__altura = altura
        self.__comprimento = comprimento
        self.__carga = carga
        self.__velocidade = velocidade

    @property
    def nome(self):
        return self.__nome

    @property
    def altura(self):
        return self.__altura

    @property
    def comprimento(self):
        return self.__comprimento

    @property
    def carga(self):
        return self.__carga

    @property
    def velocidade(self):
        return self.__velocidade

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @altura.setter
    def altura(self, altura: int):
        self._altura = altura

    @comprimento.setter
    def comprimento (self, comprimento: int):
        self.__comprimento = comprimento

    @carga.setter
    def carga(self, carga: int):
        self.__carga = carga

    @velocidade.setter
    def velocidade(self, velocidade: int):
        self.__velocidade = velocidade

    def __str__(self):
        return self.__nome


class TransporteAereo(Transporte):
    def __init__(self, nome: str, altura: int, comprimento: int, carga: int, velocidade: int,autonomia: int, envergadura: int):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__autonomia = autonomia
        self.__envergadura = envergadura

    @property
    def autonomia(self):
        return self.__autonomia

    @property
    def envergadura(self):
        return self.__envergadura

    @autonomia.setter
    def autonomia(self, autonomia: int):
        self.__autonomia = autonomia

    @envergadura.setter
    def envergadura(self, envergadura: int):
        self.__envergadura = envergadura

class TransporteTerrestre(Transporte):
    def __init__(self, nome: str, altura: int, comprimento: int, carga: int, velocidade: int,motor: str, rodas: str):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__motor = motor
        self.__rodas = rodas

    @property
    def motor(self):
        return self.__motor

    @property
    def rodas(self):
        return self.__rodas

    @motor.setter
    def motor(self, motor: str):
        self.__motor = motor

    @rodas.setter
    def rodas(self, rodas: str):
        self.__rodas = rodas

class TransporteAquatico(Transporte):
    def __init__(self, nome: str, altura: int, comprimento: int, carga: int, velocidade: int,boca: int, calado: int):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__boca = boca
        self.__calado = calado

    @property
    def boca(self):
        return self.__boca

    @property
    def calado(self):
        return self.__calado

    @boca.setter
    def boca(self, boca: int):
        self.__boca = boca

    @calado.setter
    def calado(self, calado: int):
        self.__calado = calado



class Catalogo():
    def __init__(self):
        self.__veiculos = []

    def inserir_veiculo(self, veiculo: Transporte):
        if isinstance(veiculo, Transporte):
            self.__veiculos.append(veiculo)

    def mostrar_veiculos(self):
        return self.__veiculos


c = Catalogo()

while True:
    print("""
    Selecione a opção desejada:
    1 - Inserir veículo
    2 - Mostrar veículos do catálogo
    """)

    op = input()

    if op == '1':
        print("""
        Selecione a opção desejada:
        1 - Adicionar transporte aéreo
        2 - Adicionar transporte terrestre
        3 - Adicionar transporte aquático
        """)

        op = input()
        # nome, altura, comprimento, carga, velocidad
        nome = input("Nome:")
        altura = input("Altura:")
        comprimento = input("Comprimento:")
        carga = input("Carga:")
        velocidade = input("Velocidade:")

        if op == '1':
            autonomia = input("Autonomia:")
            envergadura = input("Envergadura")
            veiculo = TransporteAereo(nome, altura, comprimento, carga, velocidade, autonomia, envergadura)
            c.inserir_veiculo(veiculo)
        elif op == '2':
            motor = input("Motor:")
            rodas = input("Rodas")
            veiculo = TransporteTerrestre(nome, altura, comprimento, carga, velocidade, motor, rodas)
            c.inserir_veiculo(veiculo)
        elif op == '3':
            boca = input("Boca:")
            calado = input("Calado:")
            veiculo = TransporteAquatico(nome, altura, comprimento, carga, velocidade, boca, calado)
            c.inserir_veiculo(veiculo)
        else:
            print("Seleção inválida")

    elif op == '2':
        veiculos = c.mostrar_veiculos()
        for veiculo in veiculos:
            print(f"- {veiculo}")
    else:
        print("Seleção inválida")

