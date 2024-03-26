<<<<<<< HEAD
# Numpy
# Numpy tem: Numpy Array(Ndarray). Qual a relação do Numpy array com o que a gente viu na aula 1?
# As vezes pegamos o conjunto de dados na tupla e usamos no NumpyArray(tem otimização)

import numpy as np

# Criando um Numpy Array:
# 1 Dimensão
arr = np.array([1,2,3,4])
print(arr)
print(type(arr)) # Importante pois vizualiza o que o python entendeu dos dados que estamos puxando.
# Resposta: <class 'numpy.ndarray'>

# 2 Dimensões
# Passando uma lista de listas. Pq? Pois uma lista mais externa é da matriz, as internas são das linhas da matriz
mtz = np.array([[1,2], [3,4]])
print(mtz)

# NumpyArray guarda somente coleções do mesmo tipo. Mas as listas consegue colocar String, float, que ele printa.
# Pq? Para facilitar a análise e para o melhor desempenho em operações sobre seus elementos e menor uso de memória.

# Estruturando Numpy Arrays Automaticamente
# ones
mtz1 = np.ones(9).reshape(3,3)
print(mtz1) # Vetor de 9 uns, em 2 dimensões 3 por 3. Se for 2 por 2 o reshape nao roda, pois sao 9 elementos e 2,2 são somente 4

# Zeros

# Arange
mtz2 = np.arange(9) # Printando elementos de 0 até 8
print(mtz2) # [0,1,2,3,4,5,6,7,8]

mtz3 = np.arange(10,20,2) # Arange de 10 até 20 pulando de 2 em 2
print(mtz3)

# Operações elemento a elemento
arr1 = np.arrange(10,20,1)
arr2 = np.arrange(30,40,1)

print(arr1)
print(arr2)
print(arr1+arr2)
print(np.concatenate([arr1, arr2])) # Passar uma coleção de Arrays. Nesse caso estamos usando uma lista.

# Propriedades de um Numpy Array
print(arr1.size) # Tamanho de um Numpy Array (quantos elementos tem)
print(arr1.ndim) # Quantas dimensões tem 
=======
# Numpy
# Numpy tem: Numpy Array(Ndarray). Qual a relação do Numpy array com o que a gente viu na aula 1?
# As vezes pegamos o conjunto de dados na tupla e usamos no NumpyArray(tem otimização)

import numpy as np

# Criando um Numpy Array:
# 1 Dimensão
arr = np.array([1,2,3,4])
print(arr)
print(type(arr)) # Importante pois vizualiza o que o python entendeu dos dados que estamos puxando.
# Resposta: <class 'numpy.ndarray'>

# 2 Dimensões
# Passando uma lista de listas. Pq? Pois uma lista mais externa é da matriz, as internas são das linhas da matriz
mtz = np.array([[1,2], [3,4]])
print(mtz)

# NumpyArray guarda somente coleções do mesmo tipo. Mas as listas consegue colocar String, float, que ele printa.
# Pq? Para facilitar a análise e para o melhor desempenho em operações sobre seus elementos e menor uso de memória.

# Estruturando Numpy Arrays Automaticamente
# ones
mtz1 = np.ones(9).reshape(3,3)
print(mtz1) # Vetor de 9 uns, em 2 dimensões 3 por 3. Se for 2 por 2 o reshape nao roda, pois sao 9 elementos e 2,2 são somente 4

# Zeros

# Arange
mtz2 = np.arange(9) # Printando elementos de 0 até 8
print(mtz2) # [0,1,2,3,4,5,6,7,8]

mtz3 = np.arange(10,20,2) # Arange de 10 até 20 pulando de 2 em 2
print(mtz3)

# Operações elemento a elemento
arr1 = np.arrange(10,20,1)
arr2 = np.arrange(30,40,1)

print(arr1)
print(arr2)
print(arr1+arr2)
print(np.concatenate([arr1, arr2])) # Passar uma coleção de Arrays. Nesse caso estamos usando uma lista.

# Propriedades de um Numpy Array
print(arr1.size) # Tamanho de um Numpy Array (quantos elementos tem)
print(arr1.ndim) # Quantas dimensões tem 
>>>>>>> 0cc721e65873a08d69ebe35463e6d7a47db29280
print(arr1.shape)# Formato da matriz/vetor Resposta: (10,) (10 elementos e 1 linha)