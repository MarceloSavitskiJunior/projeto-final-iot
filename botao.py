#Acadêmicos 
# Eduardo Ranzan Ferreira
# João Vitor Martelli
# Marcelo Júnior
import RPi.GPIO as gpio
import time as delay
import random as random

gpio.setmode(gpio.BOARD)

ledVermelho, ledVerde, botao = 11,12,18

gpio.setup(ledVermelho, gpio.OUT)
gpio.setup(ledVerde, gpio.OUT)
gpio.setup(botao, gpio.IN)

gpio.output(ledVermelho, False)
gpio.output(ledVerde, False)
contador = 0
i = 0

while True:
    if gpio.input(botao) == True:
        contador = contador + 1
        delay.sleep(0.5)
        print("+1 click")

        i = 0

    while i < contador:

        if contador == 1:

            controle = random.randint(1,2)

            print("sessao 1")

            if controle == 1:
                print("Sucesso")
                gpio.output(ledVermelho, True)
                delay.sleep(0.5)
                gpio.output(ledVermelho, False)
                delay.sleep(0.2)
                gpio.output(ledVermelho, True)
                delay.sleep(0.5)
                gpio.output(ledVermelho, False)
                delay.sleep(0.2)

                
                gpio.output(ledVerde, True)
                delay.sleep(0.5)
                gpio.output(ledVerde, False)
                delay.sleep(0.2)
                gpio.output(ledVerde, True)
                delay.sleep(0.5)
                gpio.output(ledVerde, False)
                delay.sleep(0.2)
                gpio.output(ledVerde, True)
                delay.sleep(0.5)
                gpio.output(ledVerde, False)
                delay.sleep(0.2)
            else :
                print("Falha")
                gpio.output(ledVermelho, True)
                delay.sleep(0.5)
                gpio.output(ledVermelho, False)
                delay.sleep(0.2)
                gpio.output(ledVermelho, True)
                delay.sleep(0.5)
                gpio.output(ledVermelho, False)
                delay.sleep(0.2)
                gpio.output(ledVermelho, True)
                delay.sleep(0.5)
                gpio.output(ledVermelho, False)
                delay.sleep(0.2)

            i = i + 1
            print("Fim sessão 1")

        if contador == 2:

            controle = random.randint(1,2)

            print("sessao 2")
            
            if controle == 1:
                
                print("Sucesso")
                gpio.output(ledVerde, True)
                delay.sleep(2)
                gpio.output(ledVerde, False)
                delay.sleep(0.5)
            
            else :

                print("Falha")
                gpio.output(ledVermelho, True)
                delay.sleep(2)
                gpio.output(ledVermelho, False)
                delay.sleep(0.5)

            i = i + 2
            print("Fim sessão 2")

        if contador == 3:
            
            print("sessao 3")

            controle = random.randint(1,2)

            if controle == 1:
                
                print("Sucesso")
                gpio.output(ledVerde, True)
                delay.sleep(0.5)
                gpio.output(ledVerde, False)
                delay.sleep(0.5)
                gpio.output(ledVerde, True)
                delay.sleep(0.5)
                gpio.output(ledVerde, False)
                delay.sleep(0.5)
                gpio.output(ledVerde, True)
                delay.sleep(0.5)
                gpio.output(ledVerde, False)
                delay.sleep(0.5)
                gpio.output(ledVerde, True)
                delay.sleep(0.5)
                gpio.output(ledVerde, False)
                delay.sleep(0.5)
                gpio.output(ledVerde, True)
                delay.sleep(0.5)
                gpio.output(ledVerde, False)
                delay.sleep(0.5)

            else :

                print("Falha")
                gpio.output(ledVermelho, True)
                delay.sleep(0.5)
                gpio.output(ledVermelho, False)
                delay.sleep(0.5)
                gpio.output(ledVermelho, True)
                delay.sleep(0.5)
                gpio.output(ledVermelho, False)
                delay.sleep(0.5)
                gpio.output(ledVermelho, True)
                delay.sleep(0.5)
                gpio.output(ledVermelho, False)
                delay.sleep(0.5)
                gpio.output(ledVermelho, True)
                delay.sleep(0.5)
                gpio.output(ledVermelho, False)
                delay.sleep(0.5)
                gpio.output(ledVermelho, True)
                delay.sleep(0.5)
                gpio.output(ledVermelho, False)
                delay.sleep(0.5)


            i = i + 3
            print("Fim sessão 3")
            
        if contador == 4:
            
            print("Sessão 4")

            controle = random.randint(1,2)

            if controle == 1:
                print("Sucesso")
                gpio.output(ledVerde, True)
                delay.sleep(3)
                gpio.output(ledVerde, False)
                delay.sleep(0.2)
            else :
                print("Falha")
                gpio.output(ledVermelho, True)
                delay.sleep(3)
                gpio.output(ledVermelho, False)
                delay.sleep(0.2)

            i = i + 4
            print("Fim sessão 4")
        

        if contador == 5:
            
            print("Sessão 5")
            controle = random.randint(1,2)

            def testeconexao():
                try:
                    urlopen('https://colegiomaterdei.com.br', timeout=1)
                    return True
                except:
                    return False


            if testeconexao() == False:
                print("Conexão Iniciada")
                gpio.output(ledVerde, True)
                delay.sleep(3)
                gpio.output(ledVerde, False)
                delay.sleep(0.2)
            else :
                print("Falha na conexão")
                gpio.output(ledVermelho, True)
                delay.sleep(3)
                gpio.output(ledVermelho, False)
                delay.sleep(0.2)
            
            i = i + 5
            print("Fim sessão 5")

        if contador == 6:
            
            print("Sessão 6")

            gpio.output(ledVerde, True)
            delay.sleep(0.5)
            gpio.output(ledVerde, False)
            delay.sleep(0.2)
            gpio.output(ledVerde, True)
            delay.sleep(0.5)
            gpio.output(ledVerde, False)
            delay.sleep(0.2)
            gpio.output(ledVerde, True)
            delay.sleep(0.5)
            gpio.output(ledVerde, False)
            delay.sleep(0.2)
            gpio.output(ledVermelho, True)
            delay.sleep(0.5)
            gpio.output(ledVermelho, False)
            delay.sleep(0.2)
            gpio.output(ledVermelho, True)
            delay.sleep(0.5)
            gpio.output(ledVermelho, False)
            delay.sleep(0.2)
            gpio.output(ledVermelho, True)
            delay.sleep(0.5)
            gpio.output(ledVermelho, False)
            delay.sleep(0.2)

            i = i + 6
            contador = 0
            print("Fim sessão 6")

