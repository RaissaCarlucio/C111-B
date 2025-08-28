import pandas as pd

# 1 -
dfPaises = pd.read_csv('paises.csv', delimiter = ';')

paises_OC = dfPaises[dfPaises['Region'].str.contains("OCEANIA", case = False)]
#print(paises_OC['Country'])
qtd_paises = paises_OC.shape[0]
#print(qtd_paises)

# 2 -
media = dfPaises['Literacy (%)'].mean()
#print(f"{media:.2f}")

# 3 -
indice_pais = dfPaises['Population'].idxmax()
nome_pais_id_max = dfPaises.loc[indice_pais, 'Country']
regiao_pais = dfPaises.loc[indice_pais, 'Region']
#print(nome_pais_id_max)
#print(regiao_pais)

#4 - 
nao_possui = dfPaises[dfPaises['Coastline (coast/area ratio)'] == 0]['Country']
df_sem = pd.DataFrame({'Country': nao_possui})
df_sem.to_csv('NoCosta.csv', index = False)



