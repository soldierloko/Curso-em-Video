# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zera até vinte
#Seu programa deverá ler um número pelo teclado entre 0 e 20 e mostra-lo por exenso

tp = 'Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezesete','Dezoito','Dezenove','Vinte'

while True:
   
    try:
        n = int(input('Digite um número entre 0 e 20: '))
        if n >= 0 and n <= 20:
            print(f'Você digitou o número {tp[n]}')
            break
    except:
        continue    
