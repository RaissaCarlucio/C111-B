import numpy as np

# 1 - Crie um array de floats com 10 elementos positivos e negativos entre 0 e 1. Em seguida, multiplique seus valores por 100 e crie um novo vetor apenas com a parte inteira destes numeros; (use seed(5) antes)
np.random.seed(5)
arr1 = np.random.rand(10) # 10 Numeros aleatorios 
arr1 = arr1*100
arr1 = np.array(arr1, dtype=np.int64)
print("Novo vetor: ", arr1)

print("\n")

# 2 - Crie uma matriz de tamanho 4x4 formada por numeros aleatorios inteiros entre 1 e 50; (use seed(10) antes)
np.random.seed(10)
mtz = np.random.randint(1, 50, 16).reshape(4, 4)
print("Matris exercicio2: ", mtz)

print("\n")


# 3 - Mostre o resultado da media de cada linha e cada coluna da matriz gerada pela questao 2, e em seguida, apresente o maior valor das medias para as linhas e tambem para as colunas;
media_linhas = np.mean(mtz, axis=1)
media_colunas = np.mean(mtz, axis=0)

print("Media das linhas: ", media_linhas)
print("Media das colunas: ", media_colunas)

print("Maior valor das medias nas linhas: ", np.max(media_linhas))
print("Maior valor das medias nas colunas: ", np.max(media_colunas))


print("\n")

# 4 - Baseado na matriz gerada na questao 2, mostre a quantidade de aporicoes de cada um dos numeros na mesma. Em seguida, mostre apenas os numeros que aparecem 2 vezes.
arr3 = np.unique(mtz, return_counts=True)
arr3 = np.array(arr3)
print("Mostrando a matriz: ", arr3)


for i in range(arr3.shape[1]):
    print("%d : %d" % (arr3[0][i], arr3[1][i]))

for i in range(arr3.shape[1]):
    if arr3[1][i] == 2:
        print(arr3[0][i])
