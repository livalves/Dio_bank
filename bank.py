menu = """
------------------------------------
Bem-vindo ao DIO Bank :)

Selecione a operação que deseja realizar: 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
------------------------------------
"""

balance = 0
limit = 500
statement = ""
number_withdrawals = 0
WITHDRAWAL_LIMIT = 3

def deposit():
    global balance, statement
    try:
        amount = float(input("Informe o valor do depósito: "))
        if amount > 0:
            balance += amount
            statement += f'Depósito: R$ {amount:.2f}\n'
            print("\n-> Depósito realizado com sucesso!")
        else:
            print("\n| Seu depósito falhou! Insira um valor válido.")
    except ValueError:
        print("\n| Valor inválido. Por favor, insira um número.")
    
def withdraw():
    global balance, statement, limit, number_withdrawals
    try:
        amount = float(input("Informe o valor do saque: "))
        exceeded_balance = amount > balance
        exceeded_limit = amount > limit
        exceeded_withdrawals = number_withdrawals >= WITHDRAWAL_LIMIT
        if exceeded_balance:
            print("\n| O saque falhou! Você não possui saldo suficiente.")
        elif exceeded_limit:
            print("\n| O saque falhou! O valor do saque excede o limite.")
        elif exceeded_withdrawals:
            print("\n| O saque falhou! Número máximo de saques excedido.")
        elif amount > 0:
            balance -= amount
            statement += f"Saque: R$ {amount:.2f}\n"
            number_withdrawals += 1
            print("\n-> Saque realizado com sucesso!")
        else:
            print("\n| Saque falhou! Insira um valor válido.")
    except ValueError:
        print("\n| Valor inválido. Por favor, insira um número.")    
    
def print_statement():   
    print("\n================ EXTRATO ================")
    print("\nNão foram realizadas movimentações." if not statement else statement)
    print(f"\nSaldo atual: R$ {balance:.2f}")
    print("=========================================")
   
while True: 
    option = input(menu).lower()
    if option == "d":
        deposit()
    elif option == "s":
        withdraw()
    elif option == "e":
        print_statement()
    elif option == "q":
        print("\n*** Operação encerrada! ***")
        break
    else:
        print('\n--- Operação inválida, selecione novamente a operação desejada.')