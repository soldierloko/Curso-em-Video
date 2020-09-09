#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#A vista Dinheiro ou Cheque: 10% de Desconto
#A vista no cartão: 5% de Desconto
#2x No cartão: preço normal
#3x ou mais no cartão: 20% de juros

vProduto =  float(input('Digite o valor do Produto: '))
vCondicao =  int(input('Digite a condiçaõ de Pagamento:' 
                        '\n1 à vista (Dinheiro/Cheque)'
                        '\n2 à vista no cartão'
                        '\n3 2 x no cartão'
                        '\n4 3 x ou mais no cartão '))

if vCondicao == 4:
    print('Valor total do produto {}'
            '\nValor do Acrescimo {} '
            '\nNo parcelamento acima de 2x Acrescenta-se 20%!'.format(vProduto+(vProduto*0.2),(vProduto*0.2)))
elif vCondicao == 3:
    print('Valor total do produto {}!'.format(vProduto))
elif vCondicao == 2:
    print('Valor total do produto {}'
            '\nValor do Desconto {}'
            '\nÀ Vista no Cartão 5% de Desconto!'.format(vProduto-(vProduto*0.05),(vProduto*0.05)))
else:
    print('Valor total do produto {}'
            '\nValor do Desconto {}'
            '\nÀ Vista no Cartão 10% de Desconto!'.format(vProduto-(vProduto*0.1),(vProduto*0.1)))
