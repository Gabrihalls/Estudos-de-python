import random
print('-'*20,'DECIMO-NONO DESAFIO','-'*20)
nome1 = str(input('Digite o primeiro nome para o sorteio:'))
nome2 = str(input('Digite o segundo nome para o sorteio:'))
nome3 = str(input('Digite o terceiro nome para o sorteio:'))
nome4 = str(input('Digite o último nome para o sorteio:'))
lista = [nome1,nome2,nome3,nome4]
sorteado = random.choice(lista)
print('O nome foi sorteado foi o de : {}'.format(sorteado))