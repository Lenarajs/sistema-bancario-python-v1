menu = """

    [1] - Depositar
    [2] - Sacar
    [3] - Extrato

    [0] - Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("Informe o valor do depósito: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito de R$ {valor_deposito:.2f}.\n"
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!\nSaldo atual: R$ {saldo:.2f}.")
        
        else:
            print(f"Operação inválida, apenas valores positivos são permitidos.")

    elif opcao == "2":
        print(f"Sua conta possui um limite diário de {LIMITE_SAQUES - numero_saques} saques de até R$ {limite:.2f}.")
        valor_saque = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação inválida, saldo insuficiente.")

        elif excedeu_limite:
            print(f"Operação inválida, o limite por saque é de {limite:.2f}.\nTente novamente.")
        
        elif excedeu_saques:
            print(f"Operação inválida, limite de saques diários atingido!")
        
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque de R$ {valor_saque:.2f}.\n"
            numero_saques += 1
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!\nSaldo atual: R$ {saldo:.2f}.")

        else:
            print("Operação inválida, apenas valores positivos são permitidos.")

    elif opcao == "3":
        print(" * * * * * * * * EXTRATO * * * * * * * * \n")
        print("Nenhuma movimentação realizada.\n" if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}\n")
        print(" * * * * * * * * * * * * * * * * * * * * ")

    elif opcao == "0":
        print("Obrigado por utilizar o nosso sistema bancário!\nTenha um ótimo dia!\n")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
