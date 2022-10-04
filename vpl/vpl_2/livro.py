from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numeroCapitulo: int, tituloCapitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        
        self.__editora = editora
        self.__autores = [autor]
        self.__capitulos = {}
        self.incluirCapitulo(numeroCapitulo, tituloCapitulo)

#============================================================================

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def editora(self):
        return self.__editora
    
    @property
    def autores(self):
        return self.__autores

#============================================================================
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @editora.setter
    def editora(self, editora):
        self.__editora = editora


#============================================================================

    def incluirAutor(self, autor: Autor):
        #Nao esqueca de garantir que o objeto recebido pertence a classe Autor...
        # ... Nao permitir insercao de Autores duplicados!
        if type(autor) == Autor and autor not in self.__autores:
            self.__autores.append(autor)


    def excluirAutor(self, autor: Autor):
        
        if autor in self.__autores:
            self.__autores.remove(autor)

    def incluirCapitulo(self, numeroCapitulo: int, tituloCapitulo: str):
        # ... Nao permitir insercao de Capitulos duplicados!
        cap = Capitulo(numeroCapitulo, tituloCapitulo)
        if not tituloCapitulo in self.__capitulos:
            self.__capitulos[tituloCapitulo] = cap
        

    def excluirCapitulo(self, tituloCapitulo: str):
        if tituloCapitulo in self.__capitulos:
            self.__capitulos.pop(tituloCapitulo)

    def findCapituloByTitulo(self, tituloCapitulo: str):
        if tituloCapitulo in self.__capitulos:
            return self.__capitulos[tituloCapitulo]

