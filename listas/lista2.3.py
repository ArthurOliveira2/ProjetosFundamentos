class CadastroCliente:
    def __init__(self, nome, sobrenome, data_nascimento, email, cpf, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.email = email
        self.cpf = cpf
        self.senha = senha
        self.tentativas_falhas = 0
        self.bloqueado = False

    def login(self, email, senha):
        if not self.bloqueado:
            if self.email == email and self.senha == senha:
                return True
            else:
                self.tentativas_falhas += 1
                if self.tentativas_falhas >= 3:
                    self.bloqueado = True
                return False
        else:
            print("Conta bloqueada devido a múltiplas tentativas de senha incorreta.")

    def consultar_dados(self):
        if not self.bloqueado:
            print("Nome:", self.nome)
            print("Sobrenome:", self.sobrenome)
            print("Data de Nascimento:", self.data_nascimento)
            print("Email:", self.email)
            print("CPF:", self.cpf)
        else:
            print("Conta bloqueada devido a múltiplas tentativas de senha incorreta.")


cliente1 = CadastroCliente("João", "Silva", "01/01/1990", "joao@email.com", "12345678901", "senha123")

# Cadastro e consulta
email = input("Email: ")
senha = input("Senha: ")

if cliente1.login(email, senha):
    cliente1.consultar_dados()
else:
    print("Erro no login. Por favor, verifique suas credenciais.")