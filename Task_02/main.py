menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''
usuarios = {}
contas_criadas = 0
contas = {}
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    global usuarios
    if cpf in usuarios:
        print('Já existe um usuário cadastrado com esse CPF.')
    else:
        usuario = {cpf: {'nome': nome, 'data_nascimento': data_nascimento, 'endereco': endereco, 'cpf':cpf}}
        usuarios.update(usuario)
        print('Usuário cadastrado com sucesso!')

def criar_conta(cpf):
    global contas, contas_criadas
    if cpf in usuarios:
        contas_criadas+=1
        campos_conta = {cpf:{'agencia': '0001', 'conta': contas_criadas, 'saldo': 0, 'extrato': "", 'limite': 500, 'saques_do_dia':0}}
        contas.update(campos_conta)
        print('Conta criada com sucesso!')

def sacar(*,cpf):
    valor = float(input("Selecione o valor a sacar:"))
    if valor > contas[cpf]['saldo'] + contas[cpf]['limite'] or valor < 0:
        print("Valor inválido")
    elif contas[cpf]['saques_do_dia'] == LIMITE_SAQUES:
        print("Tentativas de saque esgotadas")
    else:
        if valor > contas[cpf]['saldo']:
            contas[cpf]['saldo'] -= valor - contas[cpf]['limite']
            contas[cpf]['limite'] = 0
            print("Saque realizado com sucesso")
            contas[cpf]['extrato'] += (f"Saque de R${valor:.2f}\n")
        else:
            contas[cpf]['saldo'] -= valor
            contas[cpf]['extrato'] += (f"Saque de R${valor:.2f}\n")
            contas[cpf]['saques_do_dia'] += 1
            print("Saque realizado com sucesso")
            contas[cpf]['extrato'] += (f"Saque de R${valor:.2f}\n")
def depositar(cpf):
    valor = int(input("Selecione o valor a depositar:"))
    if valor < 0:
        print("Valor inválido ou Saldo/Limite insuficientes")
    else:
        contas[cpf]['saldo'] += valor
        print("Depósito realizado com sucesso")
        contas[cpf]['extrato'] += (f"Depósito de R${valor:.2f}\n")
def extrato(cpf):
    print(f"o extrato da sua conta é:\n{contas[cpf]['extrato']}\nSeu saldo é {contas[cpf]['saldo']}\nSeu limite é {contas[cpf]['limite']}")

cadastrar_usuario('Sabrina','06/05/2000','72','Rua dos anjos 100')
criar_conta('72')
cadastrar_usuario('Victor','09/03/2001','15','Rua paraguai 180')
criar_conta('15')
print(contas['15']['saldo'])
while True:
    opcao = input(menu)
    if opcao == "d":
        resp = input("Digite o CPF da conta que você deseja depositar dinheiro: ")
        if resp in contas:
            depositar(resp)
        else:
            print("Conta não encontrada")
    if opcao == "s":
        resp = input("Digite o CPF da conta que você deseja sacar dinheiro: ")
        if resp in contas:
            sacar(cpf = resp)
        else:
            print("Conta não encontrada")

    if opcao == "e":
        resp = input("Digite o CPF da conta que você deseja visualizar o extrato: ")
        if resp in contas:
            extrato(resp)
        else:
            print("Conta não encontrada")
    if opcao == "q":
        break
