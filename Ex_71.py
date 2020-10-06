#Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

#Obs: Considere que o caixa possui cédulas de 50, 20, 10 e 1


valor = int(input('Qual valor você quer sacar? '))
total = valor
ced = 50
totalced = 0

while True:
    #Verifica se o total do valor é maior ou igual a 50
    if total>=ced:
        #Aqui retira a cédula do total para continuar o loop
        total -=ced
        #Conta a quantidade de cédulas de 50
        totalced += 1
    else:
        if totalced >0:
            print(f'Total de {totalced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
        
