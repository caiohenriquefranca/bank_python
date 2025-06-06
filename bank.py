# Parei na função de deposito 


import textwrap

def menu():
    menu = """
    ================== MENU ==================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo Usuário
    [q]\tSair

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizada com sucesso!===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    


    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito:"))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque:"))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você nao tem saldo suficiente.")
    
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

            elif valor > 0:
                print(f"Saque de R${valor:.2f} realizado com sucesso!")
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
            
            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "e":
            print("\n ================== EXTRATO ==================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("================================================")

        elif opcao =="q":
            break

        else:
            print("Operação inválida, por favor selecione a operação desejada.")

main()