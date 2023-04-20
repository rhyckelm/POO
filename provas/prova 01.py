motoristas = dict()


def cadastrar_motorista():
    nome = input("Digite o nome do motorista: ")
    cpf = input("Digite o cpf do motorista: ")
    rg = input("Digite o RG do motorista: ")
    cnh = input("Digite a CNH do motorista: ")
    motoristas.update({cpf: {"nome": nome, "cpf": cpf, "rg": rg, "cnh": cnh}})
    print("cadastro de motorista realizado com sucesso!")


veiculos = dict()


def cadastrar_veiculo():
    marca = input("Digite a marca do veiculo: ")
    modelo = input("Digite o modelo do veiculo: ")
    ano = input("Digite o ano do veiculo: ")
    placa = input("Digite a placa do veiculo: ")
    chassi = input("Digite o chassi do veiculo: ")
    cor = input("Digite a cor do veiculo: ")
    km = int(input("Digite a quilometragem do veiculo: "))
    veiculos.update(
        {
            placa: {
                "marca": marca,
                "modelo": modelo,
                "ano": ano,
                "placa": placa,
                "chassi": chassi,
                "cor": cor,
                "km": km,
            }
        }
    )
    print("Cadastro de veiculos realizado com sucesso!")


def pesquisar_motorista():
    num = len(motoristas)
    if num == 0:
        print("Nao a motoristas cadastrados no sistema.")
        return

    cpf = input("Digite o cpf do motorista a ser procurado: ")
    motorista = motoristas.get(cpf)
    if motorista:
        print("Motorista encontrado!")
        return motorista
    else:
        print("Motorista nao encontrado.")


def pesquisar_veiculo():
    num = len(veiculos)
    if num == 0:
        print("Nao a veiculos cadastrados no sistema.")
        return

    placa = input("Digite a placa do veiculo a ser procurado: ")
    veiculo = veiculos.get(placa)
    if veiculo:
        print("Veiculo encontrado!")
        return veiculo
    else:
        print("Veiculo nao encontrado.")


def editar_motorista():
    motorista = pesquisar_motorista()
    while True:
        res = str(input("Deseja editar o nome? [S/N]")).upper()[0]
        if res in "SN":
            break
        print("Erro!, responda apenas com S ou N")
        if res == "N":
            return
    motorista["nome"] = input("Digite o novo nome: ")
    while True:
        res = str(input("Deseja editar o rg? [S/N]")).upper()[0]
        if res in "SN":
            break
        print("Erro!, responda apenas com S ou N")
        if res == "N":
            return
    motorista["rg"] = input("Digite o novo RG: ")
    while True:
        res = str(input("Deseja editar o cnh? [S/N]")).upper()[0]
        if res in "SN":
            break
        print("Erro!, responda apenas com S ou N")
        if res == "N":
            return
    motorista["cnh"] = input("Digite a nova CNH: ")
    print("Motorista editado com sucesso!")


def editar_veiculos():
    veiculo = pesquisar_veiculo()
    while True:
        res = str(input("Deseja editar a marca? [S/N]")).upper()[0]
        if res in "SN":
            break
        print("Erro!, responda apenas com S ou N")
        if res == "N":
            return
    veiculo["marca"] = input("Digite a nova marca: ")
    while True:
        res = str(input("Deseja editar o modelo? [S/N]")).upper()[0]
        if res in "SN":
            break
        print("Erro!, responda apenas com S ou N")
        if res == "N":
            return
    veiculo["modelo"] = input("Digite o novo modelo: ")
    while True:
        res = str(input("Deseja editar o ano? [S/N]")).upper()[0]
        if res in "SN":
            break
        print("Erro!, responda apenas com S ou N")
        if res == "N":
            return
    veiculo["ano"] = input("Digite o novo ano: ")
    while True:
        res = str(input("Deseja editar o chassi? [S/N]")).upper()[0]
        if res in "SN":
            break
        print("Erro!, responda apenas com S ou N")
        if res == "N":
            return
    veiculo["chassi"] = input("Digite o novo chassi: ")
    while True:
        res = str(input("Deseja editar a cor? [S/N]")).upper()[0]
        if res in "SN":
            break
        print("Erro!, responda apenas com S ou N")
        if res == "N":
            return
    veiculo["cor"] = input("Digite a nova cor: ")
    while True:
        res = str(input("Deseja editar a quilometragem? [S/N]")).upper()[0]
        if res in "SN":
            break
        print("Erro!, responda apenas com S ou N")
        if res == "N":
            return
    veiculo["km"] = int(input("Digite a nova quilometragem: "))
    print("Veiculo editado com sucesso!")


