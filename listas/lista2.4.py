import random


class Competidor:
    def __init__(self, nome):
        self.nome = nome
        self.pos = 0

    def atualizar(self):

        self.pos += random.randint(1, 6)

    def getPos(self):
        return self.pos


def corrida():
    competidores = [Competidor("Competidor 1"), Competidor("Competidor 2"), Competidor("Competidor 3"),
                    Competidor("Competidor 4"), Competidor("Competidor 5")]

    rodadas = 0

    while True:
        rodadas += 1
        print(f"Rodada {rodadas}:")

        for competidor in competidores:
            competidor.atualizar()
            print(f"{competidor.nome} está na posição {competidor.getPos()}")

        vencedores = [
            competidor for competidor in competidores if competidor.getPos() >= 20]

        if vencedores:
            print(f"\nVencedor(es):")
            for vencedor in vencedores:
                print(f"{vencedor.nome} chegou na posição {vencedor.getPos()}!")
            break

        if rodadas >= 100:
            print("\nNinguém chegou à posição final. A corrida terminou em empate.")
            break


if __name__ == "__main__":
    corrida()
