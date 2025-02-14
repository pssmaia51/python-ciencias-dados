import random
from os import system, name

# Função para limpar a tela
def limpa_tela():
    comando = 'cls' if name == 'nt' else 'clear'
    system(comando)

# Quadro (tabuleiro) da Forca
board = [
    '''
    +---+
    |   |
        |
        |
        |
        |
    =======''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =======''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =======''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =======''', '''
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =======''', '''
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =======''', '''
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    ======='''
]

# Classe Carrasco
class Carrasco:
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_escolhidas = []

    def adivinhar_letra(self, letra):
        if letra in self.palavra and letra not in self.letras_escolhidas:
            self.letras_escolhidas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True

    def jogo_terminou(self):
        return self.jogador_venceu() or len(self.letras_erradas) >= len(board) - 1

    def jogador_venceu(self):
        return '_' not in self.obter_palavra_oculta()

    def obter_palavra_oculta(self):
        return ''.join(letra if letra in self.letras_escolhidas else '_' for letra in self.palavra)

    def mostrar_status_jogo(self):
        print(board[len(self.letras_erradas)])
        print('\nPalavra: ' + self.obter_palavra_oculta())
        print('Letras erradas: ' + ', '.join(self.letras_erradas))
        print('Letras corretas: ' + ', '.join(self.letras_escolhidas))

# Função para escolher uma palavra aleatória
def escolher_palavra():
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    return random.choice(palavras)

# Função principal
def main():
    limpa_tela()
    jogo = Carrasco(escolher_palavra())

    while not jogo.jogo_terminou():
        jogo.mostrar_status_jogo()
        tentativa = input('\nDigite uma letra: ').lower()

        # Valida a entrada para ter apenas um caractere alfabético
        if len(tentativa) != 1 or not tentativa.isalpha():
            print('Entrada inválida. Digite apenas uma letra.')
            continue

        jogo.adivinhar_letra(tentativa)

    jogo.mostrar_status_jogo()
    if jogo.jogador_venceu():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print(f'A palavra era: {jogo.palavra}')

    print('\nFoi bom jogar com você! Agora vá estudar!\n')

if __name__ == "__main__":
    main()

#----End Of Cell----


#----End Of Cell----

