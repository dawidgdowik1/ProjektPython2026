class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

    @property
    def cena(self):
        return self._cena

    @cena.setter
    def cena(self, wartosc):
        if wartosc < 0:
            print(f"[Błąd] Cena produktu '{self.nazwa}' nie może być ujemna! Ustawiono 0.0 zł.")
            self._cena = 0.0
        else:
            self._cena = float(wartosc)

    def pokaz_szczegoly(self):
        return f"Produkt: {self.nazwa} | Cena: {self.cena:.2f} zł"


class Elektronika(Produkt):
    def __init__(self, nazwa, cena, gwarancja_miesiace):
        super().__init__(nazwa, cena)
        self.gwarancja = gwarancja_miesiace

    def pokaz_szczegoly(self):
        return f"[Elektronika] {self.nazwa} | Cena: {self.cena:.2f} zł | Gwarancja: {self.gwarancja} mies."


class Odziez(Produkt):
    def __init__(self, nazwa, cena, rozmiar):
        super().__init__(nazwa, cena)
        self.rozmiar = rozmiar

    def pokaz_szczegoly(self):
        return f"[Odzież] {self.nazwa} | Cena: {self.cena:.2f} zł | Rozmiar: {self.rozmiar}"


class Sklep:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.asortyment = []

    # Dodawanie obiektu do listy
    def dodaj_produkt(self, produkt):
        self.asortyment.append(produkt)

    # Wyświetlanie wszystkich produktów
    def pokaz_asortyment(self):
        print(f"\n--- Asortyment sklepu: {self.nazwa} ---")
        for produkt in self.asortyment:
            print(produkt.pokaz_szczegoly())

    # Filtrowanie po cenie (lista składana)
    def filtruj_tanie_produkty(self, max_cena):
        print(f"\n--- Produkty w cenie do {max_cena} zł ---")
        tanie = [p for p in self.asortyment if p.cena <= max_cena]
        for p in tanie:
            print(p.pokaz_szczegoly())

    # Filtrowanie po klasie (lista składana)
    def filtruj_tylko_odziez(self):
        print("\n--- Tylko odzież ---")
        ubrania = [p for p in self.asortyment if isinstance(p, Odziez)]
        for u in ubrania:
            print(u.pokaz_szczegoly())


if __name__ == "__main__":
    moj_sklep = Sklep("SuperMarket24")

    # PRODUKT DO WYWOŁANIA BŁĘDU DO SCREENA:
    moj_sklep.dodaj_produkt(Elektronika("Zepsuty telefon", -50.0, 12))

    # Reszta danych startowych
    moj_sklep.dodaj_produkt(Elektronika("Telefon Huawei", 999.99, 24))
    moj_sklep.dodaj_produkt(Odziez("Koszulka NIKE", 120.00, "M"))
    moj_sklep.dodaj_produkt(Elektronika("Słuchawki bezprzewodowe", 149.99, 12))
    
    # Główne menu programu
    while True:
        print("\n=== MENU SKLEPU ===")
        print("1. Pokaż cały asortyment")
        print("2. Pokaż tylko odzież")
        print("3. Pokaż produkty do danej kwoty")
        print("4. Zakończ program")
        
        wybor = input("Wybierz opcję (1-4): ")
        
        if wybor == '1':
            moj_sklep.pokaz_asortyment()
        elif wybor == '2':
            moj_sklep.filtruj_tylko_odziez()
        elif wybor == '3':
            kwota = float(input("Podaj maksymalną cenę: "))
            moj_sklep.filtruj_tanie_produkty(kwota)
        elif wybor == '4':
            print("Koniec programu.")
            break
        else:
            print("Niepoprawny wybór, spróbuj ponownie.")