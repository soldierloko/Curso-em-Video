#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

#A média da idade do grupo
#Qual é o nome do homem mais velho
#Quantas mulheres tem menos de 20 anos

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher20 = 0
for i in range(1,5):
    vNome = input('Digite o Nome da {} pessoa: '.format(i)).strip()
    vIdade = int(input('Digite a Idade da {} pessoa: '.format(i)))
    vSexo = input('Digite M para masculino e F para Feminino da {} pessoa: '.format(i)).strip()
    somaidade += vIdade
    if i == 1 and vSexo in 'Mm':
        maioridadehomem = vIdade
        nomevelho = vNome
    if vSexo in 'Mn' and vIdade > maioridadehomem:
        maioridadehomem = vIdade
        nomevelho = vNome
    if vSexo in 'Ff' and vIdade > 20:
        mulher20 += 1


mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O Homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher20))
