class Livro:
    def __init__(self, titulo: str, autor: str, ano: int, editora: str, edicao: int, volume: int):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__editora = editora
        self.__edicao = edicao
        self.__volume = volume

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_ano(self):
        return self.__ano

    def get_editora(self):
        return self.__editora

    def get_edicao(self):
        return self.__edicao

    def get_volume(self):
        return self.__volume

    def set_titulo(self, titulo: str):
        self.__titulo = titulo

    def get_autor(self, autor: str):
        self.__autor = autor

    def get_ano(self, ano: int):
        self.__ano = ano

    def get_editora(self, editora: str):
        self.__editora = editora

    def get_edicao(self, edicao: int):
        self.__edicao = edicao

    def get_volume(self, volume: int):
        self.__volume = volume

    def __str__(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"Ano: {self.__ano}")
        print(f"Editora: {self.__editora}")
        print(f"Edição: {self.__edicao}")
        print(f"Volume: {self.__volume} ")

        return ""

class Biblioteca:
    def __init__(self):
        self.__livros_registrados = []

    def get_livros_registrados(self):
        return self.__livros_registrados

    def registrar_livro(self, livro: Livro):
        self.__livros_registrados.append(livro)


def main():
    biblioteca = Biblioteca()
    while True:
        print("Insira o numero para realizar a ação desejada:")
        print("0 - Sair")
        print("1 - Cadastrar um livro")
        print("2 - Ver livros cadastrados")

        op = int(input())

        if op == 0:
            break
        elif op == 1:
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano: "))
            editora = input("Editora: ")
            edicao = int(input("Edição: "))
            volume = int(input("Volume: "))
            livro = Livro(titulo, autor, ano, editora, edicao, volume)
            biblioteca.registrar_livro(livro)
        elif op == 2:
            livros = biblioteca.get_livros_registrados()
            for l in livros:
                print(l)


main()
