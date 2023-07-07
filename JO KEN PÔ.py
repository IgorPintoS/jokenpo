import random
import time
print('\033[1;36;40m=\033[m' * 45)
print('\033[1;36;40m                  JO KEN PÔ                  \033[m')
print('\033[1;36;40m=\033[m' * 45)

listChoicesC = ['Pedra', 'Papel', 'Tesoura']
choiceComputer = random.choice(listChoicesC).upper()

print('\033[1;36;40m     O REI DO JOKENPÔ LHE DESAFIA!!          \033[m')
print('\033[1;36;40m     SELECIONE UMA DAS ARMAS:                \033[m\n\033[1;36;40m     OPÇÃO 1: PEDRA.                         \033[m\n\033[1;36;40m     OPÇÂO 2: PAPEL.                         \033[m\n\033[1;36;40m     OPÇÃO 3: TESOURA.                       \033[m\n\033[1;36;40m     OPÇÂO 4: DESISTO, O REI É MUITO BOM.    \033[m')

choicePlayer = int(input('\033[1;36;40m     ARMA ESCOLHIDA:                        \033[m'))
if choicePlayer == 1 and choiceComputer == 'PEDRA':
    time.sleep(1)
    print('\033[1;36;40m     MUITO BEM, JO KEN PÔ!                   \033[m')
    time.sleep(1)
    print('\033[1;36;40m     PEDRA VS PEDRA.                         \033[m')
    print('\033[1;36;40m     EMPATE, FOI POR POUCO, HE HE HE.        \033[m')
elif choicePlayer == 2 and choiceComputer == 'PAPEL':
    time.sleep(1)
    print('\033[1;36;40m     MUITO BEM, JO KEN PÔ!                   \033[m')
    time.sleep(1)
    print('\033[1;36;40m     PAPEL VS PAPEL.                         \033[m')
    print('\033[1;36;40m     EMPATE, FOI POR POUCO, HE HE HE.        \033[m')
elif choicePlayer == 3 and choiceComputer == 'TESOURA':
    time.sleep(1)
    print('\033[1;36;40m     MUITO BEM, JO KEN PÔ!                   \033[m')
    time.sleep(1)
    print('\033[1;36;40m     TESOURA VS TESOURA.                     \033[m')
    print('\033[1;36;40m     EMPATE, FOI POR POUCO, HE HE HE.        \033[m')
elif choicePlayer == 1 and choiceComputer == 'PAPEL':
    time.sleep(1)
    print('\033[1;36;40m     BEM, JO KEN PÔ!                         \033[m')
    time.sleep(1)
    print('\033[1;36;40m     PEDRA VS PAPEL.                         \033[m')
    print('\033[1;36;40m     GANHEI DE VOCÊ, ISSO FOI FÁCIL HA HA HA.\033[m')
elif choicePlayer == 1 and choiceComputer == 'TESOURA':
    time.sleep(1)
    print('\033[1;36;40m     MUITO BEM, JO KEN PÔ!                   \033[m')
    time.sleep(1)
    print('\033[1;36;40m     PEDRA VS TESOURA.                       \033[m')
    print('\033[1;36;40m     NÃÃÃO FUI DERROTADO, AHHH.              \033[m')
    print('\033[1;36;40m     PARABÉNS, VOCÊ DERROTOU O REI.          \033[m')
elif choicePlayer == 2 and choiceComputer == 'PEDRA':
    time.sleep(1)
    print('\033[1;36;40m     MUITO BEM, JO KEN PÔ!                   \033[m')
    time.sleep(1)
    print('\033[1;36;40m     PAPEL VS PEDRA.                         \033[m')
    print('\033[1;36;40m     NÃÃÃO FUI DERROTADO, AHHH.              \033[m')
    print('\033[1;36;40m     PARABÉNS, VOCÊ DERROTOU O REI.          \033[m')
elif choicePlayer == 2 and choiceComputer == 'TESOURA':
    time.sleep(1)
    print('\033[1;36;40m     MUITO BEM, JO KEN PÔ!                   \033[m')
    time.sleep(1)
    print('\033[1;36;40m     PAPEL VS TESOURA.                       \033[m')
    print('\033[1;36;40m     GANHEI DE VOCÊ, ISSO FOI FÁCIL HA HA HA.\033[m')
elif choicePlayer == 3 and choiceComputer == 'PEDRA':
    time.sleep(1)
    print('\033[1;36;40m     MUITO BEM, JO KEN PÔ!                   \033[m')
    time.sleep(1)
    print('\033[1;36;40m     TESOURA VS PEDRA.                       \033[m')
    print('\033[1;36;40m     GANHEI DE VOCÊ, ISSO FOI FÁCIL HA HA HA.\033[m')
elif choicePlayer == 3 and choiceComputer == 'PAPEL':
    time.sleep(1)
    print('\033[1;36;40m     MUITO BEM, JO KEN PÔ!                   \033[m')
    time.sleep(1)
    print('\033[1;36;40m     TESOURA VS PAPEL.                       \033[m')
    print('\033[1;36;40m     NÃÃÃO FUI DERROTADO, AHHH.              \033[m')
    print('\033[1;36;40m     PARABÉNS, VOCÊ DERROTOU O RE            \033[m')
elif choicePlayer == 4:
    time.sleep(1)
    print('\033[1;36;40m     HA HA HA, FRACOTE.                      \033[m\n\033[1;36;40m     GAME OVER.                              \033[m')








