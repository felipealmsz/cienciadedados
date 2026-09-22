import sys 
import os
import time

def tela_entrada():
    while True:
        os.system('cls')
        print('Bem vindo ao módulo CAPM \n')
        print('Você pode calcular as seguintes grandezas: alfa de Jensen e beta \n')
        grandeza = input("Digite 'a' para alfa; 'b' para beta e 'x' para encerrar")

        if grandeza =='a':
            print('Você quer calcular o alfa')
            break
        elif grandeza == 'b':
            print('Você quer calcular o beta')
            break
        elif grandeza.upper() == 'x':
            print('Você pediu para encerrar. Obrigado por usar nossa aplicação')
            break
        else:
            print('Você não digitou uma alternativa válida. Tente novamente')
            time.sleep(6)
    sys.exit()


    pass