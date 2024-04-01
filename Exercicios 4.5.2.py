import numpy as np

arr = np.loadtxt('C:/Users/usuario/Desktop/C111-B/space.csv', delimiter = ';', dtype = str, encoding = 'utf-8')

# # Obter o cabeçalho do arquivo CSV (nomes das colunas)
# header = arr[0]
#
# print("Nomes das colunas:")
# for i, column_name in enumerate(header):
#     print(f"{i}: {column_name}")

# 1 - Apresente a porcentagem de quantas missoes deram certo;

status_mission = arr[1:, -1]
print("Verificando: ", status_mission) # extraindo a coluna status mission

# Contar o numero total de missoes:
total_de_missoes = np.size(status_mission) # Tamanho da coluna Status_Mission
print("Total de missoes: ", total_de_missoes)

missoes_sucessidas = np.count_nonzero(status_mission=="Success")
print("Porcentagem das missoes bem sucessidas: ", ((missoes_sucessidas/total_de_missoes)*100), "%")

print("\n")

# 2 - Qual a media de gastos de uma missao espacial se baseando em missoes que possuam valores disponiveis(>0)? (CUSTOS)
cost_column = arr[1:, 6]
print(cost_column)

# Convertendo os valores para float
cost_values = cost_column.astype(float)

if np.any(cost_values>0):
    cost_media = np.mean(cost_values)
    print(f"A média é: ", cost_media)

print("\n")


# 3 - Encontre quantas missoes espaciais neste DataSet foram realizadas pelos Estados Unidos (USA);
qtd_missoes = arr[1:, 2]
print(qtd_missoes)

qtd_missoes = np.char.find(qtd_missoes, 'USA')
print("Quantidade de missoes que aparecem USA: ", qtd_missoes)

num_ocorrencias = np.size(np.where(qtd_missoes!=-1))

print("Número total de ocorrências de 'USA':", num_ocorrencias)

print("\n")

# 4 - Encontre qual foi a missao mais cara realizada pela Empresa "SpaceX"
cost_column = arr[1:, 6]
print(cost_column)

# Convertendo os valores para float
cost_caro = cost_column.astype(float)

mais_cara = np.max(cost_caro)

print("Missao mais cara custa: ", mais_cara)


print("\n")

# 5 - Mostre o nome das empresas que ja realizaram Missoes Espacieias juntamente com suas respectivas quantidades de missoes(use o for no final para mostrar as informacoes)
nome_das_empresas = arr[1:, 1]
status_mission = arr[1:, -1]

# Inicializar um dicionário para armazenar o número de missões bem-sucedidas para cada empresa
qtd_missoes_por_empresa = {}

# Iterar sobre as empresas e status da missão
for empresa, status in zip(nome_das_empresas, status_mission):
    if status == 'Success':
        if empresa in qtd_missoes_por_empresa:
            qtd_missoes_por_empresa[empresa] += 1
        else:
            qtd_missoes_por_empresa[empresa] = 1

for empresa, qtd_missoes in qtd_missoes_por_empresa.items():
    print(f"A empresa {empresa} realizou {qtd_missoes} missões espaciais com sucesso.")

