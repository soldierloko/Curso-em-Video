#Desenvolvas uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18,5: ABAIXO DO PESO
#Entre de 18,5 e 25: PESO IDEAL
#Entre de 25 e 30: SOBRE PESO
#Entre de 30 e 40: OBESIDADE
#Acima de 40: OBESIDADE MORBIDA

vPeso = float(input('Digite seu peso: '))
vAltura = float(input('Digite sua altura: '))

vIMC = vPeso/(vAltura*vAltura)

if vIMC >=40:
    print('OBESIDADE MÓRBIDA')
elif vIMC >=30:
    print('OBESIDADE')
elif vIMC >=25:
    print('SOBRE PESO')
elif vIMC >=18.5:
    print('PESO IDEAL')
else:
    print('ABAIXO DO PESO')