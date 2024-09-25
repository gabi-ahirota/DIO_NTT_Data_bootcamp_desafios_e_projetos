from datetime import datetime
import random

class ValidacaoCPF:
    def __init__(self, cpf):
        self.cpf = cpf

    def validar(self):
        cpf = ''.join(filter(str.isdigit, self.cpf)) 
        if len(cpf) != 11 or not cpf.isdigit():
            return False
        if cpf == cpf[0] * len(cpf): 
            return False
       
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        resto = soma % 11
        digito1 = 0 if resto < 2 else 11 - resto

        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        resto = soma % 11
        digito2 = 0 if resto < 2 else 11 - resto

        return cpf[-2:] == f"{digito1}{digito2}"

class SistemaBancario:
    def __init__(self):
        self.bd_clientes = {}  
        self.bd_contas = {}  
        self.transacoes = {}
        self.numero_saques = {}
        self.AGENCIA = "0001"
        self.cpf_usuario_atual = None 

    def menu(self):
        opcao = input("""\n
        ============== MENU ===============\n
        [l]\tLogin
        [c]\tCadastrar usuário
        [s]\tSacar
        [d]\tDepositar
        [e]\tExtrato
        [nc]\tCriar conta
        [lu]\tListar usuarios
        [lc]\tListar contas      
        [q]\tSair
        => """)
        return opcao

    def cadastrar_usuario(self):
        print("Você selecionou a opção de cadastro.")
        nome = input("Digite seu nome completo: ")
        cpf = input("Digite o seu CPF: ")

        validador = ValidacaoCPF(cpf)
        if not validador.validar():
            print("CPF inválido. Cadastro não realizado.")
            return
        
        idade = input("Digite sua idade: ")
        telefone = input("Digite seu telefone: ")
        email = input("Digite seu email: ")

        self.bd_clientes[cpf] = {
            "Nome completo": nome,
            "Idade": idade,
            "Telefone": telefone,
            "Email": email
        }

        print(f'{nome}, seu cadastro foi realizado com sucesso.')

    def login(self):
        cpf = input("Digite seu CPF: ")
        if cpf in self.bd_clientes:
            self.cpf_usuario_atual = cpf
            print(f"Login realizado com sucesso! Bem-vindo, {self.bd_clientes[cpf]['Nome completo']}.")
        else:
            print("Usuário não cadastrado.")

    def verificar_conta(self):
        if self.cpf_usuario_atual not in self.bd_contas:
            print("Usuário não possui conta. Por favor, crie uma conta primeiro.")
            return False
        return True

    def criar_conta(self):
        if self.cpf_usuario_atual is None:
            print("Por favor, faça login primeiro.")
            return

        if self.cpf_usuario_atual in self.bd_contas:
            print("O usuário já possui uma conta.")
        else:
            numero_conta = random.randint(10000, 99999)
            self.bd_contas[self.cpf_usuario_atual] = {
                "Agência": self.AGENCIA,
                "Número da conta": numero_conta
            }
            self.transacoes[self.cpf_usuario_atual] = []  
            self.numero_saques[self.cpf_usuario_atual] = 0  
            print(f'Conta criada com sucesso! Agência: {self.AGENCIA} | Número da Conta: {numero_conta}')

    def sacar(self):
        print("Você selecionou a opção de saque.")
        if not self.verificar_conta():
            return
        
        saldo_atual = sum([valor for valor in self.transacoes[self.cpf_usuario_atual]])

        try:
            saque = float(input("Quanto você deseja sacar? "))

            if saque > saldo_atual:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif saque > 500:
                print("Operação falhou! O valor do saque não pode exceder R$500.")
            elif self.numero_saques[self.cpf_usuario_atual] >= 10:
                print("Operação falhou! Número máximo de saques já atingido.")
            else:
                tempo_no_ato = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.transacoes[self.cpf_usuario_atual].append(-saque)
                self.numero_saques[self.cpf_usuario_atual] += 1
                print(f'{tempo_no_ato} - Saque de R${saque:.2f} realizado com sucesso!')
        except ValueError:
            print("Erro. Digite um valor válido.")

    def depositar(self):
        print("Você selecionou a opção de depósito")
        if not self.verificar_conta():
            return

        try: 
            deposito = float(input("Qual valor deseja depositar? "))
            if deposito > 0: 
                tempo_no_ato = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.transacoes[self.cpf_usuario_atual].append(deposito)
                print(f'{tempo_no_ato} - Depósito no valor de R${deposito:.2f} registrado.')
            else:
                print("Depósito inválido.")
        except ValueError:
            print("Erro. Digite um valor válido.")

    def extrato(self):
        print("Você selecionou a opção de extrato.")
        if not self.verificar_conta():
            return

        if self.transacoes[self.cpf_usuario_atual]:
            print("Extrato de operações:")
            for i, valor in enumerate(self.transacoes[self.cpf_usuario_atual], 1):
                tipo = "Depósito" if valor > 0 else "Saque"
                print(f"{i}. {tipo}: R${abs(valor):.2f}")
            saldo_atual = sum(self.transacoes[self.cpf_usuario_atual])
            print(f'O saldo atual: R${saldo_atual:.2f}.')
        else:
            print("Nenhuma operação registrada.")

    def listar_usuarios(self):
        print("Lista de Clientes Cadastrados:")
        if self.bd_clientes:
            for cpf, dado in self.bd_clientes.items():    
                nome = dado['Nome completo']
                idade = dado['Idade']
                telefone = dado['Telefone']
                email = dado['Email']
                print(f"Nome: {nome}, CPF: {cpf}, Idade: {idade}, Telefone: {telefone}, Email: {email}")
        else:
            print("Nenhum cliente cadastrado.")

    def listar_contas(self):
        print("Lista de Contas Cadastradas:")
        if self.bd_contas:
            for cpf, dados in self.bd_contas.items():    
                agencia = dados['Agência']
                numero_conta = dados['Número da conta']
                nome = self.bd_clientes[cpf]['Nome completo']
                print(f"Agência: {agencia}, Conta: {numero_conta}, Nome do usuário: {nome}, CPF: {cpf}")
        else:
            print("Nenhuma conta cadastrada.")

    def operacao(self):
        while True:
            opcao = self.menu()
            if opcao == "l":
                self.login()
            elif opcao == "c":
                self.cadastrar_usuario()
            elif opcao == "s":
                self.sacar()
            elif opcao == "d":
                self.depositar()
            elif opcao == "e":
                self.extrato()
            elif opcao == "nc":
                self.criar_conta()
            elif opcao == "lu":
                self.listar_usuarios()
            elif opcao == "lc":
                self.listar_contas()
            elif opcao == "q":
                print("Saindo do sistema...")
                break

sistema = SistemaBancario()
sistema.operacao()
