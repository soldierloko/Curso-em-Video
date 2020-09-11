#Crie um programa que leia o ano de nascimento de sete pessoas. No Final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

from datetime import date

cont1 = 0
cont2 = 0
vAnoAtual = date.today().year
for i in range(1,8):
    ano = int(input('Digite o ano de nascimento da {} pessoa! '.format(i)))
    if (vAnoAtual - ano) < 18:
        cont1 += 1
    else:
        cont2 += 1
print('O total de pessoas menores de idade é {}, e o total de pessoas maiores de idade são {}!'.format(cont1,cont2))
