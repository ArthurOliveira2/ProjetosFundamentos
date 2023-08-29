nome = input("digite o nome: ")
idade = input("Digite a idade: ")
escola = input("Digite o nome da escola: ")
elemento = input("Selecione o seu elemento entre fogo, água, terra e ar: ")
Mestre = input("Qual o nome do seu Mestre? ")


class Mago:
    # Atributos de classe
    possuiMagia = True
    # Método construtor

    def __init__(self, nome, idade, escola, elemento, Mestre):
        # Atributos de instância
        self.nome = nome
        self.idade = idade
        self.escola = escola
        # Os dois atributos adicionados
        self.elemento = elemento
        self.mestre = Mestre
        print('Mago', nome + ",", idade, "anos", "vindo de", escola, 'foi criado!',
              "Seu elemento principal é", elemento, "e seu Mestre se chama", Mestre + "!")

    def andar(self):
        print('Estou andando')

    def falar(self):
        print('Ola amigue! Meu nome é ', self.nome)

        # Os objetos adicionados
    def invocarMagiaFogo(self):
        print('Invocando bola de fogo!')

    def invocarMagiaTerra(self):
        print('Invocando parede de lama!')

    def invocarMagiaAgua(self):
        print('Invocando escudo de água!')

    def invocarMagiaAr(self):
        print('Invocando lâminas de vento!')

    # Método destrutor
    def tirar(self):
        print("Deixou de existir!")


mago_instance = Mago(nome.capitalize(), idade, escola.capitalize(
), elemento.capitalize(), Mestre.capitalize())
