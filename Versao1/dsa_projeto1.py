# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 1

# Import
import random
from os import system, name

# Função para limpar a tela a cada execução

def limpa_tela():
    #Windows
    if name == 'nt':
        _ = system('cls')
    # Mac ou Linux
    else:
        _ = system('clear')

# Função
def game():
    limpa_tela()
    
    print('\nBem-vindo(a) ao jogo da forca!')
    print('Adivinhe a palavra abaixo:\n')
    
    # Lista de palavras
    
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    
    # Escolhe aleatoriamente uma palavra
    palavra = random.choice(palavras)
    
    letras_decobertas = ['-' for letras in palavra]
    
    chances = 6
    
    #Lista para letras erradas
    letras_erradas = []
    
    # Loop enquanto chances for maior que zero
    while chances > 0:
        print(' '.join(letras_decobertas))
        print('\nChances restantes: ',chances)
        print('Letras erradas: ', ''.join(letras_erradas))
        
        tentativa = input('\nDigite uma letra: ').lower()
        
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_decobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
        if '-' not in letras_decobertas:
            print('\nVocê venceu, a palavra era :', palavra)
            break
    if '-' in letras_decobertas:
        print('Você perdeu, a palavra era: ', palavra)
if __name__ == '__main__':
    game()
