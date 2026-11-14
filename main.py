saldo = 0.0
limite = 500
extrato = ""
numeroSaques = 0
LIMITE_SAQUE = 3

def main():
    while True:
        
        print("""
        1. depositar
        2. sacar
        3. extrato
        4. sair
        """)

        try:
            opc = int(input("Digite sua opção: "))

            match opc:
                case 1:
                    try:
                        valor = int(input("Digite o valor a ser adicionado"))
                        depositar()
                    except ValueError:
                        print("DIgite apenas núemros")
                case 2:
                    sacar()
                case 3:
                    extrato()   
                case 4:
                    exit("Programa encerrado!")
                case _:
                    print("ERRROR!: Digite um valor entre 1 e 4.")
            
        except ValueError:
            print("Error!: Digite apenas números.")
        
def depositar(valor):
    global saldo
    global extrato

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Digite um valor maior que 0 (zero)!")

def sacar(valor):
    global saldo
    global extrato
    global numeroSaques
    global LIMITE_SAQUE

    if numeroSaques < LIMITE_SAQUE or valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numeroSaques += 1
    else:
        if numeroSaques > LIMITE_SAQUE:
            print("Limite de saques excedido!")
        elif valor < 0:
            print("Digite um valor maior que 0 (zero)!")

def extrato():



if __name__ == "__main__":
    main()