from InquirerPy import prompt

saldo = 0.0
limite = 500.0
extrato = ""
numeroSaques = 0
LIMITE_SAQUE = 3

def main():
    global saldo, extrato, numeroSaques

    # Definição das perguntas/menu interativo usando InquirerPy
    perguntas = [
        {
            "type": "list",
            "name": "opcao",
            "message": "Escolha a opção desejada:",
            "choices": ["Depositar", "Sacar", "Ver Extrato", "Sair"],
        }
    ]

    while True:
        # Executa o prompt interativo
        resposta = prompt(perguntas)
        
        # Se o usuário cancelar com Ctrl+C, o retorno pode ser vazio, evitamos erro com um check
        if not resposta:
            print("\nPrograma encerrado!")
            break

        escolha = resposta.get("opcao")

        match escolha:
            case "Depositar":
                try:
                    valor = float(input("Digite o valor a ser depositado: R$ "))
                    depositar(valor)
                except ValueError:
                    print("\n[ERRO]: Digite apenas números válidos para o valor.")
            
            case "Sacar":
                try:
                    valor = float(input("Digite o valor a ser sacado: R$ "))
                    sacar(valor)
                except ValueError:
                    print("\n[ERRO]: Digite apenas números válidos para o valor.")
            
            case "Ver Extrato":
                exibir_extrato()
            
            case "Sair":
                print("\nPrograma encerrado! Obrigado por utilizar nossos serviços.")
                break

def depositar(valor):
    global saldo, extrato

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n[SUCESSO]: Depósito realizado com sucesso!")
    else:
        print("\n[ERRO]: O valor informado deve ser maior que zero (0)!")

def sacar(valor):
    global saldo, extrato, numeroSaques

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numeroSaques >= LIMITE_SAQUE

    if excedeu_saldo:
        print("\n[ERRO]: Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print(f"\n[ERRO]: Operação falhou! O valor do saque excede o limite permitido (R$ {limite:.2f}).")
    elif excedeu_saques:
        print("\n[ERRO]: Operação falhou! Número máximo de saques diários excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numeroSaques += 1
        print("\n[SUCESSO]: Saque realizado com sucesso!")
    else:
        print("\n[ERRO]: O valor informado deve ser maior que zero (0)!")

def exibir_extrato():
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")

if __name__ == "__main__":
    main()