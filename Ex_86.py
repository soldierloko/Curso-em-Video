#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos do teclado
#No final mostre a matriz na tela, com a formatação correta
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um Valor para [{l}, {c}]: ')) 

print('-=' *30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end='')
    print()