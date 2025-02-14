#!/usr/bin/env python
# coding: utf-8

# ### Jogo da Forca - Projeto 01

# In[21]:


import random
from os import system, name

# Função para limpar a tela
def limpar_tela():
    # Windows
    if name == 'nt':
        _ = system('cls')
    # macOS ou Linux    
    else:
        _ = system('clear')

# Função principal do jogo
def game():
    
    limpar_tela()
    print("\nBem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra:\n")
    
    # Lista de palavras do jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    
    # Escolher uma palavra aleatoriamente
    palavra = random.choice(palavras).lower()
    
    # Lista para as letras descobertas (usando list comprehension)
    letras_descobertas = ['_' for letra in palavra]
    tentativas_restantes = 6
    letras_erradas = []
    
    # Loop enquanto houver tentativas e a palavra não for completamente descoberta
    while tentativas_restantes > 0 and "_" in letras_descobertas:
        print("\nPalavra: ", ' '.join(letras_descobertas))
        print(f"Tentativa(s) restantes: {tentativas_restantes}")
        print("Letras erradas: ", ' '.join(letras_erradas))
        
        # Solicitar letra do jogador
        tentativa = input("Digite uma letra: ").lower()
        
        # Verificar se a letra já foi digitada
        if tentativa in letras_erradas or tentativa in letras_descobertas:
            print("Você já tentou essa letra, escolha outra.")
            continue
        
        # Verificar se a tentativa está na palavra
        if tentativa in palavra:
            # Atualizar as letras descobertas
            for index, letra in enumerate(palavra):
                if tentativa == letra:
                    letras_descobertas[index] = letra
        else:
            # Diminuir o número de tentativas e adicionar a letra às erradas
            tentativas_restantes -= 1
            letras_erradas.append(tentativa)
        
        # Verificar se a palavra foi descoberta
        if "_" not in letras_descobertas:
            print("\nParabéns! Você venceu, a palavra era:", palavra)
            break

    # Se acabarem as tentativas e a palavra não for descoberta
    if "_" in letras_descobertas:
        print("\nVocê perdeu! A palavra era:", palavra)

# Bloco principal (main)
if __name__ == "__main__":
    game()
    print("\nParabéns pelo desenvolvimento do projeto!\n")