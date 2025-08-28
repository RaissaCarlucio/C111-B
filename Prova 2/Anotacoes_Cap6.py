import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Biblioteca Matplotlib
# Vantagens = permite a criaçao de plots valiosos com poucas linhas de códigos
# É rica em diferentes tipos de gráficos (Pode ser usado ao invés do matlab)


# ------------------------------------------------------

# Plot Simples
x = np.array([1, 2, 3, 4])
# Broadcasting: Pega o escalar e multiplica por todos os elementos do array
y = x*2

# Como deixar o gráfico mais estiloso?
# Etiqueta do X
plt.xlabel('Valores de X: ')
# Etiqueta do Y
plt.ylabel('Valores de Y: ')

# plt.plot(x, y)
# plt.show()

# O = Marcador circular
# -- = Linha tracejada
# b = cor clue
# Linewidth = largura da linha
# Markersize = Tamanho da bolinha
# plt.plot(x,y,'o--b', linewidth = 1, markersize = 5) # Traça o gráfico
# plt.show()


# ------------------------------------------------------

# PERGUNTA DE PROVA:
# Podemos fazer tambem multiplos plots:
x2 = np.array([1, 2, 3, 4])
y2 = x*2
y3 = x*x

plt.xlabel('Valores de X: ')
plt.ylabel('Valores de Y: ')

# r- = Vermelho, normal
# b-- = Azul, tracejado
# plt.plot(x2, y2, 'o-r', x2, y3, 'o--b')
# plt.show()

# ------------------------------------------------------

# Podemos fazer plots multiplos, em gráficos separados:
x3 = np.array([1, 2, 3, 4])
y3 = x*2
y4 = x*x
y5 = x*x*x

plt.xlabel('Valores de X: ')
plt.ylabel('Valores de Y: ')

# plt.subplot = plotagem de multiplos plots, porem cada um em seu plano cartesiano.
# Pode-se criar uma thread que de segundo em segundo os graficos ficam atualizando.

# Localização dos subplots: 1,2 = Matriz de 2, localizado na posição 1
# plt.subplot(1, 3, 1)
# plt.xlabel('Eixo X')
# plt.ylabel('Eixo Y')
# plt.title('Linear')
# plt.plot(x3, y3, 'r-o')

# plt.subplot(1, 3, 2)
# plt.xlabel('Eixo X')
# plt.ylabel('Eixo Y')
# plt.title('Exponencial')
# plt.plot(x3, y4, 'b--o')

# plt.subplot(1, 3, 3)
# plt.xlabel('Eixo X')
# plt.ylabel('Eixo Y')
# plt.title('Teste')
#plt.plot(x3, y5, 'k--o')

# plt.show()

# ------------------------------------------------------
# Scatter Plot (Grafico de dispersão, espalhar)
df = pd.read_csv('paises.csv', delimiter=';')
# print(df.columns)

# Grafico que mostra os 6 maiores paises do mundo:
# Eixo x = Paises, eixo Y = Area
df2 = df.nlargest(6, 'Area (sq. mi.)')  # n Maiores, 6, nome da coluna
print(df2['Country'])
plt.scatter(x=df2['Country'],
            y=df2['Area (sq. mi.)'],
            s=df2['GDP ($ per capita)']/50)

plt.title("Area dos 6 maiores paises")
plt.xlabel("Pais")
plt.ylabel("Area")

# Podemos utilizar uma terceira dimensao, ou seja, o tamanho das bolinhas.
# Quanto > A renda per capita, > as bolinhas
# A Russia é o maior país em Area, mas o em renda per capita é os UA
#plt.show()


# Bar plot
plt.bar(x=df2['Country'], height=df2['Area (sq. mi.)'], color='green')
plt.show()


