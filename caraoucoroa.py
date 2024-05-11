# CARA OU COROA - MINI GAME

import random

print('Bem-vindo ao mini game de Cara ou Coroa!')

resposta = input('Você deseja ser Cara ou Coroa? ').lower()

random = random.randint(0,1)


if random == 0 and resposta == 'cara':
    print('Cara ganhou! Você venceu!')
elif random == 1 and resposta == 'coroa':
    print('Coroa ganhou! Você venceu!')
elif random == 0 and resposta == 'coroa':
    print('Cara ganhou! Você perdeu!')
elif random == 1 and resposta == 'cara':
    print('Coroa ganhou! Você perdeu!')
else:
    print('Resposta inválida!')
