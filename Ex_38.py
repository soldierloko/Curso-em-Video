#Escreva umn programa que leia 2 números inteiros e compare-os, mostrando na tela uma mensagem:
#O Primeiro valor é maior
#O Segundo valor é menor
#Ambos os valores são iguais

vn1 = int(input("Digite o Primeiro Valor: "))
vn2 = int(input("Digite o Segundo Valor: "))


if vn1>vn2:
    print('O primeiro Valor {} é maior que o segundo {}'.format(vn1,vn2))
elif vn1<vn2:
    print('O segundo Valor {} é maior que o primeiro {}'.format(vn2,vn1)
    )
else:
    print('Ambos os valores são iguais!')