def deletar_motorista():
    num = len(motoristas)
    if num == 0:
        print("Nao a motoristas cadastrados no sistema.")
        return

    cpf = input("Digite o cpf do motorista que deseja deletar: ")
    if cpf in veiculos:
        del motoristas[cpf]
        print("Motorista removido com sucesso!")
    else:
        print("Motorista não encontrado.")


def deletar_veiculo():
    num = len(veiculos)
    if num == 0:
        print("Nao a veiculos cadastrados no sistema.")
        return

    placa = input("Digite a placa do veiculo que deseja deletar: ")
    if placa in veiculos:
        del veiculos[placa]
        print("Veiculo removido com sucesso!")
    else:
        print("Veiculo não encontrado.")


def quilometragem():
    veiculo = pesquisar_veiculo()
    print("Essa é a quilometragem desse veiculo: ", veiculo["km"])


viagens = dict()
cod_v = int(2)


def cadastrar_viagem():
    tam_motorista = len(motoristas)
    tam_veiculos = len(veiculos)
    if tam_motorista and tam_veiculos == 0:
        print("Nao possui motoristas ou veiculos suficentes no sistema.")
        return
    destino = input("Digite o destino da viagem: ")
    origem = input("Digite a origem da viagem: ")
    distancia = int(input("Digite a distacia da viagem em km: "))
    cpf = input("Digite o cpf do motorista: ")
    placa = input("Digite a placa do veiculo: ")

    cod_v = +1
    viagens.update(
        {
            cod_v: {
                "destino": destino,
                "origem": origem,
                "distancia": distancia,
                "motorista": motoristas[cpf],
                "veiculo": veiculos[placa],
            }
        }
    )
    print("Viagem cadastrada com sucesso!")


def editar_viagem():
    motorista = pesquisar_motorista()
    veiculo = pesquisar_veiculo()

    if motorista == viagens["motorista"] and veiculo == viagens["veiculo"]:
        id = viagens.get(cod_v)

    while True:
        res = str(input("Deseja editar o destino? [S/N]")).upper()[0]
        if res in "SN":
            break
        print("Erro!, responda apenas com S ou N")
        if res == "N":
            return
    id["destino"] = input("Digite o novo destino: ")
    while True:
        res = str(input("Deseja editar a origem? [S/N]")).upper()[0]
        if res in "SN":
            break
        print("Erro!, responda apenas com S ou N")
        if res == "N":
            return
    id["origem"] = input("Digite a nova origem: ")
    while True:
        res = str(input("Deseja editar a distancia? [S/N]")).upper()[0]
        if res in "SN":
            break
        print("Erro!, responda apenas com S ou N")
        if res == "N":
            return
    id["distancia"] = int(input("Digite a nova distancia: "))
    print("Viagem editada com sucesso!")


manutencoes = dict()
cod_m = int(2)


def re_manutencoes():
    tam_veiculos = len(veiculos)
    if tam_veiculos == 0:
        print("Nao a veiculos suficentes no sistema.")
        return
    tipo = input("Digite o tipo de manutençao: ")
    data = input("Digite a data da manutençao: ")
    custo = int(input("Digite o curso da manutençao: "))
    placa = input("Digite a placa do veiculo: ")

    cod_m = +1
    manutencoes.update(
        {
            cod_m: {
                "veiculo": veiculos[placa],
                "data": data,
                "tipo": tipo,
                "custo": custo,
            }
        }
    )
    print(manutencoes)


