#Coleções 19/02/2024
#Tupla coisas colocadas dentro do ()

nomes = ('Goku', 'Vegeta', 'Trunks', 'Gohan')
print(nomes)
#nomes[0] = 'Picolo' #Tentei colocar o Picolo no lugar do Goku, mas deu erro.


#Objetos do tipo Tupla são coleções imutáveis, não se consegue mudar depois de criada.
#Ela não permite adicionar, retirar ou fazer updates dos elementos, fazer somente o select.
#Utilidade: Constantes, programação que não quer que mude. Ex: Escolher os estados brasileiros.


#Slicing:"Picotar"
print(nomes[0])
print(nomes[:2]) #Qualquer coisa do inicio até o Trunks
print(nomes[1:3])#Pegar apenas o Vegeta e o Trunks. Pq colocou o 3? Pois o intervalo é aberto, nao pega o 3
#O Python lê índice negativo. Ex: Como pegar o Trunks mas andando de trás para frente?
print(nomes[-2]) #Ler de trás para frente. Gohan = -1, Trunks = -2

#--------------------------------------------------------------------------#
#Listas
##Saber a posição da lista: index
##Coleção absolutamente mutável
#Guarda seus elementos dentro de []
#Da para ordenar, adicionar, remover, alterar
lista = ['Goku', 'Vegeta', 'Trunks', 'Gohan']

#Adicionar:
lista.append('Picolo')

#Update:
lista[0] = 'Bulma'

#Delete:
lista.remove('Trunks') #Remoção por valor
del lista[1] #remoção por índice

#Select
print(lista)

#--------------------------------------------------------------------------#
#Conjuntos {}
#Ao printar o conjunto, ele printa os valores de forma aleatória, conjunto de matemática
#Ele não guarda elementos repetidos.
conj = {'Goku', 'Vegeta', 'Trunks', 'Gohan'}
print(conj)

#Add elementos:
conj.add('Bulma')
conj.add('Goku') #Não repete esse elemento.
print(conj)

#Remover elementos:
conj.remove('Trunks')

#Update(Não tem)

#Utilidade: União, Interseção, Apenas nomes de brasileiros únicos(pegar o dataset e jogar no conjunto).
#O quão custosa é essa operação? Quando a operação é muito grande, o Python não aguenta. Ai teria que
#usar uma biblioteca para conseguir. Codamos em Python mas o backend é em C++, jogar na biblioteca
#Pandas.

#--------------------------------------------------------------------------#
#Dicionário {}
#É uma coleção mutável
#Usa indices customizáveis.
pessoa1 = {
    'nome': 'Goku', 
    'idade':42
}

pessoa2 = {
    'nome': 'Bulma',
    'idade': 32
}

#ADD
pessoa1['sexo'] = 'M'

#Deletar:
del pessoa1['idade']

#Update
pessoa1['nome'] = 'Gohan'

#Coleção dentro de coleção:
pessoas = [pessoa1, pessoa2] #Lista de Dicionarios
print(pessoas[0]['nome']) #Acessando o pessoa1 e seu nome dentro da lista pessoas
print(pessoas[0]) #Mostrando todas as informações do dicionario pessoa1