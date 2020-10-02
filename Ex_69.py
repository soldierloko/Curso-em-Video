#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se p usuário quer ou não continuar. No final, mostre:
#Quantas pessoas tem mais de 18 anos
# Quantos homens foram cadastrados
#Quantas mulheres tem menos de 20 anos

maiores = homens = mulheres = 0

while True:

    idade = int(input('Digite a Idade: '))
    sexo = input('Digite a Sexo [M/F]: ').strip().upper()

    if idade >=18:
        maiores +=1
        
    if sexo in ('M'):
        homens += 1

    if sexo in ('F') and idade <20:
        mulheres +=1

    per = input('Quer continuar o cadastramento? [S/N]').strip().upper() [0]
    if per in 'N':
        break    

print(f'Total de pessoas com mais de 18 anos {maiores}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')