#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, e mostre:
#Quantas vezes apareceu o número 9
#Em que posição foi digitado o primeiro valor 3
#Quais foram os números pares

n = (int(input('Digite um número: ')),
        int(input('Digite um número: ')),
        int(input('Digite um número: ')),
        int(input('Digite um número: ')))

print(f'Você Digitou os valores {n}!')
print(f'O Valor 9 apareceu {n.count(9)}')
if 3 in n:
    print(f'O valor 3 apareceu na {núm.index(3)+1} posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição', end='')
for i in n:
    if i % 2 ==0:
        print(n,end='')

