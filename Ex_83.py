#Crie um programa onde o usuário digite uma expressão qualquer que use parentesês. 
#Seu aplicativo deverá analisar se a expressão passada está com os parentesês abertos e fechados na ordem correta

expr = input("Digite a expressão: ")

pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')'
        if len(pilha) > 0:
            pilha.pop
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print("Sua Expressão esta válida")
else:
    print("Sua Expressão não esta válida")