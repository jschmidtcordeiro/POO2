from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        self.__elevador = None

    """
    Faz o elevador subir um andar. Se jah estiver no ultimo andar, 
    dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorJahNoUltimoAndarException
    """

    def subir(self) -> str:
        self.__elevador.subir()
        return "O elevador subiu"

    """
    Faz o elevador descer um andar. Se jah estiver no terreo, 
    dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorJahNoTerreoException
    """

    def descer(self) -> str:
        self.__elevador.descer()
        return "O elevador desceu"

    """
    Entra uma pessoa no Elevador. Se nao for possivel permitir a 
    entrada da pessoa, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorCheioException
    """

    def entraPessoa(self) -> str:
        self.__elevador.entraPessoa()
        return "Entrou uma pessoa no elevador"

    """
    Sai uma pessoa no Elevador. Se nao for possivel permitir a 
    saida de uma pessoa, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorJahVazioException
    """

    def saiPessoa(self) -> str:
        self.__elevador.saiPessoa()
        return "Saiu uma pessoa do elevador"

    """
    @return Elevador
    """

    @property
    def elevador(self) -> Elevador:
        return self.__elevador

    """
    @param andarAtual andar atual do elevador
    @param totalAndaresPredio total de andares do predio
    @param capacidade capacidade maxima do elevador
    @param totalPessoas total de pessoas atual do elevador
    """

    def inicializarElevador(
        self,
        andarAtual: int,
        totalAndaresPredio: int,
        capacidade: int,
        totalPessoas: int,
    ):
        if (
            not isinstance(andarAtual, int)
            or not isinstance(totalAndaresPredio, int)
            or not isinstance(capacidade, int)
            or not isinstance(totalPessoas, int)
            or andarAtual < 0
            or totalAndaresPredio < 0
            or capacidade < 0
            or totalPessoas < 0
            or totalPessoas > capacidade
            or andarAtual >= totalAndaresPredio
        ):
            raise ComandoInvalidoException()

        self.__elevador = Elevador(
            andarAtual, totalAndaresPredio, capacidade, totalPessoas
        )