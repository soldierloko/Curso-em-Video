#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
#Qual é o total gasto na compra
#Quantos produtos custam mais de 1000
#Qual é o nome do produto mais barato

menorprod = ' '
preco = total  = menor  = qtde = 0

while True:

    produto = input('Digite o Produto: ')
    preco = int(input('Digite o Preço: '))

    total += preco
    if preco > 1000:
        qtde += 1

    if menor == 0:
        menor = preco
    if menor < preco:
        menorprod = produto
        menor = preco
    conf = input('Deseja continuar? [S/N]').strip().upper() [0]
    if conf in 'N':
        break

print(f'O total gasto na compra foi {total}')
print(f'{qtde} produtos custam mais que 1000')
print(f'O produto mais barato é o {menorprod}')