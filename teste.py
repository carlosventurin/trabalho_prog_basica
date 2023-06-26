import pandas as pd
import matplotlib.pyplot as plt

bd = pd.read_csv("dataset.csv")

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