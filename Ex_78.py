#Faça um programa que leia 5 valores numéricos e quarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
i = 0
while True:
    if i < 5:
        n = int(input("Digite um número: "))
        lista.append(n)
        i+=1
    else:
        break

Maior = max(lista)
Menor = min(lista)

print(f'O maior valor da Lista é {Maior} e esta na posição {lista.index(Maior)+1}')
print(f'O menor valor da Lista é {Menor} e esta na posição {lista.index(Menor)+1}')