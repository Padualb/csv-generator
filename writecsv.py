import csv
import json

with open('empresas.csv', 'w', newline='') as csvfile:
    campos = ['pessoa', 'sigla', 'data', 'pqp', 'tata']

    writer = csv.DictWriter(csvfile, fieldnames=campos)

    qtd = 80
    jsonList = list()

    for y in range(0, qtd):
        dicty = {}
        for i, campo in enumerate(campos):
            dicty[campo] = campo + str(y+1)

        jsonList.append(dicty)

    writer.writeheader()
    for i in range(qtd):
        writer.writerow(jsonList[i])
