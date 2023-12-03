class Musica:
    def __init__(self, titulo, artista, album, genero):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.genero = genero

    def reproduzir(self):
        print(f"Reproduzindo '{self.titulo}' por {self.artista}")

    def informacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Artista: {self.artista}")
        print(f"Álbum: {self.album}")
        print(f"Gênero: {self.genero}")


# Exemplo de criação de músicas e uma playlist
musica1 = Musica("Levitating", "Dua Lipa", "Future Nostalgia", "Pop")
musica2 = Musica("From the Start", "Laufey", "Single", "Jazz")

playlist = [musica1, musica2]

# Exemplo de uso
for musica in playlist:
    musica.informacoes()
    musica.reproduzir()
    print()
