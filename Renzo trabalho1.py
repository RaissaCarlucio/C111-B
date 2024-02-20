#Exercicio 1:
Lista = ['Brasil', 'Alemanha', 'Barcelona', 'Espanha', 'Italia']

#a) 3 primeiros colocados:
print("Os 3 primeiros colocados: ", Lista[:3])

#b) Os últimos 2 colocados:
print("Os 2 ultimos colocados: ", Lista[-2:])

#c)Uma lista com os times em ordem alfabética
ordem_alfabetica = sorted(Lista)
print("Em ordem alfabética: ", ordem_alfabetica)

#d)Em que posição da tabela está o Barcelona
posicao_bar = Lista.index("Barcelona")
print("Posição do Barcelona na Lista: ", posicao_bar)

#Exercicio 2: 
print("\n")
print("--------------------EX2-------------------")

Loja1 = {'Iphone', 'Samsung'}
Loja2 = {'Iphone', 'Xiaomi', 'Motorola'}

print("Loja 1 vende: ", Loja1)
print("Loja 2 vende: ", Loja2)

uniao = Loja1 | Loja2
ambas_lojas = Loja1 & Loja2

print("Nas 2 lojas. você poderá comprar no total: ", uniao)
print("Modelos disponveis em ambas as lojas: ", ambas_lojas)

#Exercicio 3: 
print("\n")
print("--------------------EX3-------------------")

aluno = {
    'nome': 'Raissa',
    'média': 60
}

print('Dados do aluno: ', aluno)

if aluno['média'] >= 60:
    aluno['situação_final'] = 'AP'
else:
    aluno['situação_final'] = 'RP'   
    
print('Situação final do aluno: ', aluno)