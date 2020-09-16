#Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando estrutura While

termo = int(input('Primeiro Termo: '))
razao = int(input('Qual a Razão: '))

cont = 1

while cont <=10:
    print('{} - '.format(termo),end='')
    termo +=razao
    cont +=1


