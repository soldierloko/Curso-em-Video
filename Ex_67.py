#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo



while True:
    cont = 1
    n = 0

    n = int(input('Digite um número: '))
    
    if n < 0:
        break
    else:
        while cont <= 10:
            print(f'{n} x {cont} = {cont*n}')
            cont += 1
