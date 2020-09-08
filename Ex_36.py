#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O Programa vai perguntar o valor da casa, o slário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

vCasa = float(input('Qual o Valor da casa? '))
vSalario = float(input('Qual o Valor do Salário do requerente? '))
vAnos = int(input('Quantos anos a pagar? '))

vPrestacao = vCasa/(vAnos*12)

if vPrestacao > (vSalario*0.3):
    print("Empréstimo Negado!"
    "\nValor da prestação {:.2f} é superior a 30% da renda".format(vPrestacao))
else:
    print('Emprestimo aprovado!'
            '\nValor do Empréstimo: {:.2f} reais'
            '\nQtde de Anos a pagar: {} '
            '\nValor da Parcela: {:.2f} reais'.format(vCasa,vAnos,vPrestacao))
            