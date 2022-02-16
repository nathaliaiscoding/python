import adivinhacao
import forca

def escolhe():
    print('\n************************')
    print('**** Escolha o jogo ****')
    print('************************\n')

    jogo = 0

    while(jogo != 1 and jogo !=2):
        print('\n[1] Forca \n[2] Guessed Number')
        jogo = int(input())
        continue

    if(jogo == 1):
        forca.jogar()
    elif(jogo == 2):
        adivinhacao.jogar()

if(__name__ == '__main__'):
    escolhe()