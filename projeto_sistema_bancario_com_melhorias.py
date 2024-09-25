from datetime import datetime

class SistemaBancario:
    def __init__(self):
        self.bd_clientes = {}
        self.limite_saques = 10
        self.numero_saques = 0  
        self.lista = []

    def menu(self):
        while True:
            opcao = input("Selecione a opção desejada: \n [C]adastro_cliente \n [S]aque \n [E]xtrato \n [D]eposito \n [L]istar Clientes \n [Q]uit \n").upper()
            return opcao

    def cadastrar_cliente(self):
        print("Você selecionou a opção de cadastro.")
        nome = input("Digite seu nome completo: ")
        idade = input("Digite sua idade: ")
        telefone = input("Digite seu telefone: ")
        email = input("Digite seu email: ")

        self.bd_clientes[nome] = {
            "idade": idade, 
            "telefone": telefone, 
            "email": email
        }

        print(f'{nome}, seu cadastro foi realizado com sucesso.')

    def realizar_saque(self):
        print("Você selecionou a opção de saque.")
        try:
            saque = float(input("Quanto você deseja sacar? "))
            saldo_atual = sum([valor for valor, _ in self.lista])

            if saque > saldo_atual:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif saque > 500:
                print("Operação falhou! O valor do saque não pode exceder R$500.")
            elif self.numero_saques >= self.limite_saques:
                print("Operação falhou! Número máximo de saques já atingido.")
            else:
                tempo_no_ato = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.lista.append((-saque, tempo_no_ato))
                self.numero_saques += 1  
                print(f'Saque de R${saque:.2f} realizado com sucesso às {tempo_no_ato}!')
        except ValueError:
            print("Erro. Digite um valor válido.")

    def realizar_deposito(self):
        print("Você selecionou a opção de depósito")
        try: 
            deposito = float(input("Qual valor deseja depositar? "))
            if deposito > 0: 
                tempo_no_ato = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.lista.append((deposito, tempo_no_ato))
                print(f'Depósito no valor de R${deposito:.2f} registrado às {tempo_no_ato}.')
            else:
                print("Depósito inválido.")
        except ValueError:
            print("Erro. Digite um valor válido.")

    def mostrar_extrato(self):
        print("Você selecionou a opção de extrato.")
        if self.lista:
            print("Extrato de operações:")
            for i, (valor, tempo_no_ato) in enumerate(self.lista, 1):
                tipo = "Depósito" if valor > 0 else "Saque"
                print(f"{tempo_no_ato} - {i}. {tipo}: R${abs(valor):.2f}")
            saldo_atual = sum([valor for valor, _ in self.lista])
            print(f'O saldo atual: R${saldo_atual:.2f}.')
        else:
            print("Nenhuma operação registrada.")

    def listar_clientes(self):
        print("Lista de Clientes Cadastrados:")
        if self.bd_clientes:
            for nome, dado in self.bd_clientes.items():    
                idade = dado['idade']
                telefone = dado['telefone']
                email = dado['email']
                print(f"Nome: {nome}, Idade: {idade}, Telefone: {telefone}, Email: {email}")
        else:
            print("Nenhum cliente cadastrado.")

    def operacao(self, opcao):
        if opcao == "C":
            self.cadastrar_cliente()
        elif opcao == "S":
            self.realizar_saque()
        elif opcao == "D":
            self.realizar_deposito()
        elif opcao == "E":
            self.mostrar_extrato()
        elif opcao == "L":
            self.listar_clientes()
        elif opcao == "Q":
            print("Saindo do sistema...")
            return False
        else:
            print("Opção inválida! Tente novamente.")
        
        return True  

    def executar(self):
        while True:
            opcao = self.menu()  
            if not self.operacao(opcao):  
                break
            
sistema = SistemaBancario()
sistema.executar()
