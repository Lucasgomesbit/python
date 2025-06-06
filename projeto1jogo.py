import random
from os import system, name

def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def game():
    limpa_tela()
    print('\nBem-vindo(a) ao jogo da forca!')
    print('Adivinhe a palavra abaixo:\n')

    palavras = ['cruzeiro', 'flamengo', 'barcelona', 'internacional', 'goias', 'manchester city']
    palavra = random.choice(palavras)
    letras_descobertas = ['_' if letra != ' ' else ' ' for letra in palavra]  # preserva espaços

    chances = 6
    letras_erradas = []

    while chances > 0:
        print('\n' + ' '.join(letras_descobertas))
        print(f'Chances restantes: {chances}')
        print('Letras erradas:', ' '.join(letras_erradas))

        tentativa = input('\nDigite uma letra: ').lower()

        if tentativa in palavra:
            for index, letra in enumerate(palavra):
                if tentativa == letra:
                    letras_descobertas[index] = letra
        else:
            if tentativa not in letras_erradas:
                chances -= 1
                letras_erradas.append(tentativa)

        if '_' not in letras_descobertas:
            print('\nVocê venceu! A palavra era:', palavra)
            break
    else:
        print('\nVocê perdeu! A palavra era:', palavra)

# Chama o jogo
game()
