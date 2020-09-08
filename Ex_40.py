#Crie um programa que leia 2 notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# <5: REPROVADO
#>5 E <7: RECUPERAÇÃO
#>6,59: APROVADO

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))

vMedia =  (n1+n2)/2

if vMedia < 5:
    print('REPROVADO')
elif vMedia >= 5 and vMedia<=6.59:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')

