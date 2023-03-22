notas = list()
for i in range(4):
  notas.append(float(input('Digite uma nota: ')))

media=sum(notas)/len(notas)

print('Notas: ', media)
