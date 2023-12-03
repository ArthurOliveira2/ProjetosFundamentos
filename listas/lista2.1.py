import random

class Dado:
    def __init__(self, num_faces):
        self.num_faces = num_faces

    def rolar(self):
        return random.randint(1, self.num_faces)

def main():
    dados = [Dado(6), Dado(8), Dado(12)]

    for dado in dados:
        print(f"Jogando o dado de {dado.num_faces} faces 3 vezes:")
        for _ in range(3):
            resultado = dado.rolar()
            print(f"Resultado: {resultado}")
        print()

if __name__ == "__main__":
    main()