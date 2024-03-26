import numpy as np

# Crie um Array de tamanho 21 com valores linearmente espaçados entre 0 e 1;
arr1 = np.arange(0, 1, 21)  # Missões do 1 ao 8
print("Ex1: ", arr1)
print("\n")

print("Ex2: ")
# Crie dois Arrays: um de números pares de 0 até 51 e outro também de número pares de 100 até 50. Em seguida os concatene e mostre os resultados ordenados:
arr2 = np.arange(0, 51, 2)
print("Ex2.1: ", arr2)

arr21 = np.arange(100, 48, -2)
print("Ex3.2: ", arr21)

arr22 = np.concatenate((arr2,arr21))

print("Concatenando arr2 com arr21: ", np.concatenate((arr2,arr22)))

print("\n")
print("Ex3: ")
# Ordene os resultados dos array resultante da Questao 2 em ordem decrescente:
arr3 = np.flip(np.sort(arr22))
print("Em ordem decrescente: ", arr3)


print("\n")
print("Ex4: ")
# Crie uma matriz formada somente por uns tamanho 3x4. Em seguida, transforme-a em um Array 1-D;
mtz4 = np.array([[1,2,3,4], [4,5,6,7], [7,8,9,10]])
print(mtz4)

print("Número de dimensões antes: ", mtz4.ndim)

mtz4 = mtz4.reshape(-1)

print("Transformando em matriz de 1D: ", mtz4)
print("Número de dimensões depois: ", mtz4.ndim)

print("\n")
print("Ex5: ")

# Crie uma matriz de tamanho qualquer. Extraia seu número de linhas e colunas, multiplique-os, e diga se esta matriz poderia se tornar um vetor com número par ou ímpar de elementos.
mtz5 = np.array([[1,2,3,4], [4,5,6,7], [7,8,9,10]])
print("Matriz: ", mtz5)
print("Número de linhas e colunas da matriz: ", mtz5.shape)
l, c = mtz5.shape

# Multiplique o número de linhas pelo número de colunas
total_elementos = l * c

if total_elementos % 2 == 0:
    print("A matriz pode ser convertida em um vetor com um número par de elementos.")
else:
    print("A matriz pode ser convertida em um vetor com um número ímpar de elementos.")