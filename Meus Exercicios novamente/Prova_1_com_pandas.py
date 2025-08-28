import pandas as pd

df = pd.read_csv(
    'C:/Users/usuario/Desktop/C111-B/Prova 1/brands.csv', delimiter=';')

# 2 - Mostre o nome de todas as marcas que comecam com a letra 'A'. Em seguida,
# ordene o resultado em ordem alfabetica.
marcas = df[df["Brand"].str.startswith('A')]
# print(marcas)

marcas_ordenadas = marcas.sort_values(by='Brand')
# print(marcas_ordenadas)

# 3 - Mostre a porcentagem de empresas deste Dataset que sao dos Estados Unidos

total_empresas = len(df)
eua = df[df['Country'].str.contains('United States', case=False)]
eua_contagem = eua.shape[0]
# print(eua_contagem)

porcentagem = (eua_contagem/total_empresas)*100
# print(f"{porcentagem:.2f}")

# 4 - Faca um Slicing no dataset e extraia apenas as colunas "Nome da marca", por quem foi fundada
# e o ano que ela foi fundada. Em seguida, mostre apenas o nome das empresas fundadas depois dos anos 2000
# Extrair apenas as colunas desejadas: "Nome da marca", "Por quem foi fundada" e "Ano em que foi fundada"
df_sliced = df[['Brand', 'Founded By/How it was founded', 'Founded In']]
# print(df_sliced)

empresas_fundadas_depois_2000 = df_sliced[df_sliced['Founded In'] > 2000]
print(empresas_fundadas_depois_2000['Brand'].tolist())

# 5 - Busque os diferentes anos em que as empresas foram fundadas.
# Em seguida, mostre em qual ano mais empresas abriram portas
empresas_anos_diff = df['Founded In'].nunique()
#print(empresas_anos_diff)

indice = df['Founded In'].value_counts().idxmax()
print(indice)


#ontagem_empresas_por_ano = df['Founded In'].value_counts()

#ano_mais_empresas = contagem_empresas_por_ano.idxmax()
#numero_empresas_mais_empresas = contagem_empresas_por_ano.max()
#print(ano_mais_empresas)
#print(numero_empresas_mais_empresas)
