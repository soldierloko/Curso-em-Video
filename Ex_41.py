#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 20 anos: SÊNIOR
#Acima: MASTER

from datetime import date

vAno = int(input('Digite o ano de Nascimento: '))
vAnoAtual = date.today().year

vQtdeAnos = vAnoAtual - vAno

if vQtdeAnos >= 20:
    print('Categoria SÊNIOR!')
elif vQtdeAnos >=19:
    print('Categoria JUNIOR!')
elif vQtdeAnos >=14:
    print('Categoria INFANTIL!')
else:
    print('Categoria MIRIM!')
