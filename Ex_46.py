#Faça Um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles

from time import sleep

for i in range(10,0,-1):
    sleep(1)
    print(i)

print('Feliz Ano Novo!!!')