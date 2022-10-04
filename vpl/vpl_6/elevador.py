from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException


class Elevador(AbstractElevador):
    def __init__(
        self,
        andarAtual: int,
        totalAndaresPredio: int,
        capacidade: int,
        totalPessoas: int,
    ):
        self.__andar_atual = andarAtual
        self.__total_andares_predio = totalAndaresPredio
        self.__capacidade = capacidade
        self.__total_pessoas = totalPessoas

    # ElevadorJahNoTerreoException
    def descer(self) -> str:
        if self.__andar_atual <= 0:
            raise ElevadorJahNoTerreoException
        else:
            self.__andar_atual -= 1

    # ElevadorCheioException
    def entraPessoa(self) -> str:
        if self.__total_pessoas == self.__capacidade:
            raise ElevadorCheioException
        else:
            self.__total_pessoas += 1

    # ElevadorJahVazioException
    def saiPessoa(self) -> str:
        if self.__total_pessoas == 0:
            raise ElevadorJahVazioException
        else:
            self.__total_pessoas -= 1

    # ElevadorJahNoUltimoAndarException
    def subir(self) -> str:
        if self.__andar_atual >= self.__total_andares_predio - 1:
            raise ElevadorJahNoUltimoAndarException
        else:
            self.__andar_atual += 1

    @property
    def capacidade(self) -> int:
        return self.__capacidade

    @property
    def totalPessoas(self) -> int:
        return self.__total_pessoas

    @property
    def totalAndaresPredio(self) -> int:
        return self.__total_andares_predio

    @property
    def andarAtual(self) -> int:
        return self.__andar_atual

    @totalAndaresPredio.setter
    def totalAndaresPredio(self, totalAndaresPredio: int):
        self.__total_andares_predio = totalAndaresPredio