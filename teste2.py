import numpy as np

arr = np.loadtxt('space.csv', delimiter=';',  dtype=str, encoding='utf-8')
# print(arr)

# 5 -
# Selecionar a coluna de nomes das empresas
nomes_empresas = arr[1:, 1]

# Contar quantas vezes cada empresa ocorre
empresas, contagens = np.unique(nomes_empresas, return_counts=True)

# Mostrar as informações
for empresa, num_missoes in zip(empresas, contagens):
    print(f"{empresa}: {num_missoes} missões")