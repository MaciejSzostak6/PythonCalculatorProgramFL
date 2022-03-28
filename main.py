import liczby
import figury

def funMain():
    print("+----------MENU----------+")
    print("|1. Działania na liczbach|")
    print("|2. Działania na figurach|")
    print("|3. Zakończ program      |")
    print("+------------------------+")

    wybor = int(input("Podaj numer(1-2): "))

    if wybor == 1:
        print(liczby.funLiczby())
    elif wybor == 2:
        print(figury.funFigury())
    elif wybor == 3:
        return
funMain()