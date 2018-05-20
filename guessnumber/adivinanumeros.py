import time
import sys
from random import randint
#este es un juego de adivinar numero

class Adivinar:
    def juego():
        global randint,text,letra
        secreto = randint(1,100)
        Dialogo.agilDialogo(text = "En que numero estoy pensando?:")
        numero = int(input())
        intento = 1
        while numero != secreto and intento != 5:
            if numero > secreto:
                Dialogo.agilDialogo(text = "Mi numero es menor, intentelo denuevo:")
                numero = int(input())
                intento+=1
            if numero < secreto:
                Dialogo.agilDialogo(text = "Mi numero es mayor, intentelo denuevo:")
                numero = int(input())
                intento+=1
        if numero == secreto:
            if intento == 5:
                Dialogo.agilDialogo(text = "Epa...casi que perdes, pero le has acertado\n")
                return Pregunta.preguntaJuego()
            if intento == 1:
                Dialogo.agilDialogo(text = "Crack, adivinaste en 1 solo intento, mis felicitaciones\n")
                return Pregunta.preguntaJuego()
            else:
                Dialogo.agilDialogo(text = "Exelente, le acertaste a mi numero\n")
                return Pregunta.preguntaJuego()
        if intento == 5:
            Dialogo.agilDialogo(text = "Perdiste amigo, mejor para la proxima\n")
            return Pregunta.preguntaJuego()


class SerAdivinado:
    def adivinado():
        numMin = 0
        numMax = 100
        intento2 = 1
        numMaquina = round(numMax+numMin)/2
        Dialogo.agilDialogo(text = "Piensa el numero fuertemente y no me lo digas (Coloca '+' si tu numero es mayor, '-' si es menor, '=' si es igual)\n")
        Dialogo.agilDialogo(text = "Es tu numero:")
        print(int(numMaquina))

        simbolo = input()
        while simbolo != '=' and intento2 != 7:
            if simbolo == '+':
                numMin = numMaquina
                numMaquina = numMaquina+round((numMax-numMin)/2)
                Dialogo.agilDialogo(text = "Asi que es mayor? Puede ser:")
                print(int(numMaquina))
                simbolo = input()
                intento2 = intento2+1
                if numMaquina == 99 and simbolo == '+':
                    numMaquina = 100
                    simbolo = '='

            if simbolo == '-':
                numMax = numMaquina
                numMaquina = numMaquina-round((numMax-numMin)/2)
                Dialogo.agilDialogo(text = "Conque era menor? Podra ser:")
                print(int(numMaquina))
                simbolo = input()
                intento2 = intento2+1
                if numMaquina == 2 and simbolo == '-':
                    numMaquina = 1
                    simbolo = '='

        if simbolo == '=':
            Dialogo.agilDialogo(text = "Gane, Tu numero era:")
            print(int(numMaquina))
            return Pregunta.preguntaAdiv()
        if intento2 == 7:
            Dialogo.agilDialogo(text = "Querias que perdiera, pero claramente no hay mas posibilidades\n")
            return Pregunta.preguntaAdiv()


class Pregunta:
    def pregJugar():
        Dialogo.agilDialogo(text = "Deseas jugar contra mi o quieres que adivine? (1: Adivino yo 2: Adivina Maquina):\n")
        Dialogo.agilDialogo(text = "Si quieres salir aprieta cualquier tecla\n")
        resp = int(input())

        if resp == 1:
            Adivinar.juego()
        if resp == 2:
            SerAdivinado.adivinado()
        else:
            exit()

    def preguntaJuego():
        Dialogo.agilDialogo(text = "Deseas jugar nuevamente contra mi?(si/no):\n")
        respu = input()
        if respu == 'si':
            Adivinar.juego()
        if respu == 'no':
            Pregunta.repreguntaSerAdiv()
        return

    def preguntaAdiv():
        Dialogo.agilDialogo(text = "Deseas que adivine nuevamente?(si/no):\n")
        respu = input()
        if respu == 'si':
            SerAdivinado.adivinado()
        if respu == 'no':
            Pregunta.repreguntaAdiv()
        return

    def repreguntaSerAdiv():
        Dialogo.agilDialogo(text = "Te entiendo, si ahora quieres adivinar solo dime 'si' de otro modo solo aprieta cualquier tecla para salir\n")
        respu = input()
        if respu == 'si':
            SerAdivinado.adivinado()
        else:
            Dialogo.agilDialogo(text = "Nos vimos.....\n")
            exit()

    def repreguntaAdiv():
        Dialogo.agilDialogo(text = "Oka, si quieres que adivine tu numero dime 'si' , y en caso de que quieras irte aprieta cualquier tecla\n")
        respu = input()
        if respu == 'si':
            Adivinar.juego()
        else:
            Dialogo.agilDialogo(text = "Nos vimos.....\n")
            exit()

class Dialogo:
    def agilDialogo(text):
        text = text
        for letra in str(text):
            print(letra, end="")
            time.sleep(0.03)
            sys.stdout.flush()

Dialogo.agilDialogo(text = "Bienvenido al Juego de adivinar el Numero\n")

Dialogo.agilDialogo(text = "Vamos a divertirnos eligiendo un numero del 1 al 100\n")

Pregunta.pregJugar()


