from this import d
import time

def funPrintMenu():
    print("+----------MENU----------+")
    print("|1. Pole kwadratu        |")
    print("|2. Pole prostokąta      |")
    print("|3. Pole trójkąta        |")
    print("|4. Pole koła            |")
    print("|5. Pole równoległoboku  |")
    print("|6. Pole trapezu         |")
    print("|7. Pole rombu           |")
    print("|8. Obwód kwadratu       |")
    print("|9. Obwód prostokąta     |")
    print("|10. Obwód trójkąta      |")
    print("|11. Obwód koła          |")
    print("|12. Obwód równoległoboku|")
    print("|13. Obwód trapezu       |")
    print("|14. Obwód rombu         |")
    print("+------------------------+")

def funFigury():
    funPrintMenu()
    wybor = int(input("Podaj numer operacji(1-12): "))

    if wybor!=1 and wybor!=2 and wybor!=3 and wybor!=4 and wybor!=5 and wybor!=6 and wybor!=7 and wybor!=8 and wybor!=9 and wybor!=10 and wybor!=11 and wybor!=12 and wybor!=13 and wybor!=14:
        print("Nie ma takiej operacji.")
        time.sleep(1)
        funReturnToMenu()

    else:
        a = int(input("Podaj a: "))
        b = int(input("Podaj b: "))
        pi = 3.14

        if wybor == 1:
            poleKwa = a * a
            print(f"Pole kwadratu wynosi: {round(poleKwa, 2)}")

        elif wybor == 2:
            polePro = a * b
            print(f"Pole prostokąta wynosi: {round(polePro, 2)}")

        elif wybor == 3:
            h = int(input("Podaj wysokość: "))
            poleTro = a * h / 2
            print(f"Pole trójkąta wynosi: {round(poleTro, 2)}")

        elif wybor == 4:
            r = int(input("Podaj promień koła"))
            poleKol = pi * r * r
            print(f"Pole koła wynosi: {poleKol}")

        elif wybor == 5:
            poleRow = a * b
            print(f"Pole równoległoboku wynosi: {poleRow}")

        elif wybor == 6:
            h = int(input("Podaj wysokość: "))
            poleTra = ((a + b) * h) / 2
            print(f"Pole trapezu wynosi: {poleTra}")

        elif wybor == 7:
            poleRom = (a * b) / 2
            print(f"Pole równoległoboku wynosi: {poleRom}")

        elif wybor == 8:
            obwKwa= 4 * a
            print(f"Obwód kwadratu wynosi: {obwKwa}")

        elif wybor == 9:
            obwPro = (2 * a) + (2 * b)
            print(f"Obwód prostokąta wynosi: {obwPro}")

        elif wybor == 10:
            c = int(input("Podaj c: "))
            obwTro = a + b + c
            print(f"Obwód trójkąta wynosi: {obwTro}")

        elif wybor == 11:
            r = int(input("Podaj promień: "))
            obwKol = 2 * pi * r
            print(f"Obwód koła wynosi: {obwKol}")

        elif wybor == 12:
            obwRow = (2 * a) + (2 * b)
            print(f"Obwód równoległoboku wynosi: {obwRow}")

        elif wybor == 13:
            d = int(input("Podaj d: "))
            obwTra = a + b + c + d
            print(f"Obwód trapezu wynosi: {obwTra}")

        elif wybor == 14:
            obwRom = 4 * a
            print(f"Obwód rombu wynosi: {obwRom}")
    return "Koniec programu"
def funReturnToMain():
    print()

def funReturnToMenu():
    funFigury()