
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} Temporadas - {self._likes} Likes'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def lsitagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)

arcane = Serie('Arcane', 2021, 1)
x = Filme('Jujutsu', 2022, 130)
avatar = Filme('Avatar', 2022, 160)

avatar.dar_like()
avatar.dar_like()
avatar.dar_like()
avatar.dar_like()
arcane.dar_like()
arcane.dar_like()
arcane.dar_like()
x.dar_like()
x.dar_like()

filmes_e_series = [arcane, x, avatar]
para_assistir = Playlist('para_assistir', filmes_e_series)

for programa in para_assistir:
    print(programa)