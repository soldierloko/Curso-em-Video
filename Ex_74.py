 #Crie um programa que vai gerar cinco números aleatórios e colocar em um tupla
 #Depois, mostra a listagem de números gerados e tambem indique o menor e o maior valor que estão na tupla

from random import randint

n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print(f'Sorteei os valores {n}')
print(f' O maior valor sorteado foi {max(n)}')
print(f' O menor valor sorteado foi {min(n)}')

