class Przychodnia:

    def __init__(self, nazwa, miasto):
        self.nazwa = nazwa
        self.miasto = miasto
        self.listaPacjentow = []

class Pacjent:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.listaChorob = []

    def __str__(self):
        return f"Imię: {self.imie} Nazwisko: {self.nazwisko}"

class PrzychodniaController:

    def __init__(self):
        self.listaPrzychodni = []

    def dodajPrzychodnie(self, nazwa, miasto):
        przychodnia = Przychodnia(nazwa, miasto)
        self.listaPrzychodni.append(przychodnia)
        print(f"Przychodnia: {nazwa}, w mieście: {miasto} została dodana pomyslnie!")


    def usunPrzychodnie(self, nazwa):
        for i in self.listaPrzychodni:
            if(i.nazwa == nazwa):
                self.listaPrzychodni.remove(i)
                print(f"Przychodnia: {nazwa} została pomyslnie usunieta!")
                pass


    def dodajPacjentaDoPrzychodni(self, nazwa, imie, nazwisko):
        for i in self.listaPrzychodni:
            if(i.nazwa == nazwa):
                pacjent = Pacjent(imie, nazwisko)
                i.listaPacjentow.append(pacjent)
                print(f"Pomyślnie dodano pacjenta: {imie}, {nazwisko} do przychodni {nazwa}.")


    def usunPacjentaZPrzychodni(self, nazwa, nazwisko):
        for i in self.listaPrzychodni:
            if (i.nazwa == nazwa):
                for j in i.listaPacjentow:
                    if(j.nazwisko == nazwisko):
                        i.listaPacjentow.remove(j)
                        print(f"Pomyślnie usunieto pacjenta {nazwisko} z przychodni {nazwa}.")


    def pokazPrzychodnie(self):
        for i in self.listaPrzychodni:
            print(f"Nazwa przychodni: {i.nazwa} Miasto: {i.miasto}")


    def listaPacjentowWPrzychodni(self, nazwa):
        for i in self.listaPrzychodni:
            if (i.nazwa == nazwa):
                for j in i.listaPacjentow:
                    print(j)

    def dodajChorobePacjentowi(self, nazwa, nazwisko, choroba):
        for i in self.listaPrzychodni:
            if (i.nazwa == nazwa):
                for j in i.listaPacjentow:
                    if (j.nazwisko == nazwisko):
                        choroba = Pacjent(nazwisko, choroba)
                        j.listaChorob.append(choroba)
                        print(f"Choroba {choroba} zostala dodana dla pacjenta {i.nazwa}.")


    def listaChorobPacjenta(self, nazwa, nazwisko):
        for i in self.listaPrzychodni:
            if (i.nazwa == nazwa):
                for j in i.listaPacjentow:
                    if (j.nazwisko == nazwisko):
                        for k in j.listaChorob:
                            print(f"Choroby pacjenta {nazwisko}: {k}.")

    def sprawdzPrzychodnie(self, nazwa):
        for i in self.listaPrzychodni:
            if (i.nazwa == nazwa):
                return True

        return False

    def sprawdzPacjenta(self, nazwa, nazwisko):
        for i in self.listaPrzychodni:
            if (i.nazwa == nazwa):
                for j in i.listaPacjentow:
                    if(j.nazwisko == nazwisko):
                        i.listaPacjentow.remove(j)
                        return True

        return False


