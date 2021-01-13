# -*- coding: utf-8 -*-
"""Yahoo x Twitter

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ymd488MZlHVn2vhQZjxQguxMYlj0Akzn
"""


import csv
import pandas as pd
import matplotlib.pyplot as plt

sentiment_data = []

with open('datasets/date_sentiment_bolsa.csv','r') as csvfile:
    data = csv.reader(csvfile, delimiter = ' ')
    for row in data:
      sentiment_data.append(';'.join(row))


    for i, n in enumerate(sentiment_data):
        txt = n
        txt = txt.replace("Mar;", "Mar/")
        sentiment_data[i] = txt
        txt = txt.replace("Apr;", "Apr/")
        sentiment_data[i] = txt
        txt = txt.replace("May;","May/")
        sentiment_data[i] = txt
      


txt = sentiment_data[0]
sentiment_data[0] = txt.replace(";;", ";")
df = pd.DataFrame(sentiment_data)
new_df = df[0].str.split(';', expand=True)

##new_df = new_df.drop([44,45,46,47,48,49,50], axis=0)
title = new_df.iloc[:1]
print(title)
new_df = new_df.iloc[1:]
print(new_df)

new_df[1] = pd.to_numeric(new_df[1])
new_df[2] = pd.to_numeric(new_df[2])
new_df[3] = pd.to_numeric(new_df[3])
new_df[4] = pd.to_numeric(new_df[4])

# Commented out IPython magic to ensure Python compatibility.
#importando a biblioteca
import matplotlib.pyplot as plt
#permite que o gráfico seja mostrado no seu notebook
# %matplotlib inline 
plt.rcParams['figure.figsize'] = (10,6)




x = new_df[0]
y1 = new_df[2]*100/new_df[1]
y2 = new_df[3]*100/new_df[1]
y3 = new_df[4]*100/new_df[1]

plt.plot(x,y1, label="Positivos")
plt.plot(x,y2, label="Neutros")
plt.plot(x,y3, label="Negativos")
plt.xticks(rotation = 90)
plt.legend()
plt.title("Porcentagem de Sentimentos Expressos via Twitter de 20/03 até 22/05")
plt.show()

# Commented out IPython magic to ensure Python compatibility.


###BOVESPA
#importando a biblioteca
import matplotlib.pyplot as plt
#permite que o gráfico seja mostrado no seu notebook
# %matplotlib inline 
plt.rcParams['figure.figsize'] = (13,8)



x = new_df[0]
y1 = pd.to_numeric(new_df[7])
teste = new_df[2]*100/new_df[1]
teste2 = new_df[3]*100/new_df[1]
teste3= new_df[4]*100/new_df[1]

fig,ax1 = plt.subplots()
plt.bar(x,y1)
plt.xticks(rotation = 90, fontsize=13)
plt.yticks(fontsize=13)

ax2 = ax1.twinx()
ax2.plot(x,teste, color="Green", label="Positivo")
##ax2.plot(x,teste2, color="Red")
ax2.plot(x, teste3, color="Red", label="Negativo")
plt.yticks(fontsize=13)

plt.title("Movimentação B3 (em pontos) X Sentimentos expressados no twitter (%)", fontsize= 15)
plt.legend()

plt.show()

# Commented out IPython magic to ensure Python compatibility.

###NYSE

#importando a biblioteca
import matplotlib.pyplot as plt
#permite que o gráfico seja mostrado no seu notebook
# %matplotlib inline 
plt.rcParams['figure.figsize'] = (13,8)


x = new_df[0]
y1 = pd.to_numeric(new_df[9])
teste = new_df[2]*100/new_df[1]
teste2 = new_df[3]*100/new_df[1]
teste3= new_df[4]*100/new_df[1]

fig,ax1 = plt.subplots()
plt.bar(x,y1)
plt.xticks(rotation = 90, fontsize=13)
plt.yticks(fontsize=13)

ax2 = ax1.twinx()
ax2.plot(x,teste, color="Green",label="Positivo")
##ax2.plot(x,teste2, color="Red")
ax2.plot(x, teste3, color="Red", label="Negativo")
plt.yticks(fontsize=13)

plt.title("Movimentação NYSE(em pontos) X Sentimentos expressados no twitter (%)", fontsize=15)
plt.legend()

plt.show()

# Commented out IPython magic to ensure Python compatibility.
###NASDAQ

#importando a biblioteca
import matplotlib.pyplot as plt
#permite que o gráfico seja mostrado no seu notebook
# %matplotlib inline 
plt.rcParams['figure.figsize'] = (13,8)


x = new_df[0]
y1 = pd.to_numeric(new_df[11])
teste = new_df[2]*100/new_df[1]
teste2 = new_df[3]*100/new_df[1]
teste3= new_df[4]*100/new_df[1]

fig,ax1 = plt.subplots()
plt.bar(x,y1)
plt.xticks(rotation = 90, fontsize=13)
plt.yticks(fontsize=13)

ax2 = ax1.twinx()
ax2.plot(x,teste, color="Green", label="Positivo")
##ax2.plot(x,teste2, color="Red")
ax2.plot(x, teste3, color="Red", label="Negativo")
plt.yticks(fontsize=13)

plt.title("Movimentação NASDAQ (em pontos) X Sentimentos expressados no twitter (%)", fontsize=15)
plt.legend()
plt.show()

# Commented out IPython magic to ensure Python compatibility.
###Dow Jones

#importando a biblioteca
import matplotlib.pyplot as plt
#permite que o gráfico seja mostrado no seu notebook
# %matplotlib inline 
plt.rcParams['figure.figsize'] = (13,8)


x = new_df[0]
y1 = pd.to_numeric(new_df[13])
teste = new_df[2]*100/new_df[1]
teste2 = new_df[3]*100/new_df[1]
teste3= new_df[4]*100/new_df[1]

fig,ax1 = plt.subplots()
plt.bar(x,y1)
plt.xticks(rotation = 90, fontsize=13)
plt.yticks(fontsize=13)

ax2 = ax1.twinx()
ax2.plot(x,teste, color="Green", label="Positivo")
##ax2.plot(x,teste2, color="Red")
ax2.plot(x, teste3, color="Red", label="Negativo")
plt.yticks(fontsize=13)

plt.title("Movimentação Dow Jones (em pontos) X Sentimentos expressados no twitter (%)", fontsize=15)
plt.legend()

plt.show()