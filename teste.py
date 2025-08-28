import numpy as np

# Numpy tem maior desempenho em operacoes e usa pouca memoria

arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
#           Linha 0 Linha 1 Linha 2 Linha 3
# Coluna 0
# Coluna 1
# Coluna 2
# print(arr1[1][2]) # 7

arr2 = np.zeros(3)
# print(arr2) # [0. 0. 0.]

arr3 = np.ones(3)
# print(arr3) # [1. 1. 1.]

arr4 = np.arange(4)
# print(arr4) # [0 1 2 3]

arr5 = np.arange(0, 10, 2)
# print(arr5) # [0 2 4 6 8] - Arr de 0 a 10 pulando de 2 em 2

# Valores de 0 a 10 igualmente espacados, 5 numeros
arr6 = np.linspace(0, 10, 5)
# print(arr6) # [ 0.   2.5  5.   7.5 10. ]

arr7 = np.array([2, 1, 5, 7, 3, 8, 9, 11, 20])
# print(np.sort(arr7)) # [ 1  2  3  5  7  8  9 11 20] Ordem crescente
# print(np.flip(np.sort(arr7))) # [20 11  9  8  7  5  3  2  1] Ordem decrescente

arr8 = np.array([1, 2, 3, 4])
arr9 = np.array([5, 6, 7, 8])
# print(np.concatenate((arr8, arr9))) # [1 2 3 4 5 6 7 8]
# print(arr8.size) # 4
# print(arr8.ndim) # 1 Retorna o numero de dimensoes de um Array
# print(arr8.shape) # (4,) Retorna uma tupla de inteiros que indica o numero de elementos armazenados em cada dimensao do Array

arr10 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(arr10.shape) # (3, 4)

arr11 = np.array([1, 2, 3, 4, 5, 6])
# print(arr11.reshape(3,2)) # Remodelando para 3 colunas e 2 linhas
# [[1 2]
# [3 4]
# [5 6]]

# --------------------------------------------------------------------------------------------------------------------------------------
# Parte 4.5
np.random.seed(5)
a1 = np.array([1, 2, 3, 4, 5])
# print(np.random.rand(5)) # Numeros aleatorios (float) entre 0 e 1
#print(np.random.rand(3,2)) # Gera numeros aleatorios entre 0 e 1 de 3 dimendoes, cada uma tendo 2 numeros
print(np.random.randn(3)) # Numeros aleatorios (Incluindo negativos)
# print(np.random.randint(1,10,5)) # Gera 5 numeros aleatorios entre 1 e 10
np.random.shuffle(a1)
# print(a1) # Embaralha os valores
# Gerar 10 números aleatórios de ponto flutuante entre 0 e 1
a1 = np.random.uniform(0, 1, 10)
print(a1)

a2 = np.array([1, 1, 5, 3, 7, 4, 8, 8])
# print(np.unique(a2)) # Printa somente elementos unicos, sem repeticao
# print(np.unique(a2, return_index=True)) # Retorna o indice dos primeiros elementos unicos que aparecem no Array
# print(np.unique(a2, return_counts=True))

a3 = np.array([1, 2, 3, 4])
a4 = np.array([5, 6, 7, 8])
# print(a3 + a4)
# print(a3.sum())

# Lembrando outras funcoes fundamentais:
# min() max() -> Pega o menor e maior valor
# argim() e argmax() -> Pega o indice do menor e maior valor
# mean() -> Faz a media
# astype(int) -> pega apenas a parte inteira de um float


a5 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(a5.sum(axis=0)) # Eixo 0 = Aplica uma operacao sobre as colunas do array
# print(a5.sum(axis=1)) # Eixo 1 = Aplica uma operacao sobre as linhas do array
# print(a5.sum(axis=0)[1])
# print(a5/5)

a6 = np.array([1, 2, 3, 4])
# print(5*a6)

# --------------------------------------------------------------------------------------------------------------------------------------
# Parte 4.6
arr21 = np.array([2, 1, 5, 3, 7, 4, 6, 8])
#print(arr21[arr21 <= 5]) # Numeros menores ou iguais a 5
#print(arr21[arr21%2==0])
#print(arr21>5)
# print(arr21[0:2])
# print(arr21[-2:])
arr22 = arr21[4:].copy()

mtz2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(mtz2[2])


#np.char.find(arr,sub) # Para cada elemento do array, retorna o indice
# em que a substring aparece (retorna -1 para textos onde a substring nao aparece)

#np.char.startswith(arr,sub) # Retorna True para cada elemento do array iniciado por uma 
# Substring especifica

#np.char.upper(arr) # Retorna um array com os textos colocados em letras maiusculas

#np.char.isalpha(arr) # Retorna True para cada texto do array formado apenas por letras






