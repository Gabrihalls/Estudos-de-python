print('-----------------------SÉTIMO DESAFIO-----------------------')
nome = input('Olá , aluno , por favor digite seu nome:')
n1 = float(input('{}, qual foi sua média em Literatura nesse bimestre?:'.format(nome)))
n2 = float(input('{}, qual foi sua média em Redação nesse bimestre?:'.format(nome)))
n3 = float(input('{}, qual foi sua média em Gramática nesse bimestre?:'.format(nome)))
m = (n1+n2+n3)/3
print('{}, sua média em português nesse bimestre vai ser: {}'.format(nome,m))
