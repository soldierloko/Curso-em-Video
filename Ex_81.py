#Crie um programa que avi ler vários números e colocar em uma lista
#Depois disso, mostre:
#Quantos números foram digitados
#Lista de valores, ordenada de forma decrescente
# Se o valor 5 foi digitado e está ou não na lista

lista = []

while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    
    if input("Deseja continuar? [S/N]").upper() == "N":
        break

lista.sort(reverse=True)
print(f"Foram digitados {len(lista)} números")
print(f"A Lista em ordem Decrescente fica: {lista}")
if 5 in lista:
    print("O Número 5 esta na lista!")
else:
    print("O Número 5 não esta na lista!")