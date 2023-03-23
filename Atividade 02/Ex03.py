principal = {}
backup = {}

while True:
    chave = input("Digite a chave do dicionário: ")
    valor = input("Digite o valor para armaxenar: ")
    principal[chave] = valor
    backup[chave] = valor

    if len(principal) == 5:
        print("Dados do dicionário principal:")
        print(principal)
        principal = {}

    if len(backup) == 10:
        print("Backup:")
        print(backup)
        backup = {}
