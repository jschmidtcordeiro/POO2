from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__lista_chamados = []
        self.__lista_tipo_chamado = []

    # Retorna o total de chamados registrados para o TipoChamado recebido como parametro
    # @param tipo TipoChamado
    # @return int com a quantidade total dos chamados daquele tipo
    def totalChamadosPorTipo(self, tipo: TipoChamado) -> int:
        i = 0
        for chamado in self.__lista_chamados:
            if chamado.tipo == tipo:
                i += 1
        return i

    # Permite incluir um novo chamado na lista de Chamados. O chamado incluido eh retornado como um IChamado
    # @param data data do chamado em formato Date
    # @param cliente referencia para o Cliente do chamado
    # @param tecnico referencia para o Tecnico do chamado
    # @param titulo titulo do chamado
    # @param descricao descricao do chamado
    # @param prioridade prioridade do chamado
    # @param tipo tipo do chamado (TipoChamado)
    # @return retorna o chamato cadastrado
    def incluiChamado(
        self,
        data: Date,
        cliente: Cliente,
        tecnico: Tecnico,
        titulo: str,
        descricao: str,
        prioridade: int,
        tipo: TipoChamado,
    ) -> Chamado:

        if not isinstance(data, Date):
            return

        if not isinstance(cliente, Cliente):
            return

        if not isinstance(tecnico, Tecnico):
            return

        if not isinstance(titulo, str):
            return

        if not isinstance(descricao, str):
            return

        if not isinstance(prioridade, int):
            return

        if not isinstance(tipo, TipoChamado):
            return

        for it_chamado in self.__lista_chamados:
            if (it_chamado.data == data and
                it_chamado.cliente == cliente and
                it_chamado.tecnico == tecnico and
                it_chamado.tipo == tipo):
                return chamado
        
        chamado = Chamado(data, cliente, tecnico, titulo, descricao, prioridade, tipo)
        self.__lista_chamados.append(chamado)

        return chamado

    # Permite incluir um novo TipoChamado na lista de TiposChamado. O TipoChamado incluido eh retornado como um ITipoChamado
    # @param codigo codigo do Tipo Chamado
    # @param nome nome do Tipo Chamado
    # @param descricao descricao do Tipo Chamado
    # @return retorna o Tipo Chamado cadastrado
    def incluiTipoChamado(self, codigo: int, descricao: str, nome: str) -> TipoChamado:

        for tipo_chamado in self.__lista_tipo_chamado:
            if tipo_chamado.codigo == codigo:
                return

        tipo_chamado = TipoChamado(codigo, descricao, nome)
        self.__lista_tipo_chamado.append(tipo_chamado)

        return tipo_chamado

    @property
    def tipoChamados(self):
        return self.__lista_tipo_chamado
