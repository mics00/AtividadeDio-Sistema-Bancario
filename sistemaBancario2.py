from datetime import datetime

menu = """ 
[1] Depositar
[2] Sacar 
[3] Extrato
[4] Sair 

=> """

saldo = 0 
limite = 500.0
extrato = []
LIMITE_SAQUES = 0
LIMITE_TRANSACOES = 0
MAX_TRANSACOES_DIARIAS = 10
deposito = 0

def registro_transacao(tipo, valor):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"{timestamp} - {tipo}: R$ {valor:.2f}"

def depositar(saldo, extrato):
    global LIMITE_TRANSACOES
    if LIMITE_TRANSACOES >= MAX_TRANSACOES_DIARIAS:
          print("Você atingiu o limite de transações diárias!")
          return saldo, extrato 
    
    print("\n--- Depósito ---")
    deposito = float(input("Qual valor você deseja depositar?"))

    if deposito > 0:
        saldo += deposito
        extrato.append(registro_transacao("Depósito", deposito))
        LIMITE_TRANSACOES += 1 
        print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")
    else: 
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato
    

def sacar (saldo, extrato, limite):
            
            global LIMITE_SAQUES, LIMITE_TRANSACOES

            if LIMITE_TRANSACOES >= MAX_TRANSACOES_DIARIAS:
                 print("Você atingiu o limite de transações diárias!")
                 return saldo, extrato, LIMITE_SAQUES

            print("\n--- Saque ---")
            saque = float(input("Digite o valor a ser sacado: R$ "))
            
            if saque <= 0:
                 print("Operação falhou! O valor informado é inválido.")
                 return saldo, extrato, LIMITE_SAQUES

            elif LIMITE_SAQUES >= 3:
                  print("Já ultrapassou o limite de saques diários")
                  return saldo, extrato, LIMITE_SAQUES

            elif saque > limite:
                print(f"O valor de saque excede o limite de R$ {limite:.2f}.")
                return saldo, extrato, LIMITE_SAQUES
            
            elif saldo < saque:
                print("Seu saldo é insuficiente...")
                return saldo, extrato, LIMITE_SAQUES
            
            else:
                saldo -= saque
                extrato.append(registrar_transacao("Saque", saque))
                LIMITE_SAQUES += 1
                LIMITE_TRANSACOES += 1
                print(f"Saque de R$ {saque:.2f} realizado com sucesso!")

            return saldo, extrato, LIMITE_SAQUES
   
def ver_extrato (saldo, extrato):
                print("\n---- Extrato ----\n")
                if len (extrato) == 0:
                    print("Nenhuma transação realizada ainda.")
                else: 
                    for transacao in extrato:
                        print(transacao)

                print(f"\nSaldo atual: R$ {saldo:.2f}")

while True:

    opcao = input(menu)
    if opcao == "1":
          saldo, extrato = depositar(saldo, extrato)

    elif opcao == "2":
          saldo, extrato, LIMITE_SAQUES = sacar(saldo, extrato, limite) 
    elif opcao == "3":
          ver_extrato(saldo, extrato)
    elif opcao == "4":
        print("Saindo da conta... ")
        break
    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada.")





    



    