import pandas as pd
import matplotlib.pyplot as plt

bd = pd.read_csv("dataset.csv")



#Moda dos diretores
numeromax = bd['directors'].value_counts().max()
diretores = bd['directors'].value_counts()
print('O número de aparições dos diretores que mais possuem filmes na lista é', numeromax)
for i in range(len(diretores)):
    if diretores[i] == numeromax:
        print(diretores.index[i])
print('São os diretores que aparecem', numeromax, 'vezes.')

'''
print(bd['run_time'][0])
print(bd['run_time'][1])


tempomin = []
for k in range(len(bd)):
    filme = bd['run_time'][k]
    if filme.count('h') == 0 and filme != 'Not Available':
        filme ='0h' + filme
    a = filme.replace('m', 'h').split('h')
    soma = 0
    for i in range(len(a)):
        if a[i] == 'Not Available':
            tempomin.append('Not Available')
        else:
            if i == 0:
                soma += (60*int(a[i]))
            if i == 1 and a[i] != '':
                soma += int(a[i])
    if a[0] != 'Not Available':
        tempomin.append(soma)

bd['run_time'] = tempomin
print(bd.head())
'''