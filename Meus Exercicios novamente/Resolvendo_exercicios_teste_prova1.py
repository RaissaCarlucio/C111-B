import numpy as np
import pandas as pd

# -------------------- Prova 1 --------------------
# 1 - Mostre o quanto ($) a empresa Microsoft valorizou de 2021 para 2022
arr = np.loadtxt('C:/Users/usuario/Desktop/C111-B/Prova 1/brands.csv',
                 delimiter=';', dtype=str, encoding='utf-8')
arr = arr[1:]

microsoft = np.where(arr[::, 0] == 'Microsoft')
microsoft_2 = arr[microsoft]
#print(microsoft_2)
#print("\n")
microsoft_3 = np.array(microsoft_2[0])
#print(microsoft_3)

# Brand_value de 2021 e 2022 (9 e 10)
brand_value_2022 = float(microsoft_3[9])
brand_value_2021 = float(microsoft_3[10])

Valor_Total = (brand_value_2022 - brand_value_2021)

#print(f"Valor valorizado: {Valor_Total:.2f}")

# 2 - Mostre o nome de todas as marcas que comecam com a letra 'A'. Em seguida, 
# ordene o resultado em ordem alfabetica.

marcas = np.array(arr[1::,0])

letra_A = np.char.startswith(marcas, "A") # True
marcas_com_A = marcas[letra_A]
#print(marcas_com_A)
ordenando = np.sort(marcas_com_A)
#print(ordenando)

# 3 - Mostre a porcentagem de empresas deste Dataset que sao dos Estados Unidos
eua = np.where(arr[::, 3]== "United States")
eua = arr[eua]
#print(eua)
num_total = len(arr)
eua_total = len(eua)
#print((eua_total/num_total)*100)

# 4 - Faca um Slicing no dataset e extraia apenas as colunas "Nome da marca", por quem foi fundada
# e o ano que ela foi fundada. Em seguida, mostre apenas o nome das empresas fundadas depois dos anos 2000
# Extrair apenas as colunas desejadas: "Nome da marca", "Por quem foi fundada" e "Ano em que foi fundada"
marcas = np.array(arr[1::, 0])
por_quem_fundada = np.array(arr[1::, 1])
ano_que_foi_fundada = np.array(arr[1::,2])

# Transformar astype
ano_que_foi_fundada = ano_que_foi_fundada.astype(int)

# Nome das empresas fundadas depois do ano 2000:
empresas_apos_2000 = marcas[ano_que_foi_fundada>2000]
print(empresas_apos_2000)

# 5 - Busque os diferentes anos em que as empresas foram fundadas. 
# Em seguida, mostre em qual ano mais empresas abriram portas.
ano_que_foi_fundada = np.array(arr[1::,2])
ano_que_foi_fundada = ano_que_foi_fundada.astype(int)
diferentes_anos = np.unique(ano_que_foi_fundada)
#print(diferentes_anos)

ano_mais_empresas = np.argmax(np.bincount(diferentes_anos))
print(ano_mais_empresas)















