import random
from os import system, name

#----End Of Cell----

import random
from os import system, name

# Função para limpar a tela
def limpa_tela():
    if name == 'nt':  # Windows
        _ = system('cls')
    else:  # Mac ou Linux
        _ = system('clear')

# Tabuleiro para exibir o estado do jogo
board = ['''
+---+
|   |
    |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
+---+
|   |
O   |
/|   |
     |
     |
=========''', '''
+---+
|   |
O   |
/|\  |
     |
     |
=========''', '''
+---+
|   |
O   |
/|\  |
/    |
     |
=========''', '''
+---+
|   |
O   |
/|\  |
/ \  |
     |
=========''']

# Classe Carrasco
class Carrasco:
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_escolhidas = []

    def guess(self, letra):
        """Processa a tentativa do jogador e atualiza letras corretas ou incorretas."""
        if letra in self.palavra and letra not in self.letras_escolhidas:
            self.letras_escolhidas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True

    def hangman_over(self):
        """Verifica se o jogo terminou."""
        return self.hangman_won() or (len(self.letras_erradas) == 6)

    def hangman_won(self):
        """Verifica se o jogador venceu."""
        return '_' not in self.mostrar_palavra()

    def mostrar_palavra(self):
        """Mostra a palavra com as letras corretas reveladas e '_' nas letras não adivinhadas."""
        return ''.join([letra if letra in self.letras_escolhidas else '_' for letra in self.palavra])

    def print_game_status(self):
        """Imprime o estado atual do jogo."""
        print(board[len(self.letras_erradas)])
        print(f'\nPalavra: {self.mostrar_palavra()}')
        print(f'Letras erradas: {" ".join(self.letras_erradas)}')
        print(f'Letras corretas: {" ".join(self.letras_escolhidas)}')
        print(f'Tentativas restantes: {6 - len(self.letras_erradas)}')

# Função para escolher uma palavra aleatoriamente
def rand_palavra():
    """Retorna uma palavra aleatória de uma lista."""
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    return random.choice(palavras)

# Função principal
def main():
    limpa_tela()
    game = Carrasco(rand_palavra())

    while not game.hangman_over():
        game.print_game_status()

        # Solicita a entrada do usuário, validando que é uma única letra alfabética
        user_input = input('\nDigite uma letra: ').lower()
        if len(user_input) != 1 or not user_input.isalpha():
            print("Entrada inválida. Digite apenas uma letra.")
            continue

        # Processa o palpite do jogador
        game.guess(user_input)

    # Verifica o status final do jogo e exibe a palavra completa
    game.print_game_status()
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print(f'\nGame over! Você perdeu. A palavra era "{game.palavra}".')

    print('\nFoi bom jogar com você! Agora vá estudar!\n')

if __name__ == "__main__":
    main()

#----End Of Cell----

