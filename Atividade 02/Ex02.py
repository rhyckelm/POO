agenda = {}
menores = {}

while True:
    cpf = input("Digite o CPF: ")

    if not cpf:
        break

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    agenda[cpf] = {
        "nome": nome,
        "idade": idade,
    }

    if idade < 18:
        menores[nome] = agenda


print("agenda menores de 18 anos: ", menores)
