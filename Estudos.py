# Capitulo 3

# TUplas: sao variaveis imutaveis, nao podem ter seus valores alterados.
# Consigo colocar elementos misturados.

nomes = ("Goku", "Vegeta", "Trunks", "Gohan")
# print(nomes)
# print(nomes[1])
# print(nomes[-1])
# print(nomes[1:3]) # Python se conta como o menos significativo. Entao nesse caso o Vegeta e o 1, o Trunks o 2 e o Gohan o 3. Mas como ele conta como -1, vai parar no Trunks.
# print(nomes[:2])
# print(len(nomes))

# print("Contando de 0 ate o numero maximo de personagens do Dragon Ball: ")
# for cont in range(0,len(nomes)):
#     print(cont)

# print("Enumerando os indices: ")
# for pos,nomes in enumerate(nomes):
#     print(f'Nome {nomes}: {pos}')    

nomes2 = ("Teste", 10, "Adrian", 5.0)
# print(nomes2)    

x = (2,3,4)
y = (5,6,7)
z = x+y
# print(z)

# print(z.count(2)) # Uma ocorrencia do numero 2
# print(max(z))
# print("\n")

# ------------------------------- #
# Listas:
# Seus valores podem ser mudados ao contrario das tuplas.
lista1 = ["Goku", "Vegeta", "Trunks", "Gohan"]
lista1.append("Bulma")
print(lista1) # Adicionando a Bulma na lista.

lista1.insert(0, "Kuririn") # Adiciona o Kuririn na posicao 0.
print(lista1)
lista1.remove("Vegeta")
print(lista1)

# Verificando:
if "Goku" in lista1:
    lista1.remove("Goku")
    print(lista1)
else:
    print("Personagem nao encontrado")    
print("\n")

# ------------------------------- #
# Conjuntos: colecao nao ordenada e que nao admite elementos duplicados. {}
conj = {"Goku", "Vegeta", "Gohan", "Trunks", "Goku"}
print(conj)
 
a = {2,4,6}
b = {1,4,5}
print(a|b)

print("\n")
# Dicionarios: {}

dados = {'nome': "Goku", 
        'idade': 23}
print(dados["nome"])
print(dados["idade"])

dados["sexo"] = "M"
print(dados)

print(dados.values())
print(dados.keys())
print(dados.items())















