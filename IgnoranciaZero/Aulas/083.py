def main():
    senha = ""
    while True:
        escolha = input("Digete S para definir uma senha ou V para verificar a senha ou E para sair: ").upper()
        if escolha[0] == "S":
            while True:
                senha = (input("Digete a nova senha(Apenas numeros): "))
                if not senha.isdigit():
                    print("\nSenha invalida")
                else:
                    break

        elif escolha[0] == "V":
            tentativas = input("Digete sua senha: ")
            try:
                if all([senha[i] == tentativas[i] and len(senha) == len(tentativas) for i in range(len(senha))]):

                    print("Senha certa")
                else:
                    print("Senha errada")
            except:
                print("Senha errada")

        elif escolha[0] == "E":
            break


main()
