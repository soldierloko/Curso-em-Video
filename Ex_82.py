#Crie um programa que vai ler vários números e colocar em uma lista
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e impares digitados, respectivamentes
#Ao final, mostre o conteúdo das 3 listas geradas

lista = []
par = []
impar = []


while True:
    n = int(input("Digite um número: "))
    lista.append(n)

    if n % 2 ==0:
        par.append(n)
    else:
        impar.append(n)

    if input("Deseja continuar? [S/N]").upper() == "N":
        break

print(f"Os números digitados foram {lista}")
print(f"Os números pares digitados foram {par}")
print(f"Os números impares digitados foram {impar}")