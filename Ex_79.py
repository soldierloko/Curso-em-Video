#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente


lista = []
n = 0

while n != 99:

    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        n = int(input("Digite 99 para parar ou qualqer número para continuar: "))
    else:
        print('Número já cadastrado!')
        n = int(input("Digite 99 para parar ou qualqer número para continuar: "))

print(sorted(lista))