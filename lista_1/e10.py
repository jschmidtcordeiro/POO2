class Aluno:
    def __init__(self, matricula: int, nome: str, iaa):
        self.__matricula = matricula
        self.__nome = nome
        self.__iaa = iaa
        self.__turmas = []

    def get_matricula(self):
        return self.__matricula

    def get_nome(self):
        return self.__nome

    def get_iaa(self):
        return self.__iaa

    def cadastrar_turmas(self):


class Professor:
    def __init__(self):
        pass

class Turma:
    def __init__(self):
        pass
