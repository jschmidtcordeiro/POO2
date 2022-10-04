from abc import ABC, abstractmethod

class AbstractElevador(ABC):
    @abstractmethod
    def __init__(self,  andarAtual: int, totalAndaresPredio: int, capacidade: int, totalPessoas: int):
        self.__andar_atual = andarAtual
        self.__total_andares_predio = totalAndaresPredio
        self.__capacidade = capacidade
        self.__total_pessoas = totalPessoas

    # ElevadorJahNoTerreoException
    @abstractmethod
    def descer(self) -> str:
        if self.__andar_atual <= 0:
            raise ElevadorJahNoTerreoException
        else:
            self.__andar_atual -= 1

    # ElevadorCheioException
    @abstractmethod
    def entraPessoa(self) -> str:
        if self.__total_pessoas == capacidade:
            raise ElevadorCheioException
        else:
            self.__total_pessoas += 1

    # ElevadorJahVazioException
    @abstractmethod
    def saiPessoa(self) -> str:
        if self.__total_pessoas == 0:
            raise ElevadorJahVazioException
        else:
            self.__total_pessoas -= 1

    # ElevadorJahNoUltimoAndarException
    @abstractmethod
    def subir(self) -> str:
        if self.__andar_atual == self.__total_andares_predio:
            raise ElevadorJahNoUltimoAndarException
        else:
            self.__andar_atual += 1

    @property
    @abstractmethod
    def capacidade(self) -> int:
        return self.__capacidade

    @property
    @abstractmethod
    def totalPessoas(self) -> int:
        return self.__total_pessoas

    @property
    @abstractmethod
    def totalAndaresPredio(self) -> int:
        return self.__total_andares_predio

    @property
    @abstractmethod
    def andarAtual(self) -> int:
        return self.__andar_atual

    @totalAndaresPredio.setter
    @abstractmethod
    def totalAndaresPredio(self, totalAndaresPredio: int):
        self.__total_andares_predio = totalAndaresPredio

