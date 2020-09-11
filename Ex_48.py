#Faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que se encontram no intervalo de 1 até 500

ac = 0
cont = 0

for i in range(1,501,2):
    if i % 3 == 0:
        ac += i
        cont += 1
        print(i, end = ' ')

print('A Soma de todos os {} valores solicitados é {}'.format(cont,ac))
