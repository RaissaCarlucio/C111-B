import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1 - Por meio do Dataset space.csv, trace um grafico em barras
# mostrando quantas empresas Espaciais os EUA e China possuem
# Dica: Utilize o metodo unique() para retirar os resultados repetidos

df = pd.read_csv('space.csv', delimiter=';')
# print(df.columns)

# USA, China
empresas_USA = df[df['Location'].str.contains("USA", case=False)]
empresas_China = df[df['Location'].str.contains("China", case=False)]

# Contando as empresas únicas dos EUA e da China
qtd_empresas_USA = empresas_USA['Company Name'].nunique()
qtd_empresas_China = empresas_China['Company Name'].nunique()

print("Empresas Espaciais nos EUA:", qtd_empresas_USA)
print("Empresas Espaciais na China:", qtd_empresas_China)


plt.bar(["USA", "China"], [qtd_empresas_USA,
        qtd_empresas_China], color=["blue", "red"])
plt.xlabel('País')
plt.ylabel('Número de Empresas Espaciais')
plt.title('Número de Empresas Espaciais nos EUA e na China')
plt.show()
# ----------------------------------------------------------------------------------------------
# Por meio do Dataset paises.csv, trace dois graficos de linhas em um mesmo plano cartesiano,
# um mostrando a taxa de mortalidade (Deathrate) e outro
# A Taxa de natalidade (Birthrate) dos paises da America do Norte(NORTHERN AMERICA)
dfPaises = pd.read_csv('paises.csv', delimiter=';')
# print(dfPaises.columns)
paises_NA = dfPaises[dfPaises['Region'].str.contains(
    "NORTHERN AMERICA", case=False)]
print(paises_NA['Country'])

x = paises_NA['Country']
y = paises_NA['Birthrate']

y2 = paises_NA['Deathrate']

plt.title("Birthrate and Deathrate")
plt.xlabel("Country")
plt.plot(x, y2, 'o-k')
plt.plot(x, y, 'o-r')
plt.show()
