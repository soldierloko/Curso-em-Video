#Crie um programa que fala o computador jogar Jokenpô com você

from random import randint
from time import sleep



vJogador = int(input('Suas Opções: '
                    '\n[ 0 ] PEDRA'
                    '\n[ 1 ] PAPEL'
                    '\n[ 2 ] TESOURA '))

itens = ('Pedra','Papel','Tesoura')

vComputador = randint(0,2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('-='*11)
print('Computador jogou {}'.format(itens[vComputador]))
print('Jogador jogou {}'.format(itens[vJogador]))
print('-='*11)

if vComputador ==0:
    if vJogador == 0:
        print('Empate')
    elif vJogador == 1:
        print('Jogador Vence')
    elif vJogador == 2:
        print('Computador Vence')
    else:
        print('Jogada Inválida!')
elif vComputador ==1:
    if vJogador == 0:
        print('Computador Vence')
    elif vJogador == 1:
        print('Empate')
    elif vJogador == 2:
        print('Jogador Vence')
    else:
        print('Jogada Inválida!')
elif vComputador ==2:
    if vJogador == 0:
        print('Jogador Vence')
    elif vJogador == 1:
        print('Computador Vence')
    elif vJogador == 2:
        print('Empate')
    else:
        print('Jogada Inválida!')