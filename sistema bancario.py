menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 3


while True:

    opçao = imput(menu)

    if opçao == "1":
          valor = float(imput("Informe o valor do deposito:"))

          if valor > 0:
              saldo += valor
              extrato += f"Deposito: R$ {valor:.2f}\n"

    else:
        print("Falha na operação! Valor invalido")         


    elif opçao == "2":
        valor = float(input("informe o valor do saque"))
        
        excedeu_saldo = valor > saldo
    
        excedeu_limite = valor > limite
    
        excedeu_saques = numero_saques >= LIMITE_SAQUES
    
        if excedeu_saldo:
           print("Falha na operação! voce não tem saldo suficiente.")

        elif excedeu_limite:
           print("Falha na operação! o valor do saque excede o limite")   

        elif excedeu_saques:
           print("Falha na operação! Numero de saques exedido")

        else valor > 0:
             saldo -= valor
             extrato += f"saque: R$ {valor:.2f}\n"
             numero_saqus += 1

        else:
             print("Operaçao falhou! Valor invalido.")
    
    elif opçao == "3":
        print("\n=============EXTRATO=============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("====================================")
    
    elif opçao =="4":
        break

    else:
        print("Operação invalida, por favor selecione novamente a opção desejada.")

           
    
