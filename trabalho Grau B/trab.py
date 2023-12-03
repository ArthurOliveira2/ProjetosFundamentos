import csv
import os

class Usuario:
    def __init__(self, nome_usuario, senha, tipo_assinatura='Simples'):
        self.nome_usuario = nome_usuario
        self.senha = senha
        self.tipo_assinatura = tipo_assinatura
        self.lista_perfis = []

        if self.tipo_assinatura == 'Simples':
            self.max_perfis = 3
            self.propagandas = True
            self.custo_mensal = 29.90
        elif self.tipo_assinatura == 'Premium':
            self.max_perfis = 5
            self.propagandas = False
            self.custo_mensal = 49.90

        # Cria diretório para armazenar arquivos CSV se não existir
        if not os.path.exists("usuarios_csv"):
            os.makedirs("usuarios_csv")

    def adicionar_perfil(self, nome, idade):
        if len(self.lista_perfis) < self.max_perfis:
            novo_perfil = {'nome': nome, 'idade': idade}
            self.lista_perfis.append(novo_perfil)
            print(f"Perfil {nome} adicionado com sucesso ao usuário {self.nome_usuario}.")
            self.salvar_para_csv()  # Salva imediatamente ao adicionar um perfil
        else:
            print("Limite máximo de perfis atingido.")

    def remover_perfil(self, nome):
        for perfil in self.lista_perfis:
            if perfil['nome'] == nome:
                self.lista_perfis.remove(perfil)
                print(f"Perfil {nome} removido com sucesso.")
                self.salvar_para_csv()  # Salva imediatamente ao remover um perfil
                return
        print(f"Perfil {nome} não encontrado.")

    def alterar_senha(self, nova_senha):
        self.senha = nova_senha
        print("Senha alterada com sucesso.")
        self.salvar_para_csv()  # Salva imediatamente ao alterar a senha

    def alterar_plano(self, novo_tipo):
        if novo_tipo in ['Simples', 'Premium']:
            self.tipo_assinatura = novo_tipo
            print(f"Plano alterado para {novo_tipo}.")
            self.salvar_para_csv()  # Salva imediatamente ao alterar o plano
        else:
            print("Tipo de assinatura inválido.")

    def salvar_para_csv(self):
        arquivo_csv = f"usuarios_csv/{self.nome_usuario}.csv"
        with open(arquivo_csv, 'w', newline='') as file:
            writer = csv.writer(file)

            # Cabeçalho
            writer.writerow(['Nome de Usuário', 'Senha', 'Tipo de Assinatura', 'Custo Mensal'])
            writer.writerow([self.nome_usuario, self.senha, self.tipo_assinatura, self.custo_mensal])
            writer.writerow([])  # Linha em branco para separar os dados do usuário dos perfis

            # Dados dos perfis
            for perfil in self.lista_perfis:
                writer.writerow(['Nome do Perfil', 'Idade do Perfil'])
                writer.writerow([perfil['nome'], perfil['idade']])

    def carregar_de_csv(self):
        arquivo_csv = f"usuarios_csv/{self.nome_usuario}.csv"
        if os.path.exists(arquivo_csv):
            with open(arquivo_csv, 'r') as file:
                reader = csv.reader(file)
                
                # Ignora cabeçalho
                next(reader, None)
                next(reader, None)
                next(reader, None)

                # Lê os perfis
                for row in reader:
                    if row:
                        nome_perfil, idade_perfil = row[0], row[1]
                        self.lista_perfis.append({'nome': nome_perfil, 'idade': idade_perfil})


class Mídia:
    def __init__(self, tipo, título, gênero, ano_lançamento, classificação):
        self.id = None
        self.tipo = tipo
        self.título = título
        self.gênero = gênero
        self.ano_lançamento = ano_lançamento
        self.classificação = classificação

    def exibir_informações(self):
        print(f"Tipo: {self.tipo}")
        print(f"Título: {self.título}")
        print(f"Gênero: {self.gênero}")
        print(f"Ano de Lançamento: {self.ano_lançamento}")
        print(f"Classificação: {self.classificação}")

class Série(Mídia):
    def __init__(self, título, gênero, ano_lançamento, classificação, num_temporadas):
        super().__init__('Série', título, gênero, ano_lançamento, classificação)
        self.num_temporadas = num_temporadas

    def listar_episodios(self, nro_temporada):
        return self.episodios_por_temporada.get(nro_temporada, [])

class Filme(Mídia):
    def __init__(self, título, gênero, ano_lançamento, classificação, diretor, produtor):
        super().__init__('Filme', título, gênero, ano_lançamento, classificação)
        self.diretor = diretor
        self.produtor = produtor

class Documentário(Mídia):
    def __init__(self, título, gênero, ano_lançamento, classificação, tema):
        super().__init__('Documentário', título, gênero, ano_lançamento, classificação)
        self.tema = tema

