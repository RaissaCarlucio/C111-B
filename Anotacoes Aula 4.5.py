#print(np.unique(arr2), return_counts=True)

import numpy as np

# Numeros aleatorios
# Tem como gerar numeros aleatorios gerar nas mesmas maquinas? Posso plantar a mesma semente (seed)
# np.random.seed(10)
arr = np.random.randint(10,20,5)  # 5 Números aleatorios de 10 a 20
print(arr)

# Elementos únicos
np.random.seed(5)
arr2 = np.random.randint(0,10,15)
print(arr2)
print(np.unique(arr2)) # Numeros sem ser repetidos e ja ordenados. O 10 nunca aparece
print(set(arr2))
# Entre o unique e o set, o unique é mais rápido devido ao numpy. O set é um recurso do python (ele também faz a implementação sem números repetidos)
# Casting = o set é um conjunto.

# Operações em matrizes
# Slide 19 exercicio 2
np.random.seed()
mtz = np.random.randint(1,11,9).reshape(3,3)
print(mtz)

print(mtz.sum(axis=0)) # Somar as 3 colunas
print(mtz.sum(axis=1 [0])) # Somar a linha 0
print(mtz.mean(axis=0 [1])) # A media dos valores da coluna do meio.

# Broadcasting = transmitir. Operação entre um Escalar(número avulso) x Array(vários elementos)
print(mtz*2)


# ----------------------------------------------------

# Conceito de condicional:
# Dessa matriz eu quero extrair apenas os elementos pares:
arr3 = mtz%2==0
print(arr3) # Responde true ou false somente, mas eu quero os valores

arr4 = mtz[mtz%2==0]
print(arr4) # Onde for true, mostra os valores para mim, aonde for false, nao mostre).

# Apenas os elementos que tem os valores maiores que a media da minha matriz:
cond = mtz>mtz.mean()
print(cond) # Resposta em true e false
print(mtz[cond]) # Aonde for true, mostrar. Aonde for false, nao mostrar
print('\n')

# Trabalhando com padrões textuais:
arr5 = np.array(['Giovanni', 'Isaque', 'Luiza', 'Raissa'])
print(np.char.find(arr5, 's')) # Filtrando os nomes que tem a letra s, resposta: [-1,1,3] (Retornou a posição da letra em que esse critério esta), Giovanni e luiza retornaram -1. 
# A posição do nome Isaque e Raissa foi 0 e 3 (Sempre mostra a posição da 1 letra)

arr6 = arr5[np.char.find(arr5, 's') >= 0]
print(arr6)

# Boa prática: Escreva tudo em maiusculo ou tudo em minusculo, mais facil depois para procurar ao fazer a busca