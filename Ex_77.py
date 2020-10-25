#Crie um programa que tenha várias palavras (Não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais
palavras = ('aprender', 'programar', 'liguagem', 'python'
            'curso', 'gratis' , 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro') 

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
