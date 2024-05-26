import numpy as np
import pandas as pd

# 1 - Carregue o dataset paises.csv. Em seguida, mostre:
# a) Quais os paises da OCEANIA
# b) Quantos paises sao da OCEANIA
# Dica: use do auxilio do metodo contains da classe str

dfPaises = pd.read_csv('paises.csv', delimiter=';')
#print(dfPaises)

#print(dfPaises.columns) # Ocenia = Region

paises_oceania = dfPaises[dfPaises['Region'].str.contains('OCEANIA', case=False)] # Case = False significa que ele encontrara todas as entradas que contem 'oceania', tamto minuscula como maiuscula.
print("Paises que sao da Oceania: ", paises_oceania['Country']) # Mostrando apenas os paises.

paises_soma = paises_oceania.shape[0]
print("Quantidade de paises que sao da Oceania: ", paises_soma)

print("\n")

# 2 - Mostre a media da taxa de alfabetizacao(Literacy(%) do planeta)
# Dica: use do auxilio da funcao mean

media = dfPaises['Literacy (%)'].mean()
print("Media da Literacy: ", media)

print("\n")

# 3 - Encontre o nome e a regiao do pais que possui a maior populacao
# Dica: use do auxilio da funcao max

indice_max_pop = dfPaises['Population'].idxmax() # ID do pais com maxima populacao
print(indice_max_pop)

nome_pais_max_pop = dfPaises.loc[indice_max_pop, 'Country']
regiao_max_pop = dfPaises.loc[indice_max_pop, 'Region']

print("País com a maior população: ", nome_pais_max_pop)
print("Região do país com a maior população: ", regiao_max_pop)

print("\n")

# 4 - Busque o nome de todos os paises do dataset que nao possuem costa maritima(Coastline (coast/area ratio)==0)
# e guarde-os em um novo arquivo chamado noCoast.csv; 
# Dica: apos realizar os filtros, use do auxilio da funcao to_csv

paises_sem_costa_maritima = dfPaises[dfPaises['Coastline (coast/area ratio)'] == 0]['Country']

# Criando um novo DataFrame com os países sem costa
df_sem_costa = pd.DataFrame({'Country': paises_sem_costa_maritima})

# Salvando os nomes dos países sem costa em um novo arquivo chamado "noCoast.csv"
df_sem_costa.to_csv('noCoast.csv', index=False)






