print('-----------------------DÉCIMO-PRIMEIRO DESAFIO-----------------------')
nome = input('Olá , bem vindo ao meu sistema pra descobrir quantas tintas serão usadas para pintar uma parede , qual seu nome?:')
a = float(input('{}, qual a altura da parede que você quer pintar?(em metros):'.format(nome)))
l = float(input('E qual a largura da parede ?(em metros):'))
t = ((a*l)/2)
print('{}, você vai gastar cerca de {} latas de tinta para pintar sua parede. (consideramos que cada lata de tinta pinta 2m²)'.format(nome,t))