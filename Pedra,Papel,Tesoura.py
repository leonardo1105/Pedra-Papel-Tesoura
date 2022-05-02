print('='*20)
print('\033[92mJokenpo\033[m')
print('='*20)
import random
from time import sleep
lista=['Tesoura','Papel','Pedra']
n=random.choice(lista)
print('Vamos jogar Jokenpô')
print('\033[95mAperte 1 para jogar Tesoura\nAperte 2 para jogar Papel\nAperte 3 para jogar Pedra\033[m')
m=int(input('Coloque aqui: '))
if m == 1:
    r='Tesoura'
elif m == 2:
    r='Papel'
elif m == 3:
    r='Pedra'
print('Certo,Vamos lá')
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po')
sleep(1)
if 'Tesoura' in r and 'Pedra' in n or 'Papel' in r and 'Tesoura' in n or 'Pedra' in r and 'Papel' in n:
    print('\033[91mVocê perdeu!Eu coloquei {} e você {}\033[m'.format(n, r))
elif 'Tesoura' in r and 'Papel' in n or 'Papel' in r and 'Pedra' in n or 'Pedra' in r and 'Tesoura' in n:
    print('\033[92mVocê ganhou.Eu coloquei {} e você {}.\033[m'.format(n, r))
else:
    print('\033[97mDeu empate, nós dois colocamos {}\033[m'.format(n))
n=str(input('Você quer continuar?[Sim/Não]: ')).lower()[0]
while 's' in n:
    lista = ['Tesoura', 'Papel', 'Pedra']
    n = random.choice(lista)
    print('\033[95mAperte 1 para jogar Tesoura\nAperte 2 para jogar Papel\nAperte 3 para jogar Pedra\033[m')
    m = int(input('Coloque aqui: '))
    if m == 1:
        r = 'Tesoura'
    elif m == 2:
        r = 'Papel'
    elif m == 3:
        r='Pedra'
    print('Certo,Vamos lá')
    print('Jo')
    sleep(1)
    print('Ken')
    sleep(1)
    print('Po')
    sleep(1)
    if 'Tesoura' in r and 'Pedra' in n or 'Papel' in r and 'Tesoura' in n or 'Pedra' in r and 'Papel' in n:
        print('\033[91mVocê perdeu!Eu coloquei {} e você {}\033[m'.format(n, r))
    elif 'Tesoura' in r and 'Papel' in n or 'Papel' in r and 'Pedra' in n or 'Pedra' in r and 'Tesoura' in n:
        print('\033[92mVocê ganhou.Eu coloquei {} e você {}.\033[m'.format(n, r))
    else:
        print('\033[97mDeu empate, nós dois colocamos {}\033[m'.format(n))
    n = str(input('Você quer continuar?[Sim/Não]: ')).lower()[0]
print('Obrigado por jogar comigo!')
