print('-'*20,'DECIMO-QUINTO DESAFIO','-'*20)
print('Bem vindo a localiza!')
nome = input('Por favor digite seu nome:')
dias = int(input('{}, quantos dias você utilizou o carro?:'.format(nome)))
km = int(input('{}, quantos km foram andados no carro?'.format(nome)))
total = (dias*60)+(km*0.15)
print('{}, você deve pagar R${:.2f}! Vá a sede da localiza mais próxima'.format(nome,total))