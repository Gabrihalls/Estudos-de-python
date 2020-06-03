import math
print('-'*20,'DECIMO-OITAVO DESAFIO','-'*20)
nome = input('Qual o seu nome?:')
angulo1 = int(input('{}, escolha um ângulo:'.format(nome)))
angulo2 = math.radians(angulo1)
sen = (math.sin(angulo2))
cos = (math.cos(angulo2))
tg = (math.tan(angulo2))
print('{} o seno do seu ângulo é : {:.2f}\nO cosseno do seu angulo é : {:.2f}\nA tangente do seu ângulo é : {:.2f}'.format(nome,sen,cos,tg))