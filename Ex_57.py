#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto

vSexo = input('Informe seu Sexo [M/F]: ').upper().strip()[0]
while vSexo not in 'MF':
    vSexo = input('Informe seu Sexo [M/F]: ').upper().strip()[0]
  
print('Sexo {} registrado com sucesso!'.format(vSexo))