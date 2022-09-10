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

    def cadastrar_turma(self, turma):
        self.__turmas.append(turma)

    def __str__(self):
        return self.__nome


class Professor:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__turmas = []

    def get_nome(self):
        return self.__nome

    def cadastrar_turma(self, turma):
        self.__turmas.append(turma)
        turma.add_professor(self)

    def opcoes(self, lista_de_turmas):
        print("Para cadastrar o professor em uma turma selecione a turma:")
        for i in range(len(lista_de_turmas)):
            print(f"{i + 1} - {lista_de_turmas[i]}")
        op2 = int(input())
        self.cadastrar_turma(lista_de_turmas[op2 - 1])

    def __str__(self):
        return self.__nome

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
        pass
    def marcar_nota(self, aluno: Aluno, nota: int):
        ## TODO
        pass

    def opcoes(self, lista_de_professores):
        print("Opções:")
        print("""
        1 - Informações da turma
        2 - Adicionar aluno
        """)
        op = int(input())

        if op == 1:
            print(f"Nome: {self.__nome}")
            print("Alunos")
            for aluno in self.__alunos_info:
                print(f"{aluno['aluno']} Notas:{aluno['notas']} Presença: {aluno['presenca']}")
            print(f"Créditos: {self.__creditos}")
            print("Professores")
            print(*self.__professores)
        elif op == 2:
            matricula = int(input("Insira a matrícula:"))
            nome = input("Insira o nome:")
            iaa = int(input("Insira o IAA"))
            aluno = Aluno(matricula, nome, iaa)
            self.add_aluno(aluno)

    def __str__(self):
        return self.__nome

def main():
    lista_de_turmas = []
    lista_de_professores = []
    while True:
        print("Insira o valor para selecionar a opção:")
        print("1 - Criar turma")
        print("2 - Mostrar lista de turmas")
        print("3 - Cadastrar professor")
        print("4 - Mostrar professores")

        op = int(input())
        if op == 1:
            nome = input("Insira o nome da turma:")
            creditos = int(input("Insira o número de créditos da turma:"))
            turma = Turma(nome, creditos)
            lista_de_turmas.append(turma)
        elif op == 2:
            print("Turmas")
            for i in range(len(lista_de_turmas)):
                print(f"{i + 1} - {lista_de_turmas[i]}")
            op2 = int(input("Insira o número da turma:"))
            lista_de_turmas[op2 - 1].opcoes(lista_de_professores)
        elif op == 3:
            nome = input("Insira o nome do professor:")
            professor = Professor(nome)
            lista_de_professores.append(professor)
        elif op == 4:
            print("Professores")
            for i in range(len(lista_de_professores)):
                print(f"{i + 1} - {lista_de_professores[i]}")
            op2 = int(input("Insira o número do professor:"))
            lista_de_professores[op2 - 1].opcoes(lista_de_turmas)

main()
