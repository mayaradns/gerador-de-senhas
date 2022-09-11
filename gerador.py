from utilitarios import *

while True:
    menu()
    try:
        choice = int(
            input('Digite o número correspondente a opção desejada: '))
        if choice == 1:
            password = gera()
            print(f'\nSenha: \033[33m{password}\033[m\n')
            save = input(
                'Digite "s" para salvar ou pressione enter para continuar: ').lower().strip()
            if save == 's':
                name = input('Digite o site da senha: ')
                save_password(name, password)
                formata_outros('## Senha salva!!! ##')
            else:
                print('\n    ~~~ Senha não foi salva! ~~~\n')
        elif choice == 2:
            try:
                show_password()
                print()
            except FileNotFoundError:
                formata_erro('Não existe senha salva.')
        elif choice == 0:
            break
        else:
            formata_erro('Opção inválida!!!')
    except ValueError:
        formata('Opção inválida!!!')
