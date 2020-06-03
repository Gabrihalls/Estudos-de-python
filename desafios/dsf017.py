import math
print('-'*20,'DECIMO-SÉTIMO DESAFIO','-'*20)
nome = input('Olá , digite seu nome:')
print('{}, bem vindo a minha resolução de triângulos retângulos!'.format(nome))
ca = int(input('{}, digite o valor do cateto adjacente: '.format(nome)))
co = int(input('Agora digite o valor do cateto oposto: '))
h = math.hypot(ca,co)
print('{} , o valor da sua hipotenusa é : {}'.format(nome,h))