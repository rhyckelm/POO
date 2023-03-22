agenda = {}

while True:
    cpf = input('Digite o CPF: ')

    if not cpf:
        break
    
    nome = input('Digite o nome: ')
    idade = input('Digite a idade: ')
    telefone = input('Digite o telefone: ')
    
    agenda[cpf] = {
        'nome': nome,
        'idade': idade,
        'telefone': telefone
    }

print('Agenda:')
for cpf, dados in agenda.items():
    print(f"{dados['nome']}-{dados['idade']}-{dados['telefone']}")
