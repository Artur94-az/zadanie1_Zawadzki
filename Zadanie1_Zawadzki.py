# Stworzenie menu

def srednia_arytmetyczna():  # Średnia arytmetyczna
    print("Wybrałeś opcję 1: Średnia arytmetyczna")
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))
    srednia = (liczba1 + liczba2) / 2
    print(f"Średnia arytmetyczna wynosi: {srednia}")

def Liczba_do_potegi():  # Liczba do potęgi
    print("Wybrałeś opcję 2: Liczba do potęgi")
    Liczba = float(input("Podaj Liczbę: "))
    potega = int(input("Podaj wykładnik potęgi: "))
    wynik = Liczba ** potega
    print(f"{Liczba} do potęgi {potega} wynosi: {wynik}")

def Porownanie_dwoch_liczb():  # Porównanie dwóch liczb
    print("Wybrałeś opcję 3: Porównanie dwóch Liczb")
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))
    if liczba1 > liczba2:
        print(f"{liczba1} jest większa od {liczba2}")
    elif liczba1 < liczba2:
        print(f"{liczba1} jest mniejsza od {liczba2}")
    else:
        print(f"{liczba1} jest równa {liczba2}")

def zbadaj_trojkat():  # Zbadanie trójkąta
    while True:  # Pętla, aby po złych danych wrócić do menu
        try:
            a = float(input("Podaj pierwszy bok trójkąta: "))
            b = float(input("Podaj drugi bok trójkąta: "))
            c = float(input("Podaj trzeci bok trójkąta: "))

            # Sprawdzenie, czy można utworzyć trójkąt
            if a + b > c and a + c > b and b + c > a:
                print("Można utworzyć trójkąt.")
                break  # Jeśli trójkąt jest możliwy, wychodzimy z pętli
            else:
                print("Nie można stworzyć trójkąta. Spróbuj ponownie.")

        except ValueError:  # Obsługuje błąd w przypadku, gdy użytkownik poda coś, co nie jest liczbą
            print("Błąd! Proszę podać prawidłowe liczby.")

def menu():  # Przypisanie do menu
    while True:  # Pętla umożliwiająca powroty do menu po wykonaniu opcji
        print("\n1. Średnia arytmetyczna")
        print("2. Liczba do potęgi")
        print("3. Porównanie dwóch liczb")
        print("4. Zbadaj trójkąt")
        print("0. Zakończ")

        # Użytkownik wybiera opcję
        wybor = input("Wybierz opcję: ")

        if wybor == '1':
            srednia_arytmetyczna()
        elif wybor == '2':
            Liczba_do_potegi()
        elif wybor == '3':
            Porownanie_dwoch_liczb()
        elif wybor == '4':
            zbadaj_trojkat()
        elif wybor == '0':
            print("Kończę program.")
            break  # Zakończenie programu
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")  # Jeśli użytkownik poda błędną opcję

# Uruchomienie programu
menu()
