from random import shuffle

baralho_padrao = [
  'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10', 'm11', 'm12',
  'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11', 'e12',
  'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12',
  'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12'
]


class Baralho:
    def __init__(self):
        self.__cartas_disponiveis = baralho_padrao
        self.__cartas_descarte = []

    def get_cartas_disponiveis(self):
        return self.__cartas_disponiveis

    def get_cartas_descarte(self):
        return self.__cartas_descarte

    def set_cartas_disponiveis(self, novas_cartas: list):
        self.__cartas_disponiveis = novas_cartas

    def set_cartas_descarte(self, novas_cartas: list):
        self.__cartas_descarte = novas_cartas

    def add_cartas_descarte(self, carta: str):
        self.__cartas_descarte.append(carta)

    def embaralhar_cartas_disponiveis(self):
        shuffle(self.__cartas_disponiveis)

    def embaralhar_tudo(self):
        self.__cartas_disponiveis.extend(self.__cartas_descarte)
        print(self.__cartas_disponiveis)

class Jogador:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__cartas = []

    def get_nome(self):
        return self.__nome

    def pegar_carta(self, baralho: Baralho):
        b = baralho.get_cartas_disponiveis()
        self.__cartas.append(b[0])
        b.pop(0)
        baralho.set_cartas_disponiveis(b)


    def ver_cartas(self):
        if len(self.__cartas) == 0:
            print("Você não possuí cartas")
        else:
            print("Suas cartas são:")
            for carta in self.__cartas:
                print(carta)

    def descartar_carta(self, baralho: Baralho, carta: str):
        for i in range(len(self.__cartas)):
            if carta == self.__cartas[i]:
                baralho.add_cartas_descarte(carta)
                self.__cartas.pop(i)

    def opcoes_de_jogada(self, baralho: Baralho):
        print("Digite o número referênte a ação desejada")
        print("1 - Pegar carta")
        print("2 - Ver cartas")
        print("3 - Descartar carta")

        op = int(input())

        if op == 1:
            self.pegar_carta(baralho)
        elif op == 2:
            self.ver_cartas()
        elif op == 3:
            print("Insira a carta que você quer descartar")
            carta = input()
            self.descartar_carta(baralho, carta)

class Menu:
    def __init__(self):
        self.__jogadores = []
        self.__baralho = Baralho()

    def get_jogadores(self):
        return self.__jogadores

    def get_baralho(self):
        return self.__baralho

    def opcoes(self):
        print("Digite o número referênte a ação desejada")
        print("1 - Reiniciar")
        print("2 - Embaralhar cartas disponíveis")
        print("3 - Embaralhar tudo")
        print("4 - Adicionar jogardor")
        for i in range(len(self.__jogadores)):
            print(f"{i + 5} - Jogador {self.__jogadores[i].get_nome()}")

        op = int(input())
        return op

    def reiniciar(self):
        pass

    def embaralhar_cartas_disponiveis(self):
        self.__baralho.embaralhar_cartas_disponiveis()

    def embaralhar_tudo(self):
        self.__baralho.embaralhar_tudo()

    def add_jogador(self):
        print("Insira o nome do jogador:")
        nome = input()
        jogador = Jogador(nome)
        self.__jogadores.append(jogador)

def main():
    while True:
        menu = Menu()

        while True:
            op = menu.opcoes()
            if op == 1:
                break
            elif op == 2:
                menu.embaralhar_cartas_disponiveis()
            elif op == 3:
                menu.embaralhar_tudo()
            elif op == 4:
                menu.add_jogador()
            elif op > 0 and op < (5 + len(menu.get_jogadores())):
                jogadores = menu.get_jogadores()
                jogador = jogadores[op - 5]
                jogador.opcoes_de_jogada(menu.get_baralho())

main()
