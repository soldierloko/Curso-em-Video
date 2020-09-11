#Refaço o desafiop 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

vTabuada = int(input('Digite um valor para a taboada: '))

cont = 1
for i in range(1,11):
    print('{} x {} = {}'.format(vTabuada,i,vTabuada*i))