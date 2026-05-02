from banco import Banco
from conta import ContaCorrente, ContaPoupanca
from cliente import ClienteFisico, ClienteJuridico

def main():

    # Criando instância de Banco
    banco = Banco("Itaú")
    # Criando instâncias de Cliente
    banco.add_cliente(ClienteFisico("Lucas", "12345678909"))
    # Criando instância de Agência
    banco.add_agencia("0001")
    # Criando instância de Conta
    banco.add_conta(ContaCorrente("1337", "0001", 1000))


    while True:

        print("\n--- Sistema Bancário ---")
        print("1. Criar conta")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("1. Cliente Físico")
            print("2. Cliente Jurídico")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                nome = input("Nome: ")
                cpf = input("CPF: ")
                banco.add_cliente(ClienteFisico(nome, cpf))
            elif opcao == "2":
                nome = input("Nome: ")
                cnpj = input("CNPJ: ")
                banco.add_cliente(ClienteJuridico(nome, cnpj))
        
        elif opcao == "2":
            numero_conta = input("Conta: ")
            valor = float(input("Valor: "))
            for conta in banco.contas:
                if conta.conta == numero_conta:
                    conta.depositar(valor)
                    print(f"Saldo atual: R$ {conta.saldo}")
                    break
            else:
                print("Conta não encontrada.")

        elif opcao == "3":
            numero_conta = input("Conta: ")
            valor = float(input("Valor: "))
            for conta in banco.contas:
                if conta.conta == numero_conta:
                    conta.sacar(valor)
                    print(f"Saldo atual: R$ {conta.saldo}")
                    break
            else:
                print("Conta não encontrada.")

        elif opcao == "4":
            break

        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()