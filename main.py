menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        dep = float(input("Qual o valor que deseja depositar? "))
        if dep <= 0:
            print("Por gentileza digite um valor valido!")
            
        else:
            
            print(f"O valor de R$ {dep:.2f} foi depositado com sucesso!")
            saldo += dep
            extrato += f"Deposito: R$ {dep:.2f}\n"
            
    elif opcao == "s":
        saq = float(input("Qual o valor que deseja sacar? "))
        
        excedeu_saldo = saq > saldo
        
        excedeu_limite = saq > limite
        
        excedeu_saques = numero_saques >=LIMITE_SAQUES
        if excedeu_saldo:
            print("Saque não permitido, pois não a saldo na conta!")
                        
        elif excedeu_limite:
             print("Saque não permitido, pois excedeu o limite da conta!")
        
        elif excedeu_saques:
            print("Saque não permitido, excedeu o numero de maximo de saques do dia!")

        elif saq > 0:
            print(f"O valor de R$ {saq:.2f} foi sacado com sucesso!")
            saldo -= saq
            extrato += f"Saque: R$ {saq:.2f}" 
            numero_saques += 1
        
        else:
            print("Operação falhou! O valor informado é inválido.")     
                      
    elif opcao == "e":
        print("\n==========EXTRATO==========")
        print("não foram realizadas movimentações!" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("============================")
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
