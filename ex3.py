import random

def ler_palavras(arquivo):
    with open(arquivo, 'r') as f:
        palavras = f.read().splitlines()
    return palavras

def jogar(palavras):
    palavra = random.choice(palavras)
    tentativas = 6
    letras_descobertas = ['_' for _ in palavra]
    letras_tentadas = []
    
    while tentativas > 0:
        print('Palavra:', ' '.join(letras_descobertas))
        print('Letras tentadas:', ' '.join(letras_tentadas))
        tentativa = input('Digite uma palavra: ').lower()
        
        if tentativa == palavra:
            print('Parabéns! Você venceu!')
            return
        
        letras_tentadas.append(tentativa)
        tentativas -= 1
        
        for i, letra in enumerate(palavra):
            if letra in tentativa:
                letras_descobertas[i] = letra
    
    print('Você perdeu! A palavra era:', palavra)

palavras = ler_palavras('lista_palavras.txt')
jogar(palavras)
