#Faça um programa que leia o peso de cinco pessoas. No final, mopstre qual foi o maior e o menor peso lidos
vMaior = 0
vMenor = 0

for i in range (1,6):
    vPeso = float(input('Digite o peso da {} pessoa: '.format(i)))
    if i== 1:
        vMaior = vPeso
        vMenor = vPeso
    else:
        if vPeso > vMaior:
            vMaior = vPeso
        elif vPeso < vMenor:
            vMenor = vPeso

print('O Maior peso foi {}!'.format(vMaior))
print('O Menor peso foi {}!'.format(vMenor))