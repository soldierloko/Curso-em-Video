#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista
#No final mostre:
#Quantas pessoas foram cadastradas
#Uma listagem com as pessoas mais pesadas
#Uma listagem com as pessoas mais leves

galera = []
individuo = []
cont = 0

while True:
    nome = input("Digite um nome: ")
    peso = input("Digite peso: ")
    individuo.append(nome)
    individuo.append(peso)

    galera.append(individuo[:])
    individuo.clear()
    cont +=1
    
    if input("Deseja continuar? [S/N]").upper() == "N":
        break

print(f'A quantidade de pessoas cadastradas foram {cont}')

