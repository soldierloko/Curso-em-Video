#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão


vPa = int(input('Digite o valor do termo: '))
vRazao = int(input('Digite o valor da razão: '))
dec = vPa + (10-1) * vRazao

for i in range(vPa,dec + vRazao ,vRazao):
    print('{} > '.format(i), end= ' ')

print('ACABOU')