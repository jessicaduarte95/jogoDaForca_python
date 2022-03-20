
# Jogo da Forca

import random
from random import choice

forca = [
    "+----+\n|    |\n|\n|\n|\n=====",
    "+----+\n|    |\n|    O\n|\n|\n=====",
    "+----+\n|    |\n|    O\n|    |\n|\n=====",
    "+----+\n|    |\n|    O\n|   /|\n|\n=====",
    "+----+\n|    |\n|    O\n|   /|\ \n|\n=====",
    "+----+\n|    |\n|    O\n|   /|\ \n|   /\n=====",
    "+----+\n|    |\n|    O\n|   /|\ \n|   / \ \n====="
]
    

# Classe 
class jogo:
    def __init__(self,palavra):
        self.palavra = palavra
        print(forca[0])
        print("Palavra: ")
        
    # Método para realizar o jogo
    def adivinhar(self):
        letra = ''
        acertos = 0
        erros = 0
        letrasCorretas = ''
        letrasErradas = ''
        while acertos != (len(self.palavra)) and erros != 6:
            mensagem = ''
            for letra in self.palavra:
                if letra in letrasCorretas:
                    mensagem += letra + " "
                else:
                    mensagem += '- '
            print(mensagem)
            print("Letras Corretas: " + letrasCorretas)
            print("Letras Erradas: " + letrasErradas)

            letra = (input("Digite uma letra: "))

            if letra in letrasCorretas+letrasErradas:
                print("Você já digitou essa letra.")
                continue
            if letra in self.palavra:
                letrasCorretas += letra
                acertos += self.palavra.count(letra)
            else:
                letrasErradas += letra
                erros += 1
            print(forca[erros])
        if acertos == len(self.palavra):
            print('Jogador venceu.')
            print('Palavra Correta: ' + self.palavra)
        elif erros == 6:
            print("Você perdeu.")
            print('Palavra Correta: ' + self.palavra)
         
# Selecionando Palavras 

def selecionarPalavras():
    with open('C:\\Users\\jessica\\Documents\\Treino_python\\jogoDaForca_python\\palavras.txt') as f:
        banco = f.read()
        bancoLista = banco.split('\n')
    palavra = choice(bancoLista)
    jogar = jogo(palavra)
    jogar.adivinhar()


# Função para chamar as funções

def main():
    selecionarPalavras()
    
# Executa o programa

if __name__ == "__main__":
	main()
