class SistemaBancario:
    def __init__(self):
        self.lista = [] 
        self.limite_saques = 3 
        self.numero_saques = 0  

    def menu(self):
        while True:
            opcao = input("Selecione a opção desejada: \n [S]aque \n [E]xtrato \n [D]eposito \n [Q]uit \n").upper()
            return opcao

    def operacao(self, opcao): 
        if opcao == "S":
            print("Você selecionou a opção de saque.")
            try:
                saque = float(input("Quanto você deseja sacar? "))

                saldo_atual = sum(self.lista)  

                excedeu_saldo = saque > saldo_atual
                excedeu_limite = saque > 500
                excedeu_saques = self.numero_saques >= self.limite_saques

                if excedeu_saldo:
                    print("Operação falhou! Você não tem saldo suficiente.")
                elif excedeu_limite:
                    print("Operação falhou! O valor do saque não pode exceder R$500.")
                elif excedeu_saques:
                    print("Operação falhou! Número máximo de saques já atingido.")
                else:
                    self.lista.append(-saque) 
                    self.numero_saques += 1  
                    print(f'Saque de R${saque:.2f} realizado com sucesso!')

            except ValueError:
                print("Erro. Digite um valor válido.")

        elif opcao == "E":
            print("Você selecionou a opção de extrato.")
            if self.lista:
                print("Extrato de operações:")
                for i, valor in enumerate(self.lista, 1):
                    tipo = "Depósito" if valor > 0 else "Saque"
                    print(f"{i}. {tipo}: R${abs(valor):.2f}")
                saldo_atual = sum(self.lista)  
                print(f'O saldo atual: R${saldo_atual:.2f}.')
            else:
                print("Nenhuma operação registrada.")

        elif opcao == "D":
            print("Você selecionou a opção de depósito")
            
            try: 
                deposito = float(input("Qual valor deseja depositar? "))
                if deposito > 0: 
                    self.lista.append(deposito)  
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

    def executar(self):
        
        while True:
            if not self.operacao(self.menu()):
                break

sistema = SistemaBancario()
sistema.executar()
