#Crie um programa que leia vários números interios pelo teclado. O programa só vai parar quando o usuário digitar o valor 999. que é a condição de parada. No final, mostr quantos números foram digitados e qual foi a soma entre eles.

n = 0
cont = 0
soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    else:
        soma  += n
        cont += 1
print(f'A Soma dos números digitados foi {soma} e quantidade de números digitados foram {cont}')