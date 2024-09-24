# Sistema bancario

lista = []

def Menu():
    while True:
        opcao = input("Selecione a opção desejada: \n [S]aque \n [E]xtrato \n [D]eposito \n [Q]uit \n").upper()
        return opcao

def Operacao(opcao):
    if opcao == "S":
        print("Você selecionou a opção de saque.")
        try:
            saque = float(input("Quanto você deseja sacar? "))
            if saque <= 500:
                saldo_atual = sum(lista)
                if saldo_atual >= saque:
                    lista.append(-saque)
                    print(f'Saque de R${saque:.2f} realizado com sucesso!')
                else:
                    print("Saldo insuficiente!")
            
            else:
                print("Saque negado. Limite de no máximo R$500,00 por saque.")

        except ValueError:
            print("Erro. Digite um valor válido.")

    elif opcao == "E":
        print("Você selecionou a opção de extrato.")
        if lista:
            print("Extrato de operações:")
            for i, valor in enumerate(lista, 1):
                tipo = "Depósito" if valor > 0 else "Saque"
                print(f"{i}. {tipo}: R${abs(valor):.2f}")
            soma = sum(lista)
            print(f'O saldo atual: R${soma:.2f}.')
        else:
            print("Nenhuma operação registrada.")

    elif opcao == "D":
        print("Você selecionou a opção de depósito")
        
        try: 
            deposito = float(input("Qual valor deseja depositar? "))
            if deposito > 0: 
                lista.append(deposito)
                print(f'Depósito no valor de R${deposito:.2f} registrado.')
            else:
                print("Depósito inválido.")
        
        except ValueError:
            print("Erro. Digite um valor válido.")

    elif opcao == "Q":
        print("Saindo do sistema...")
        return False

    else:
        print("Opção inválida! Tente novamente.")
    return True  

while True:
    if not Operacao(Menu()):
        break


    