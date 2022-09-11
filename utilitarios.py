from random import choice
import string


def menu():
    print('-=' * 20)
    print('       \033[42m*** GERADOR DE SENHAS ***\033[m')
    print('-=' * 20)
    print("""OPÇÕES:
    [1] - Gerar Senha.
    [2] - Mostrar senhas salvas.
    [0] - Encerrar Programa.
    """)
    print('-=' * 20)


def gera():
    """Gera a senha com 8 digitos"""
    letters = string.ascii_letters
    numbers = string.digits
    symbols = '@#&!?'
    characters = letters + numbers + symbols
    password = ''

    for num in range(0, 8):
        digit = choice(characters)
        password += digit

    return password


def formata_erro(msg):
    """Formata menssagem, letras saem da cor vermelha"""
    print(f'\n         \033[31m{msg}\033[m\n')


def formata_outros(msg):
    """Formata menssagem, letras saem da cor verde"""
    print(f'\n         \033[32m{msg}\033[m\n')


def save_password(name, password):
    """Salva a senha em um arquivo txt"""
    with open('Passwords.txt', 'a') as file:
        file.write(name + ': ' + password + '\n')


def show_password():
    """Mostra senhas salvas"""
    with open('Passwords.txt', 'r') as file:
        for value in file:
            print()
            print(value)
            print('~' * 20)
