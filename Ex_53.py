#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços 

frase = str(input('Digite uma frase: ')).strip().upper()
#Separo em coleção
palavra = frase.split()
#Depois eu junto as palavras 
junto = ''.join(palavra)

inverso = ''

for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]

if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo!')

