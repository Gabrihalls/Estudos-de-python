print('-'*20,'DECIMO-QUARTO DESAFIO','-'*20)
nome = input('Olá, qual o seu nome?:')
c = float(input('{}, qual a temperatura em Cº que você quer que seja convertida?'.format(nome)))
f = (c*9/5)+32
print('{}, {} em graus celcius são {} graus Fahrenheit'.format(nome,c,f))