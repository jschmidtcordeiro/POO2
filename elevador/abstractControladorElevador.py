from abc import ABC, abstractmethod
from elevador import Elevador


class AbstractControladorElevador(ABC):
    @abstractmethod
    def __init__(self):
        self.__elevador = None

    '''
    Faz o elevador subir um andar. Se jah estiver no ultimo andar, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorJahNoUltimoAndarException
    '''
    @abstractmethod
    def subir(self) -> str:
        self.__elevador.subir()
        return "O elevador subiu"

    '''
    Faz o elevador descer um andar. Se jah estiver no terreo, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorJahNoTerreoException
    '''
    @abstractmethod
    def descer(self) -> str:
        self.__elevador.descer()
        return "O elevador desceu"

    '''
    Entra uma pessoa no Elevador. Se nao for possivel permitir a entrada da pessoa, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorCheioException
    '''
    @abstractmethod
    def entraPessoa(self) -> str:
        self.__elevador.entraPessoa()
        return "Entrou uma pessoa no elevador"

    '''
    Sai uma pessoa no Elevador. Se nao for possivel permitir a saida de uma pessoa, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorJahVazioException
    '''
    @abstractmethod
    def saiPessoa() -> str:
        self.__elevador.saiPessoa()
        return "Saiu uma pessoa do elevador"

    '''
    @return Elevador
    '''
    @property
    @abstractmethod
    def elevador(self) -> Elevador:
        return self.__elevador

    '''
    @param andarAtual andar atual do elevador
    @param totalAndaresPredio total de andares do predio
    @param capacidade capacidade maxima do elevador
    @param totalPessoas total de pessoas atual do elevador
    '''
    @abstractmethod
    def inicializarElevador(self, andarAtual: int, totalAndaresPredio: int, capacidade: int, totalPessoas: int):
        if (
                isinstance(andarAtual, int) and
                isinstance(totalAndaresPredio, int) and
                isinstance(capacidade, int) and
                isinstance(totalPessoas, int)
        ):
            if(
                    andarAtual >= 0 and
                    totalAndaresPredio >= 0 and
                    capacidade >= 0 and
                    totalPessoas >= 0
            ):
                self.__elevador = Elevador(
                    andarAtual, totalAndaresPredio, capacidade, totalPessoas)
