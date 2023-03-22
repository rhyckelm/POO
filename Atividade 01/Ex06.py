alunos = []
cont = 0
for i in range(2):
  print(f'Aluno {i+1}')
  notas = []
  for i in range(4):
    notas.append(float(input(f'Digite a °{i+1} nota: ')))

  alunos.append(notas)
  media=sum(notas)/len(notas)
  if media >= 7:
    cont += 1
print('Alunos aprovados: ',cont)
