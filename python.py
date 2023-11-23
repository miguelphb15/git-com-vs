print('olá amigo')
n = int(input('Você tem quantos anos?\n'))
if n >= 18 :
    print('já que você tem {} então você pode servir'.format(n))
else:
    print('não está apto ainda.')
#fazendo uma atualização para comitar em outra branch(repositório)
n2 = input('E qual o seu nome?')
if n >= 18 :
    print('pois {},nos veremos amanhã para você servir.'.format(n2))
else:
    print('Até mais então {}'.format(n2))