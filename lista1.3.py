class Data:
    def __init__(self, dia=1, mes=1, ano=2000):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def imprimirData(self):
        print(f"{self.dia:02d}/{self.mes:02d}/{self.ano}")

    def imprimirDataPorExtenso(self, cidade):
        meses = [
            'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
            'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
        ]
        mes_por_extenso = meses[self.mes - 1]
        print(f"{cidade}, {self.dia} de {mes_por_extenso} de {self.ano}")

# Exemplo de uso:
data1 = Data(18, 10, 2023)
data2 = Data(25, 12, 2023)

data1.imprimirData()
data2.imprimirData()
data1.imprimirDataPorExtenso("São Paulo")
data2.imprimirDataPorExtenso("Rio de Janeiro")