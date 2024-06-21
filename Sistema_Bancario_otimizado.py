def depositar(valor, extrato, saldo, /):
    if valor != 0:
        saldo += valor
        extrato += f"\nDepósito:\tR$ {valor:.2f}"

        global total_depositos
        global numero_depositos
        total_depositos += valor
        numero_depositos += 1

        print("Depósito realizado!")
    else:
        print("Valor inválido!")
    
    return extrato, saldo

def sacar(*, valor, extrato, saldo):
    if saldo < valor:
        print("Saldo Insuficiente.")

    elif valor != 0:
        saldo -= valor
        extrato += f"\nSaque:\t\tR$ {valor:.2f}"

        global numero_saques
        global total_saques
        total_saques += valor
        numero_saques += 1

        print("Saque realizado!")
    else:
        print("Valor inválido!")
    
    return extrato, saldo

def mostrar_extrato(saldo, /, *, extrato):
    print("===========EXTRATO===========", end="")

    print("\nNada foi feito." if extrato == "" else extrato)
    print(f"""=============================
Nº Depósitos: {numero_depositos}
Total Depositado: R$ {total_depositos:.2f}
=============================
Nº Saques: {numero_saques}
Total Sacado: R$ {total_saques:.2f}
=============================""")
    
    print(f"Saldo: R$ {saldo:.2f}")

def cadastrar():
    nome = str(input("Nome: "))
    data_nascimento = str(input("Data de nascimento (DD/MM/AAAA): "))
    cpf = int(input("CPF (somente os números): "))

    if clientes:
        repetido = True
        while repetido:
            for pessoa in clientes:
                if cpf == pessoa["cpf"]:
                    repetido = True
                    break
                else:
                    repetido = False
            if repetido:
                print("CPF já cadastrado.")
                cpf = int(input("Informe outro CPF (somente os números): "))

    print("Informações do Endereço")
    logradouro = str(input("Logradouro: "))
    numero = int(input("Número: "))
    bairro = str(input("Bairro: "))
    cidade = str(input("Cidade: "))
    estado = str(input("Sigla do Estado: "))

    endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"

    usuario = dict(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(usuario)

    print("Cadastro realizado!")

def criar_conta(cpf): 
    global num
    num += 1

    conta = dict(agencia=AGENCIA, numero_conta=num, usuario=cpf)
    contas.append(conta)

    print("Conta criada: Nº", conta["numero_conta"])

AGENCIA = "0001"
saldo = 0
num = 0
operacao = -1
extrato = ""

clientes = []
contas = []

total_depositos = 0
numero_depositos = 0
total_saques = 0
numero_saques = 0

while operacao != 0:

    operacao = int(input(f"""
===========MENU===========
1 - Depósito
2 - Saque
3 - Extrato
4 - Criar Usuário
5 - Criar Conta Corrente

0 - Sair
==========================
"""))
    
    if operacao == 1:
        valor = float(input("Valor a Depositar: "))
        while valor < 0:
            valor = float(input("Não pode ser menor que 0: "))
    
        extrato, saldo = depositar(valor, extrato, saldo)

    elif operacao == 2:
        if numero_saques == 3:
            print("Limite diário de Saques excedido:", 3)

        else:
            valor = float(input("Valor a sacar: "))
            while valor < 0 or valor > 500:
                valor = float(input("R$ 500.00 é o valor máximo para saques\nO valor não pode ser menor que 0: "))
            
            extrato, saldo = sacar(valor=valor, extrato=extrato, saldo=saldo)
            
    elif operacao == 3:
        mostrar_extrato(saldo, extrato=extrato)
        
    elif operacao == 4:
        cadastrar()
        
    elif operacao == 5:
        if clientes:
            usuario = int(input("Informe seu CPF (Apenas números): "))

            for pessoa in clientes:
                if usuario != pessoa["cpf"]:
                    repetido = False
                else:
                    repetido = True

            if repetido:
                print("CPF cadastrado!")
                criar_conta(usuario)

            else: print("CPF não encontrado.")
        else: print("Não há usuários cadastrados.")

    elif operacao == 0:
        print("Obrigado por usar o programa!")

    else: print("Escolha uma das opções válidas.")