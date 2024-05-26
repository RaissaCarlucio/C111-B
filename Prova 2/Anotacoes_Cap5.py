#file - settings - nome do projeto - python interpreter - + - Pandas
#(Isso no Python, Pycharm)

import numpy as np
import pandas as pd

# O Numpy os indices sao explicitamente, numericos. No Pandas, os indices sao customizaveis.
# Qual estrutura usa chave-valor? Dicionario.

# SERIES (1D)
dic = {'a': 10,
       'b': 20,
       'c': 30}

s1 = pd.Series(dic)
#print(s1)
#print(type(s1))

# Posso criar tambem 2 listas, 1 com as chaves: a,b,c e outra com os valores e passar para o pandaSeries
# O Pandas eu consigo guardar dados heterogenios. Mais flexibilidade para uso.
# Qual a vantagem de dados homogenios? Otimização.

s2 = pd.Series(data=[20,30,40],
               index=['a', 'b', 'd'])
#print(s1+s2) # A resposta de c e d vai ser: NaN pois nao consegue somar C com nada. Os elementos tem que existir em ambas as series.
# Como faço para somar o nada como se fosse zero?

print()
#print(s1.add(s2, fill_value=0)) # Todos os lugares que estiverem vazio = 0.

#print(s1['b'])
#print(s1[['b', 'c']]) # Para acessar multiplos elementos, devo usar com 2 colchetes.
#print(s1[s1 > s1.mean()]) # Quais elementos de S1, sao maiores que a média de s1?

# --------------------------------------------------------------------- #
# DATAFRAMES (2D)
# Precisa-se enviar 2 indices e 1 valor. É uma planilha do excel só que no Python praticamente.

df1 = pd.DataFrame(
       index = ['A', 'B', 'C', 'D'], # Linhas
       colums = ['X', 'Y', 'Z'], # Colunas
       data = np.random.randint(1,50, [4,3]) # Numeros de 1 a 40, de 4 linhas e 3 colunas.
)

#print(df1)

# Qual a vantagem? Se eu tenho uma planilha no excel e quero trazer para o python, se usa 1 função.

# Slicing com loc:
#print(df1.loc[['B', 'C'], ['X', 'Y', 'Z']]) # Estou localizando apenas as linhas B e C, com as colunas X,Y e Z
#print(df1.loc[['B', 'C'], :]) # Tambem funciona assim


#Slicing com iloc:
#print(df1.iloc[[1:3, :]) # Mesma coisa que no de cima, mas com o iloc.

# Adicionar e remover colunas são poucos usados. Existem mas não se é muito utilizado.

# Para carregar um arquivo em excel, temos como por exemplo:

dfPaises = pd.read_csv('paises.csv', delimiter = ';')
#print(dfPaises)
#print(df.columns)
#print(df['Country'])
#print(df.head(5)) # Mostra os primeiros registros do dataset
#print(df.tail(2)) # Os dois ultimos registros do dataset