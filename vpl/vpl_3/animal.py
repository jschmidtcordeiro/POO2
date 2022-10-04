from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, tamanho_passo):
        self.__tamanho_passo = tamanho_passo

    @property
    def tamanho_passo(self):
        return self.__tamanho_passo

    @tamanho_passo.setter
    def tamanho_passo(self, tamanhoPasso):
        self.__tamanho_passo = tamanhoPasso

    def mover(self):
        # Implementar método - Método será sobrescrito em ave
        mensagem = f"ANIMAL: DESLOCOU {self.__tamanho_passo}"
        return mensagem

    @abstractmethod
    def produzir_som(self):
        pass