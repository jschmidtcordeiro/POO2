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


class Conta:
    def __init__(self, saldo_inicial: int, tipo: str, correntista_inicial):
        self.__saldo = saldo_inicial
        self.__tipo = tipo
        self.__limite = 0
        self.__data_inicial = 0
        self.__correntistas = [correntista_inicial]

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
        if novo_tipo == "corrente":
            self.__tipo = novo_tipo
        elif novo_tipo == "vip":
            if self.__saldo > 1000:
                print("Parabéns, agora a sua conta é VIP")
                print(f"Seu limite é de {self.__limite}")
                self.__tipo = novo_tipo
            else:
                print("Infelizmente não foi possível abrir uma conta vip")

        elif novo_tipo == "poupanca":
            print("Sua conta agora é do tipo poupança")
            print(f"Data de troca do tipo da conta: {self.__data_inicial}")
            self.__data_inicial = 1
            self.__tipo = novo_tipo

        else:
            print("Não foi possível trocar de conta")


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

    def print_correntistas(self):
        print("Os correntista são:")
        for correntista in self.__correntistas:
            print(f"- {correntista}")

    def verificar_rendimento(self):
        if self.__tipo == "poupanca":
            if self.__data_inicial > 30:
                self.__data_inicial -= 30
                self.__saldo += self.__saldo * 0.001
                print(f"Seu novo saldo é {self.__saldo}")

class Correntista:
    def __init__(self, nome: str, telefone: int):
        self.__nome = nome
        self.__telefone = telefone
        self.__conta = False

    @property
    def nome(self):
        return self.__nome

    @property
    def telefone(self):
        return self.__telefone

    def criar_conta(self):
        self.__conta = Conta()


def main():
    correntistas = []
    while True:
        print("1 - Cadastro de usuário")
        for i in range(len(correntistas)):
            print(f"{i+2} - Acessar {correntistas[i].nome}")

        op = int(input())
        if op == 1:
            print("Insira o nome e o telefone")
            nome = input()
            telefone = int(input())
            c = Correntista(nome, telefone)
            correntistas.append(c)

        elif op >= len(correntistas) + 1:
            ## Mostra opções do correntista
            print(f"Bem vindo {correntistas[op - 2].nome}!")
            print("Escolha uma das opções abaixo")
            print("0 - Sair")
            print("Criar conta")

            op2 = int(input())

            if op2 == 0:
                break




main()

