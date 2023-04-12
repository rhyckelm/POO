funcionario = dict()
lista = list()


def cadastrar():
    while True:
        funcionario.clear()
        funcionario["nome"] = input("Nome: ")
        funcionario["cpf"] = input("Cpf: ")
        funcionario["cargo"] = input("Cargo: ")
        funcionario["salario"] = float(input("Salario: "))
        funcionario["telefone"] = []
        qnt = int(input("Deseja adicionar quantos telefones? "))
        for i in range(qnt):
            telefone = input("Telefone: ")
            funcionario["telefone"].append(telefone)
        lista.append(funcionario.copy())
        while True:
            res = str(input("Deseja continuar? [S/N]")).upper()[0]
            if res in "SN":
                break
            print("Erro!, responda apenas com S ou N")
        if res == "N":
            break


def pesquisar(cpf):
    indice_pessoas = {i["cpf"]: i for i in lista}
    print(indice_pessoas[cpf])


def tel_novo(cpf):
    for i in lista:
        if cpf == i["cpf"]:
            telefone = input("Telefone: ")
            funcionario["telefone"].append(telefone)
            print("Telefone novo adicionado")
        else:
            print("Cpf nao encontrado.")


def editar(cpf):
    for i in lista:
        if cpf == i["cpf"]:
            cargo = input("Cargo: ")
            i["cargo"] = cargo
            salario = float(input("Salario: "))
            i["salario"] = salario
            telefone = input("Telefone: ")
            i["telefone"].clear()
            i["telefone"].append(telefone)
            print("Funcionario editado")
            return
    print("Cpf nao encontrado.")


def remover(cpf):
    for i in range(len(lista)):
        if cpf == lista[i]["cpf"]:
            del lista[i]
            print("Funcionario removido")
            return
    print("Cpf nao encontrado.")


cadastrar()
cpf = input("Digite o cpf: ")
remover(cpf)

print(lista)
