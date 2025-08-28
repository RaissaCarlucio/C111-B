import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('space.csv', delimiter=';')

"""usa_company = ["NASA", "US Navy", "US Air Force"]
chn_company = ["CASC"]
print(df['Company Name'].unique())
"""
usa_company = df['Location'].apply(lambda x: "USA" in x)
usa_company = df[usa_company]
usa_company = usa_company['Company Name'].unique()

chn_company = df['Location'].apply(lambda x: "China" in x)
chn_company = df[chn_company]
chn_company = chn_company['Company Name'].unique()

n_usa = usa_company.shape[0]
n_chn = chn_company.shape[0]

plt.title("Company Quantities")
plt.bar(['USA', 'China'], [n_usa, n_chn], color='blue')
plt.show()

#Ex2
df = pd.read_csv('paises.csv', delimiter=';')

df2 = df['Region'].str.contains("NORTHERN AMERICA")
df2 = df[df2]

plt.title("Deathrate and Birthrate")
plt.xlabel("Country")
plt.ylabel("Rate")

plt.plot(df2['Country'], df2['Deathrate'], 'o-k', label='Deathrate')
plt.plot(df2['Country'], df2['Birthrate'], 'o-r', label='Birthrate')

plt.legend()

plt.show()