import random

def jogar():
    print('\n********************************')
    print('* Bem-vindo ao Number Guessed! *')
    print('********************************\n')
    print('NÍVEIS')
    print('--------------------------------')
    print('[1] Fácil [2] Médio [3] Difícil')
    print('--------------------------------')

    numero_secreto = round(random.randrange(1 , 101))
    pontos = 1000
    rodada = 1
    nivel = 1

    while(nivel >= 1 or nivel <= 3):
        nivel = int(input('\nEm qual nível deseja jogar? \n'))
        if(nivel == 1):
            pontos = pontos - 500
            tentativas = 10
            break
        elif(nivel == 2):
            pontos = pontos - 200
            tentativas = 5
            break
        elif(nivel == 3): 
            pontos = pontos + 200
            tentativas = 3
            break



    for rodada in range(1, tentativas + 1):
        print(f'** Tentativa {rodada} de {tentativas} **')
        chute = input("\nDigite um número de 1 a 100: \n")
        numero_chute = int(chute)

        if(numero_chute < 1 or numero_chute > 100):
            print("\n--> Digite um número entre 1 e 100 <--\n")
            continue

        acertou = numero_secreto == numero_chute
        maior   = numero_secreto > numero_chute
        menor   = numero_secreto < numero_chute

        if(acertou):
            print(f"\n--> Você acertou e fez {pontos} pontos! <--\n")
            break
        else:  
            if(menor):
                print("\n--> Você errou! <--\n\nDica: O número é menor do que esse!\n")
            elif(maior):
                print("\n--> Você errou! <--\n\nDica: O número é maior do que esse!\n")
            pontos_perdidos = abs(numero_secreto - numero_chute)
            pontos = pontos - pontos_perdidos

    print("\n***** Fim do jogo *****\n\n")

if(__name__ == '__main__'):
    jogar()