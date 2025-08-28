import numpy as np

arr = np.loadtxt('C:/Users/usuario/Desktop/C111-B/Prova 1/brands.csv',
                 delimiter=';', dtype=str, encoding='utf-8')

# Ex1:
marcas = np.array(arr[1::, 0])
slicing_de_microsoft = arr[np.char.find(marcas, "Microsoft")]
# print(slicing_de_microsoft)

# Ideia inicial: pegar os valores de 2021 e de 2022, somar e depois ver a diferença dos 2, mas como não da de mudar de string para float, vou usar a tabela de change:
# em_2021 = np.array(slicing_de_microsoft[1::, -5])
# em_20211 = em_2021.astype(float)
# print(em_20211)

# Usando a tabela de change:
change = np.array(slicing_de_microsoft[1::, -3])
# print(change)

# Como só printa 20%, irei fazer um unique.
change2 = np.unique(change)
# print(change2)

print("\n")

# Ex2 :
marcas = np.array(arr[1::, 0])
# print(marcas)

# Ordenando em ordem alabetica:
ordem_alfa = np.sort(marcas)
# print(ordem_alfa)

# Nao sei fazer como começr com a letra A professor :/
# No caso eu iria colocar no find, e depois fazer aparecer os nomes que aparecem -1.
começa_com_a_letra_A = np.char.find(ordem_alfa, "_A")
# print(começa_com_a_letra_A)
# print("\n")

# Ex3:
eua = np.array(arr[1::, 3])

x = np.char.find(eua, "United States")
print(x)

contagem = np.size(np.where(x != -1))
print("Empresas que são dos Estados Unidos: ", contagem/100, "%")
# print("\n")

# Ex4:
marcas = np.array(arr[1::, 0])
por_quem_foi_fundada = np.array(arr[1::, 1])
ano_em_que_foi_fundada = np.array(arr[1::, 2])
# print(marcas)
# print(por_quem_foi_fundada)
# print(ano_em_que_foi_fundada)

# Nome das empresas fundadas depois do ano 2000
ano_float = ano_em_que_foi_fundada.astype(float)

# if np.any(ano_float>=2000):
#    print("Ano >= 2000 e por quem foi fundada: ", por_quem_foi_fundada)
# print("\n")

# Ex5:
# Busque os diferentes anos em que as empresas foram fundadas. Em seguida, mostre em qual ano mais empresas abriram as portas.
# ano_em_que_foi_fundada = np.array(arr[1::,2])
# print(ano_em_que_foi_fundada)

diferentes_anos = np.unique(ano_em_que_foi_fundada, return_counts=False)
# print("Anos diferentes: ", diferentes_anos)

# print("\n")
anos_que_mais_aparecem: np.unique(ano_em_que_foi_fundada, return_counts=True)
# print("Anos que mais aparecem: ", ano_em_que_foi_fundada)
