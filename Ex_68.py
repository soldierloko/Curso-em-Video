#Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

v = 0
while True:
    print('===='*10)
    print('Vamos Jogas Par ou Impar!')
    print('===='*10)
    jogador = int(input('Diga um valor? :'))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('par ou impar? ').strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}.Total {total}')
    if tipo == 'P':
        if total %2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo =='I':
        if total %2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos Jogar novamente?')
print(f'GAME OVER! Você venceu {v} vezes.')