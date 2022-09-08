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

    def cadastrar_turma(self, turma: Turma):
        self.__turmas.append(turma)


class Professor:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__turmas = []

    def get_nome(self):
        return self.__nome

    def cadastrar_turma(self, turma: Turma):
        self.__turmas.append(turma)

class Turma:
    def __init__(self, nome: str, creditos: int):
        self.__nome = nome
        self.__alunos_info = []
        self.__creditos = creditos
        self.__professores = []

    def get_nome(self):
        return self.__nome

    def get_professores(self):
        return self.__professores

    def get_alunos_info(self):
        print("Digite o número do aluno para retornar suas informações")
        for i in range(len(self.__alunos_info)):
            print(f"{i + 1} - {self.__alunos_info[i].get_nome()}")
        op = int(input()) - 1

        return self.__alunos_info[op]

    def add_professor(self, professor: Professor):
        self.__professores.append(professor)

    def add_aluno(self, aluno: Aluno):
        self.__alunos_info.append({'aluno': aluno, 'notas': [], 'presenca': []})

    def marcar_presença(self, aluno: Aluno, presenca: int):
        ## TODO

    def marcar_nota(self, aluno: Aluno, nota: int):
        ## TODO
