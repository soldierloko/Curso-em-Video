#Melhore o Jogo Desafio 028 onde o computador vai pensar em um n´úmro entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint

vPc = randint(0,10)

print('Acabei de pensar em um númerp entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

acertou = False
palpite = 0

while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite += 1
    if jogador == vPc:
        acertou = True
    else:
        if jogador < vPc:
            print('Mais...tente mais uma vez!')
        else:
            print('Menos...tente mais uma vez!')
    

print('Acertou com {} Tentativas!'.format(palpite))