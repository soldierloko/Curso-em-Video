#Crie um programa que leia 2 valores e mostre um menu na tela:

#[1] Somar
#[2] Multiplicar
#[3] Maior
#[4] Novos Números
#[5] Sair do Programa


#Seu programa deverá realizar a operação solicitada em cada caso

v1 = int(input('Primeiro Valor: '))
v2 = int(input('Segundo Valor: '))

op = 0
while op != 5:
    print('''[ 1 ] Somar
             [ 2 ] Multiplicar
             [ 3 ] Maior
             [ 4 ] Novos Números
             [ 5 ] Sair do Programa''')
    op = int(input('Qual a sua opção: '))
    if op == 1:
        print('A soma entre {} e {} é {}'.format(v1,v2,v1+v2))
    elif op == 2:
        print('A multiplicação entre {} e {} é {}'.format(v1,v2,v1*v2))
    elif op == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('O Maior número entre {} e {} é {}'.format(v1,v2,maior))
    elif op == 4:
        v1 = int(input('Primeiro Valor: '))
        v2 = int(input('Segundo Valor: '))
    elif op == 5:
        print('Finalizando...')

    else:
        print('Opção Inválida, tente novamente!')
    print('=-='*10)
print('Fim do Programa, volte sempre!')