"""
Exercício 1: Banco

O banco Tatu, moderno e eficiente, precisa de um novo programa para controlar o saldo de
seus correntistas. Cada conta corrente pode ter um ou mais clientes como titular. O banco
controla apenas o nome e o telefone de cada cliente. A conta corrente apresenta um saldo e
uma lista de operações de saques e depósitos. Quando o cliente fizer um saque, diminuiremos
o saldo da conta corrente. Quando ele fizer um depósito, aumentaremos o saldo. O banco
oferece também contas especiais, com limite especial além do saldo, e conta poupança, que
oferece um rendimento mensal sempre que o saldo na conta completa um mês. Evidentemente
é necessário oferecer aos clientes a possibilidade de verificar saldos, extratos e um resumo
com todas as informações da conta e seus respectivos clientes.
"""

from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, saldo_inicial: int, tipo: str):
        self.__saldo = saldo_inicial
        self.__tipo = tipo

    ## Getters
    @property
    def saldo(self):
        return self.__saldo

    @property
    def tipo(self):
        return self.__tipo

    ## Setters
    @tipo.setter
    def trocar_tipo_de_conta(self, novo_tipo: str):
        self.__tipo = novo_tipo

    ## Métodos comuns
    def saque(self, valor: int):
        self.__saldo -= valor

    def deposito(self, valor: int):
        self.__saldo += valor

    def print_saldo(self):
        print(f"Saldo: {self.__saldo}")

    def print_info(self):
        ## TODO
        pass

    def print_extrato(self):
        ## TODO
        pass


class Corrente:
    def __init__(self, saldo_inicial: int, tipo="corrente":
        self.__saldo = saldo_inicial
        self.tipo = tipo

    @property
    def saldo(self):
        return self.__saldo

    def saque(self, valor: int):
        if 
        self.__saldo -= valor

    def deposito(self, valor: int):
        self.__saldo += valor

class Cliente:
    def __init__(self, nome: str, telefone: str):
        self.nome = nome
        self.telefone = telefone

