import time
import sys
from random import randint
#este es un juego de adivinar numero

class Adivinar:
    def juego():
        global randint,text,letra
        secreto = randint(1,100)
        text = "En que numero estoy pensando?:"
        for letra in str(text):
            print(letra, end="")
            time.sleep(0.03)
            sys.stdout.flush()
        numero = int(input())
        intento = 1
        while numero != secreto and intento != 5:
            if numero > secreto:
                text = "Mi numero es menor, intentelo denuevo:"
                for letra in str(text):
                    print(letra, end="")
                    time.sleep(0.03)
                    sys.stdout.flush()
                numero = int(input())
                intento+=1
            if numero < secreto:
                text = "Mi numero es mayor, intentelo denuevo:"
                for letra in str(text):
                    print(letra, end="")
                    time.sleep(0.03)
                    sys.stdout.flush()
                numero = int(input())
                intento+=1
        if numero == secreto:
            if intento == 5:
                text = "Epa...casi que perdes, pero le has acertado\n"
                for letra in str(text):
                    print(letra, end="")
                    time.sleep(0.03)
                    sys.stdout.flush()
                return Pregunta.preguntaJuego()
            if intento == 1:
                text = "Crack, adivinaste en 1 solo intento, mis felicitaciones\n"
                for letra in str(text):
                    print(letra, end="")
                    time.sleep(0.03)
                    sys.stdout.flush()
                return Pregunta.preguntaJuego()
            else:
                text = "Exelente, le acertaste a mi numero\n"
                for letra in str(text):
                    print(letra, end="")
                    time.sleep(0.03)
                    sys.stdout.flush()
                return Pregunta.preguntaJuego()
        if intento == 5:
            text = "Perdiste amigo, mejor para la proxima\n"
            for letra in str(text):
                print(letra, end="")
                time.sleep(0.03)
                sys.stdout.flush()
            return Pregunta.preguntaJuego()


class SerAdivinado:
    def adivinado():
        numMin = 0
        numMax = 100
        intento2 = 1
        numMaquina = round(numMax+numMin)/2
        text = "Piensa el numero fuertemente y no me lo digas (Coloca '+' si tu numero es mayor, '-' si es menor, '=' si es igual)\n"
        for letra in str(text):
            print(letra, end="")
            time.sleep(0.03)
            sys.stdout.flush()

        text = "Es tu numero:"
        for letra in str(text):
            print(letra, end="")
            time.sleep(0.03)
            sys.stdout.flush()
        print(int(numMaquina))

        simbolo = input()
        while simbolo != '=' and intento2 != 7:
            if simbolo == '+':
                numMin = numMaquina
                numMaquina = numMaquina+round((numMax-numMin)/2)
                text = "Asi que es mayor? Puede ser:"
                for letra in str(text):
                    print(letra, end="")
                    time.sleep(0.03)
                    sys.stdout.flush()
                print(int(numMaquina))
                simbolo = input()
                intento2 = intento2+1
                if numMaquina == 99 and simbolo == '+':
                    numMaquina = 100
                    simbolo = '='

            if simbolo == '-':
                numMax = numMaquina
                numMaquina = numMaquina-round((numMax-numMin)/2)
                text = "Conque era menor? Podra ser:"
                for letra in str(text):
                    print(letra, end="")
                    time.sleep(0.03)
                    sys.stdout.flush()
                print(int(numMaquina))
                simbolo = input()
                intento2 = intento2+1
                if numMaquina == 2 and simbolo == '-':
                    numMaquina = 1
                    simbolo = '='

        if simbolo == '=':
            text = "Gane, Tu numero era:"
            for letra in str(text):
                print(letra, end="")
                time.sleep(0.03)
                sys.stdout.flush()
            print(int(numMaquina))
            return Pregunta.preguntaAdiv()
        if intento2 == 7:
            text = "Querias que perdiera, pero claramente no hay mas posibilidades\n"
            for letra in str(text):
                print(letra, end="")
                time.sleep(0.03)
                sys.stdout.flush()
            return Pregunta.preguntaAdiv()


class Pregunta:
    def pregJugar():
        text = "Deseas jugar contra mi o quieres que adivine? (1: Adivino yo 2: Adivina Maquina):\n"
        for letra in str(text):
            print(letra, end="")
            time.sleep(0.03)
            sys.stdout.flush()
        text = "Si quieres salir aprieta cualquier tecla\n"
        for letra in str(text):
            print(letra, end="")
            time.sleep(0.03)
            sys.stdout.flush()
        resp = int(input())

        if resp == 1:
            Adivinar.juego()
        if resp == 2:
            SerAdivinado.adivinado()
        else:
            exit()

    def preguntaJuego():
        text = "Deseas jugar nuevamente contra mi?(si/no):\n"
        for letra in str(text):
            print(letra, end="")
            time.sleep(0.03)
            sys.stdout.flush()
        respu = input()
        if respu == 'si':
            Adivinar.juego()
        if respu == 'no':
            Pregunta.repreguntaSerAdiv()
        return

    def preguntaAdiv():
        text = "Deseas que adivine nuevamente?(si/no):\n"
        for letra in str(text):
            print(letra, end="")
            time.sleep(0.03)
            sys.stdout.flush()
        respu = input()
        if respu == 'si':
            SerAdivinado.adivinado()
        if respu == 'no':
            Pregunta.repreguntaAdiv()
        return

    def repreguntaAdiv():
        text = "Te entiendo, si ahora quieres adivinar solo dime 'si' de otro modo solo aprieta cualquier tecla para salir\n"
        for letra in str(text):
            print(letra, end="")
            time.sleep(0.03)
            sys.stdout.flush()
        respu = input()
        if respu == 'si':
            SerAdivinado.adivinado()
        else:
            text = "Nos vimos.....\n"
            for letra in str(text):
                print(letra, end="")
                time.sleep(0.05)
                sys.stdout.flush()
            exit()

    def repreguntaSerAdiv():
        text = "Oka, si quieres que adivine tu numero dime 'si' , y en caso de que quieras irte aprieta cualquier tecla\n"
        for letra in str(text):
            print(letra, end="")
            time.sleep(0.03)
            sys.stdout.flush()
        respu = input()
        if respu == 'si':
            Adivinar.juego()
        else:
            text = "Nos vimos.....\n"
            for letra in str(text):
                print(letra, end="")
                time.sleep(0.05)
                sys.stdout.flush()
            exit()

text = "Bienvenido al Juego de adivinar el Numero\n"
for letra in str(text):
    print(letra, end="")
    time.sleep(0.03)
    sys.stdout.flush()

text = "Vamos a divertirnos eligiendo un numero del 1 al 100\n"
for letra in str(text):
    print(letra, end="")
    time.sleep(0.03)
    sys.stdout.flush()

Pregunta.pregJugar()




