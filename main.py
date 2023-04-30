menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Selecione o valor a depositar:"))
        if valor < 0:
            print("Valor inválido")
        else:
            saldo += valor
            extrato+=(f"Depósito de R${valor:.2f}\n")
    if opcao == "s":
        valor = float(input("Selecione o valor a sacar:"))
        if valor > saldo + limite or valor < 0:
            print("Valor inválido")
        elif numero_saques == LIMITE_SAQUES:
            print("Tentativas de saque esgotadas")
        else:
            if valor > saldo:
                saldo -= valor - limite
                limite = 0
            else:
                saldo -= valor
            extrato+=(f"Saque de R${valor:.2f}\n")
            numero_saques+=1

    if opcao == "e":
        print(extrato + f"O saldo da conta é R${saldo:.2f}\ne o limite é{limite}")
    if opcao == "q":
        break