class Nfz(PrzychodniaController):

    def __init__(self):
        super().__init__()
        self.menu()

    def menu(self):

        while(True):
            print("----- WITAJ W NFZ! -----"
                  "\n ----- PROSZĘ WYBRAĆ OPCJE ----")
            menu = input("1 - PRZYCHODNIE, 2 - PACJENCI, 3 - KONIEC EDYCJI")

            if(menu == "1"):

                while(True):
                    submenu = input("1 - Dodaj przychodnie, 2 - Usuń przychodnie, 3 - Lista przychodni, \n"
                                    " 4 - Lista pacjentow w przychodni, 5 - Wstecz")

                    if(submenu == "1"):
                        nazwa = input("Podaj nazwe przychodni: ")
                        miasto = input("Podaj miasto: ")
                        self.dodajPrzychodnie(nazwa, miasto)
                        break

                    elif (submenu == "2"):
                        nazwa = input("Podaj nazwe przychodni: ")
                        if(self.sprawdzPrzychodnie(nazwa) == True):
                            self.usunPrzychodnie(nazwa)

                        else:
                            print("Blędna nazwa przychodni!")

                    # elif (submenu == "3"):
                    #     nazwa = input("Podaj nazwe:")
                    #     if (self.sprawdzPrzychodnie(nazwa) == True):
                    #         imie = input("Podaj imie pacjenta")
                    #         nazwisko = input("Podaj nazwisko pacjenta")
                    #         self.dodajPacjentaDoPrzychodni(nazwa, imie, nazwisko)
                    #     else:
                    #         print("Bledna nazwa przychodni")

                    # elif (submenu == "4"):
                    #     nazwa = input("Podaj nazwe:")
                    #     if (self.sprawdzPrzychodnie(nazwa) == True):
                    #         nazwisko = input("Podaj nazwisko pacjenta")
                    #         if(self.sprawdzPacjenta(nazwisko) == True):
                    #             self.usunPacjentaZPrzychodni(nazwa, nazwisko)
                    #         else:
                    #             print("Brak pacjenta")
                    #     else:
                    #         print("Bledna nazwa przychodni")

                    elif (submenu == "3"):
                        self.pokazPrzychodnie()

                    elif (submenu == "4"):
                        nazwa = input("Podaj nazwe przychodni: ")
                        if (self.sprawdzPrzychodnie(nazwa) == True):
                            self.listaPacjentowWPrzychodni(nazwa)
                        else:
                            print("Bledna nazwa przychodni.")

                    elif (submenu == "5"):
                        break
                    else:
                        break


            elif(menu == "2"):

                while (True):
                    submenu = input("1 - Dodaj pacjenta do przychodni, 2 - Usuń pacjenta z przychodni, \n"
                                    "3 - Dodaj chorobę pacjentowi, 4 - Lista chorób pacjenta, 5 - Wstecz")
                    if(submenu == "1"):
                        nazwa = input("Do której przychodni dodać pacjenta: ")
                        if (self.sprawdzPrzychodnie(nazwa) == True):
                            imie = input("Podaj imię pacjenta: ")
                            nazwisko = input("Podaj nazwisko pacjenta: ")
                            self.dodajPacjentaDoPrzychodni(nazwa, imie, nazwisko)

                        else:
                            print("Błędna nazwa przychodni!")


                    elif (submenu == "2"):
                        nazwa = input("Podaj nazwe przychodni z której usuwamy pacjenta: ")
                        if(self.sprawdzPrzychodnie(nazwa) == True):
                            nazwisko = input("Podaj nazwisko pacjenta: ")
                            if(self.sprawdzPacjenta(nazwa, nazwisko) == True):
                                self.usunPacjentaZPrzychodni(nazwa, nazwisko)

                            else:
                                print("Podano błędne nazwisko pacjenta!")

                        else:
                            print("Podano błędne nazwisko pacjenta!")


                    elif (submenu == "3"):
                        nazwa = input("Podaj nazwe przychodni danego pacjenta: ")
                        if (self.sprawdzPrzychodnie(nazwa) == True):
                            nazwisko = input("Podaj nazwisko pacjenta: ")
                            if(self.sprawdzPacjenta(nazwa, nazwisko) == True):
                                choroba = input("Podaj chorobe: ")
                                self.dodajChorobePacjentowi(nazwa, nazwisko, choroba)
                            else:
                                print("Brak pacjenta w przychodni!")
                        else:
                            print("Bledna nazwa przychodni!")

                    elif (submenu == "4"):
                        nazwa = input("Podaj nazwe przychodni danego pacjenta: ")
                        if (self.sprawdzPrzychodnie(nazwa) == True):
                            nazwisko = input("Podaj nazwisko pacjenta: ")
                            if (self.sprawdzPacjenta(nazwa, nazwisko) == True):
                                self.listaChorobPacjenta(nazwa, nazwisko)
                            else:
                                print(f"Brak pacjenta {nazwisko} w przychodni!")
                        else:
                            print("Bledna nazwa przychodni!")

                    elif (submenu == "5"):
                        break


            elif(menu == "3"):
                print("--- KONIEC EDYCJI ---")
                break

            else:
                print("! Nierozpoznana opcja menu !")


ob = Nfz()

# pacjent - dodaj / lista chorób EDYTOWAC