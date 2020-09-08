#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar
#Se é a hora de se alistar
#Se á passou do tempo do alistamento

#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date

vAno = int(input('Qual é o ano do seu nascimento? '))
vAnoAtual = date.today().year


vAnos = vAnoAtual - vAno

if vAnos < 18:
    print('Faltam {} anos para o seu alistamento!'.format(18 - vAnos))
elif vAnos == 18:
    print('Você deve se alistar este ano!')
else:
    print('Você deveria ter se alistado a {} anos atrás!'.format(vAnos-18))

    