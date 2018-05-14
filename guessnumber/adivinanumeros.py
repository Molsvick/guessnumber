import time
import sys
from random import randint
#este es un juego de adivinar numero

class Adivinar:
    def juego():
        global randint,text,letra
        secreto = randint(1,2)
        text = "En que numero estoy pensando?:"
        for letra in str(text):
            print(letra, end="")
            time.sleep(0.05)
            sys.stdout.flush()
        numero = int(input())
        intento = 1
        while numero != secreto and intento != 5:
            if numero > secreto:
                text = "Mi numero es menor, intentelo denuevo:"
                for letra in str(text):
                    print(letra, end="")
                    time.sleep(0.05)
                    sys.stdout.flush()
                numero = int(input())
                intento+=1
            if numero < secreto:
                text = "Mi numero es mayor, intentelo denuevo:"
                for letra in str(text):
                    print(letra, end="")
                    time.sleep(0.05)
                    sys.stdout.flush()
                numero = int(input())
                intento+=1
        if numero == secreto:
            if intento == 5:
                text = "Epa...casi que perdes, pero le has acertado\n"
                for letra in str(text):
                    print(letra, end="")
                    time.sleep(0.05)
                    sys.stdout.flush()
                return Pregunta.preguntaJuego()
            if intento == 1:
                text = "Crack, adivinaste en 1 solo intento, mis felicitaciones\n"
                for letra in str(text):
                    print(letra, end="")
                    time.sleep(0.05)
                    sys.stdout.flush()
                return Pregunta.preguntaJuego()
            else:
                text = "Exelente, le acertaste a mi numero\n"
                for letra in str(text):
                    print(letra, end="")
                    time.sleep(0.05)
                    sys.stdout.flush()
                return Pregunta.preguntaJuego()
        if intento == 5:
            text = "Perdiste amigo, mejor para la proxima\n"
            for letra in str(text):
                print(letra, end="")
                time.sleep(0.05)
                sys.stdout.flush()
            return Pregunta.preguntaJuego()


class Pregunta:
    def pregJugar():
        text = "Deseas jugar contra mi o quieres que adivine? (1: Adivino yo 2: Adivina Maquina):\n"
        for letra in str(text):
            print(letra, end="")
            time.sleep(0.05)
            sys.stdout.flush()
        text = "Si quieres salir aprieta cualquier tecla\n"
        for letra in str(text):
            print(letra, end="")
            time.sleep(0.05)
            sys.stdout.flush()
        resp = int(input())

        if resp == 1:
            Adivinar.juego()
        else:
            exit()

    def preguntaJuego():
        global text,letra
        text = "Deseas jugar nuevamente contra mi?(si/no):\n"
        for letra in str(text):
            print(letra, end="")
            time.sleep(0.05)
            sys.stdout.flush()
        respu = input()
        if respu == 'si':
            Adivinar.juego()
        return

text = "Bienvenido al Juego de adivinar el Numero\n"
for letra in str(text):
    print(letra, end="")
    time.sleep(0.05)
    sys.stdout.flush()

text = "Vamos a divertirnos eligiendo un numero del 1 al 100\n"
for letra in str(text):
    print(letra, end="")
    time.sleep(0.05)
    sys.stdout.flush()

Pregunta.pregJugar()




