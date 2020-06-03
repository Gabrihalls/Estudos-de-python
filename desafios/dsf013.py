print('-----------------------DÉCIMO-TERCEIRO DESAFIO-----------------------')
nome = input('Olá , bem vindo a central eletrônica da empresa \nQual seu nome?:')
sa = float(input('{}, você deseja ter um reajuste em seu salário?\nSe sim ,digite o valor de seu salário:'.format(nome)))
sn = sa*1.15
print('{}, conseguimos um reajuste de 15% em seu salário , que passou de R${:.2f} para R${:.2f}, espero que esteja satisfeito'.format(nome,sa,sn))