abastecimentos = dict()
cod_a = int(2)


def re_abastecimentos():
    tam_veiculos = len(veiculos)
    if tam_veiculos == 0:
        print("Nao a veiculos suficentes no sistema.")
        return
    quantidade = input("Digite a quantidade de litros: ")
    data = input("Digite a data do abastecimento: ")
    valor = input("Digite o valor do abastecimento: ")
    placa = input("Digite a placa do veiculo: ")

    cod_a = +1
    abastecimentos.update(
        {
            cod_a: {
                "veiculo": veiculos[placa],
                "valor": valor,
                "data": data,
                "quantidade": quantidade,
            }
        }
    )
    print(abastecimentos)


def relatorio():
    # Quantidade de Motoristas
    qtd_motoristas = len(motoristas)
    print(f"Quantidade de Motoristas: {qtd_motoristas}")

    # Quantidade de Veículos
    qtd_veiculos = len(veiculos)
    print(f"Quantidade de Veículos: {qtd_veiculos}")

    # Encontra e exibe o motorista com a maior quilometragem percorrida
    motorista_mais_km = max(motoristas, key=lambda motorista: motorista.km_percorridos)
    print("Motorista com a maior quilometragem percorrida:", motorista_mais_km.nome)

    # Encontra e exibe o motorista com mais viagens
    max_viagens = 0
    motorista_mais_viagens = None
    for motorista in motoristas:
        if motorista.num_viagens > max_viagens:
            max_viagens = motorista.num_viagens
            motorista_mais_viagens = motorista.nome
    print("Motorista com mais viagens:", motorista_mais_viagens)

    # Veículo com maior km
    km_por_veiculo = {}
    for viagem in viagens:
        if viagem["veiculo"] in km_por_veiculo:
            km_por_veiculo[viagem["veiculo"]] += viagem["quilometragem"]
        else:
            km_por_veiculo[viagem["veiculo"]] = viagem["quilometragem"]
    if km_por_veiculo:
        veiculo_maior_km = max(km_por_veiculo, key=km_por_veiculo.get)
        print(f"Veículo com maior km percorrido: {veiculo_maior_km}")

    # Total de despesas com abastecimento
    total_abastecimento = sum(
        abastecimento["valor"] for abastecimento in abastecimentos
    )
    print(f"Total de despesas com abastecimento: R${total_abastecimento:.2f}")

    # Total de despesas de Manutenção
    total_manutencao = sum(manutecao["valor"] for manutecao in manutencoes)
    print(f"Total de despesas com manutenção: R${total_manutencao:.2f}")


while True:
    print("1 - Cadastrar motorista.")
    print("2 - Pesquisar motorista.")
    print("3 - Editar motorista.")
    print("4 - Deletar motorista.")
    print("5 - Cadastrar veiculo")
    print("6 - Pesquisar veiculo.")
    print("7 - Editar motorista.")
    print("8 - Deletar veiculo.")
    print("9 - Ver quilometragem do veiculo.")
    print("10 - Cadastrar viagem.")
    print("11 - Editar viagem.")
    print("12 - Registrar manutençoes.")
    print("13 - Registrar abastecimentos.")
    print("14 - Relatorio")
    while True:
        op = int(input("Digite a opçao desejada: "))
        if op > 0:
            match op:
                case 1:
                    cadastrar_motorista()
                    break
                case 2:
                    print(pesquisar_motorista())
                    break
                case 3:
                    editar_motorista()
                    break
                case 4:
                    deletar_motorista()
                    break
                case 5:
                    cadastrar_veiculo()
                    break
                case 6:
                    print(pesquisar_veiculo())
                    break
                case 7:
                    editar_veiculos()
                    break
                case 8:
                    deletar_veiculo()
                    break
                case 9:
                    quilometragem()
                    break
                case 10:
                    cadastrar_viagem()
                    break
                case 11:
                    editar_viagem()
                    break
                case 12:
                    re_manutencoes()
                    break
                case 13:
                    re_abastecimentos()
                case 14:
                    relatorio()
