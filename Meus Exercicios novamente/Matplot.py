import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dfSpace = pd.read_csv('space.csv', delimiter=';')

# Quantas empresas Espaciais os EUA e a China possuem?
# Utilizar unique
# USA, China (Location)
Usa = dfSpace[dfSpace['Location'].str.contains("USA", case=False)]
Usa = Usa.shape[0]

China = dfSpace[dfSpace['Location'].str.contains("China", case=False)]
China = China.shape[0]

# Nao deu certo!!!
# usa_unique = np.unique(Usa)
# usa_unique = usa_unique.astype(int)
# china_unique = np.unique(China)
# china_unique = china_unique.astype(int)

#print("China: ", China)  # Quantidade de empresas que China possui
#print("Usa: ", Usa)  # Quantidade de empresas que EUA possui

# Fazendo o grafico em barras:
countries = ['USA', 'China']
num_companies = [Usa, China]
#plt.bar(countries, num_companies, color=['blue', 'red'])
#plt.xlabel('Pais')
#plt.ylabel('Numero de Empresas')
#plt.title("Numero de Empresas nos Eua e na China")
#plt.show()

# 2 - DataSet paises.csv, trace dois graficos de linhas em um mesmo plano cartesiano, um mostrando
# a taxa de mortalidade (Deathrate) e o outro a 
# Taxa de natalidade(Birthrate) dos paises da Amerida do Norte (NORTHERN AMERICA)


dfPaises = pd.read_csv('paises.csv', delimiter =';')
paises_america_do_norte = dfPaises[dfPaises['Region'].str.contains("NORTHERN AMERICA", case=False)]
deathrate = paises_america_do_norte['Deathrate']
birthrate = paises_america_do_norte['Birthrate']
paises_AM = paises_america_do_norte['Country']

plt.plot(paises_AM, deathrate, 'r-', paises_AM, birthrate, 'b-')
plt.show()

