print('-----------------------DÉCIMO-SEGUNDO DESAFIO-----------------------')
nome = input('Olá , qual seu nome?')
p = float(input('{}, qual o valor do produto que você quer desconto?'.format(nome)))
d = p-(p*5/100)
print('{}, conseguimos te dar 5% de desconto , o valor passou de R${:.2f}, para R${:.2f}'.format(nome,p,d))