class Animação(Mídia):
    def __init__(self, título, gênero, ano_lançamento, classificação, estúdio):
        super().__init__('Animação', título, gênero, ano_lançamento, classificação)
        self.estúdio = estúdio

class ProgramaTV(Mídia):
    def __init__(self, título, gênero, ano_lançamento, classificação, num_episódios):
        super().__init__('Programa de TV', título, gênero, ano_lançamento, classificação)
        self.num_episódios = num_episódios

class Catálogo:
    def __init__(self):
        self.lista_séries = []
        self.lista_filmes = []
        self.lista_documentários = []
        self.lista_animações = []
        self.lista_programas_tv = []
        self.id_counter = 1

    def adicionar_mídia(self, mídia, tipo):
        mídia.id = self.id_counter
        self.id_counter += 1
        if tipo == 'Série':
            self.lista_séries.append(mídia)
        elif tipo == 'Filme':
            self.lista_filmes.append(mídia)
        elif tipo == 'Documentário':
            self.lista_documentários.append(mídia)
        elif tipo == 'Animação':
            self.lista_animações.append(mídia)
        elif tipo == 'Programa de TV':
            self.lista_programas_tv.append(mídia)

    def criar_midia(self, tipo, mídia):
         with open('Catalogo.csv', mode='a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            # Adicione as informações da nova mídia como uma nova linha no arquivo CSV
            writer.writerow([tipo, mídia.título, mídia.gênero, mídia.ano_lançamento, mídia.classificação])
    
    def listar_todas_as_midias(self):
        for tipo in ['Série', 'Filme', 'Documentário', 'Animação', 'Programa de TV']:
            lista_mídias = self.obter_lista(tipo)
            print(f"\nMídias do tipo {tipo}:")
            for mídia in lista_mídias:
                print(f"{mídia.título}")

    def obter_lista(self, tipo):
        if tipo == 'Série':
            return self.lista_séries
        elif tipo == 'Filme':
            return self.lista_filmes
        elif tipo == 'Documentário':
            return self.lista_documentários
        elif tipo == 'Animação':
            return self.lista_animações
        elif tipo == 'Programa de TV':
            return self.lista_programas_tv

    def carregar_dados_csv(self, arquivo_csv):
     with open(arquivo_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            tipo = row['Tipo']
            título = row['Título']
            gênero = row['Gênero']
            ano_lançamento = int(row['Ano'])
            classificação = str(row['Classificação'])

            if tipo == 'Série':
                num_temporadas = int(row['Temporadas'])
                mídia = Série(título, gênero, ano_lançamento, classificação, num_temporadas)
            elif tipo == 'Filme':
                diretor = row['Diretor']
                produtor = row['Produtor']
                mídia = Filme(título, gênero, ano_lançamento, classificação, diretor, produtor)
            elif tipo == 'Documentário':
                tema = row['Tema']
                mídia = Documentário(título, gênero, ano_lançamento, classificação, tema)
            elif tipo == 'Animação':
                estúdio = row['Estúdio']
                mídia = Animação(título, gênero, ano_lançamento, classificação, estúdio)
            elif tipo == 'Programa de TV':
                num_episódios = int(row['Número de episódios'])
                mídia = ProgramaTV(título, gênero, ano_lançamento, classificação, num_episódios)

            self.adicionar_mídia(mídia, tipo)

class Perfil:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.lista_favoritos = []
        self.lista_ultimos_assistidos = []

    def adicionar_favorito(self, mídia):
        if mídia not in self.lista_favoritos:
            self.lista_favoritos.append(mídia)
            print(f"{mídia.título} foi adicionado aos favoritos.")

    def remover_favorito(self, mídia):
        if mídia in self.lista_favoritos:
            self.lista_favoritos.remove(mídia)
            print(f"{mídia.título} foi removido dos favoritos.")

    def adicionar_ultimo_assistido(self, mídia):
        self.lista_ultimos_assistidos = [m for m in self.lista_ultimos_assistidos if m != mídia]
        self.lista_ultimos_assistidos.append(mídia)
        print(f"{mídia.título} foi adicionado aos últimos assistidos.")

    def listar_midias_apropriadas(self, tipo, lista_mídias):
        if self.idade >= 18 or not hasattr(lista_mídias[0], 'classificação'):
            return lista_mídias
        else:
            return [mídia for mídia in lista_mídias if mídia.classificação <= self.idade]

    def assistir(self, mídia):
        print(f"{mídia.título} foi assistido.")
        self.adicionar_ultimo_assistido(mídia)

    def favoritar(self, mídia, adicionar):
        if adicionar:
            self.adicionar_favorito(mídia)
        else:
            self.remover_favorito(mídia)

    def buscar_por_título(self, título, catálogo):
        tipos_mídia = ['Série', 'Filme', 'Documentário', 'Animação', 'Programa de TV']
        for tipo in tipos_mídia:
            lista_mídias = self.listar_midias_apropriadas(tipo, catálogo.obter_lista(tipo))
            for mídia in lista_mídias:
                if mídia.título.lower() == título.lower():
                    return mídia
        return None

# Lista de usuários
usuarios = []
usuario_atual = None

while True:
    print("\n----- Menu Inicial -----")
    print("1. Cadastrar-se")
    print("2. Login")
    print("3. Sair")

    opcao_inicial = input("Escolha uma opção (1-3): ")

    if opcao_inicial == '1':
        nome_usuario = input("Digite o nome de usuário: ")

        # Verifica se o nome de usuário já está cadastrado
        if any(u.nome_usuario == nome_usuario for u in usuarios):
            print("Nome de usuário já cadastrado. Tente novamente.")
            continue

        senha = input("Digite a senha: ")
        tipo_assinatura = input("Digite o tipo de assinatura (Simples ou Premium): ")
        novo_usuario = Usuario(nome_usuario, senha, tipo_assinatura)
        usuarios.append(novo_usuario)
        print("Usuário cadastrado com sucesso!")

        # Salva os dados no CSV
        novo_usuario.salvar_para_csv()

    elif opcao_inicial == '2':
        nome_usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")

        # Verifica se o usuário e senha correspondem
        usuario_atual = next((u for u in usuarios if u.nome_usuario == nome_usuario and u.senha == senha), None)

        if usuario_atual:
            print("Login bem-sucedido!")
            # Carrega os dados do CSV ao fazer login
            usuario_atual.carregar_de_csv()
        else:
            print("Usuário ou senha incorretos. Tente novamente.")

    elif opcao_inicial == '3':
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

    while usuario_atual:
        print("\n----- Menu -----")
        print("1. Adicionar Perfil")
        print("2. Remover Perfil")
        print("3. Alterar Senha")
        print("4. Alterar Plano")
        print("5. Opçoes de catalogo")
        print("6. Sair")

        opcao = input("Escolha uma opção (1-7): ")

        if opcao == '1':
            nome_perfil = input("Digite o nome do perfil: ")
            idade_perfil = input("Digite a idade do perfil: ")
            usuario_atual.adicionar_perfil(nome_perfil, idade_perfil)

        elif opcao == '2':
            nome_perfil = input("Digite o nome do perfil a ser removido: ")
            usuario_atual.remover_perfil(nome_perfil)

        elif opcao == '3':
            nova_senha = input("Digite a nova senha: ")
            usuario_atual.alterar_senha(nova_senha)

        elif opcao == '4':
            novo_plano = input("Digite o novo plano (Simples ou Premium): ")
            usuario_atual.alterar_plano(novo_plano)

        elif opcao == '5':
            catalogo = Catálogo()
            catalogo.carregar_dados_csv('Catalogo.csv')
            print("\n----- Menu de catalogo -----")
            print("1. Listar o catalogo")
            print("2. Adicionar midia")
            print("3. Sair")
            opcaocatalogo = input('Digite uma opção:')

            if opcaocatalogo == '1':
             catalogo.listar_todas_as_midias()
            if opcaocatalogo == '2':
             tipo = input('Digite o tipo a ser adicionado:')
             título = input('Digite o título a ser adicionado:')
             gênero = input('Digite o gênero a ser adicionado:')
             ano_lançamento = input('Digite o ano_lançamento a ser adicionado:')
             classificação = input('Digite o classificação a ser adicionado:')

             if tipo == 'Serie':
                num_temporadas = input('Digite o num de temporadas a ser adicionado:')
                mídia = Série(título, gênero, ano_lançamento, classificação, num_temporadas)
                catalogo.criar_midia(tipo,mídia)
                print('Adicionado com sucesso')

             elif tipo == 'Filme':
                diretor = input('Digite o diretor a ser adicionado:')
                produtor = input('Digite o produtor a ser adicionado:')
                mídia = Filme(título, gênero, ano_lançamento, classificação, diretor, produtor)
                catalogo.criar_midia(tipo,mídia)
                print('Adicionado com sucesso')

             elif tipo == 'Documentário':
                tema = input('Digite o tema a ser adicionado:')
                mídia = Documentário(título, gênero, ano_lançamento, classificação, tema)
                catalogo.criar_midia(tipo,mídia)
                print('Adicionado com sucesso')

             elif tipo == 'Animação':
                estúdio = input('Digite o estúdio a ser adicionado:')
                mídia = Animação(título, gênero, ano_lançamento, classificação, estúdio)
                catalogo.criar_midia(tipo,mídia)
                print('Adicionado com sucesso')

             elif tipo == 'Programa de TV':
                num_episódios = input('Digite o num_episódios a ser adicionado:')
                mídia = ProgramaTV(título, gênero, ano_lançamento, classificação, num_episódios)
                catalogo.criar_midia(tipo,mídia)
                print('Adicionado com sucesso')


        elif opcao == '6':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
