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
            print(f"[Blad] Cena produktu '{self.nazwa}' nie moze byc ujemna! Ustawiono 0.0 zl.")
            self._cena = 0.0
        else:
            self._cena = float(wartosc)

    def pokaz_szczegoly(self):
        return f"Produkt: {self.nazwa} | Cena: {self.cena:.2f} zl"


class Elektronika(Produkt):
    def __init__(self, nazwa, cena, gwarancja_miesiace):
        super().__init__(nazwa, cena)
        self.gwarancja = gwarancja_miesiace

    def pokaz_szczegoly(self):
        return f"[Elektronika] {self.nazwa} | Cena: {self.cena:.2f} zl | Gwarancja: {self.gwarancja} mies."


class Odziez(Produkt):
    def __init__(self, nazwa, cena, rozmiar):
        super().__init__(nazwa, cena)
        self.rozmiar = rozmiar

    def pokaz_szczegoly(self):
        return f"[Odziez] {self.nazwa} | Cena: {self.cena:.2f} zl | Rozmiar: {self.rozmiar}"


class Sklep:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.asortyment = []

    # Dodawanie obiektu do listy
    def dodaj_produkt(self, produkt):
        self.asortyment.append(produkt)

    # Wyswietlanie wszystkich produktow
    def pokaz_asortyment(self):
        print(f"\n--- Asortyment sklepu: {self.nazwa} ---")
        for produkt in self.asortyment:
            print(produkt.pokaz_szczegoly())

    # Filtrowanie po cenie (lista skladana)
    def filtruj_tanie_produkty(self, max_cena):
        print(f"\n--- Produkty w cenie do {max_cena} zl ---")
        tanie = [p for p in self.asortyment if p.cena <= max_cena]
        for p in tanie:
            print(p.pokaz_szczegoly())

    # Filtrowanie po klasie (lista skladana)
    def filtruj_tylko_odziez(self):
        print("\n--- Tylko odziez ---")
        ubrania = [p for p in self.asortyment if isinstance(p, Odziez)]
        for u in ubrania:
            print(u.pokaz_szczegoly())


if __name__ == "__main__":
    moj_sklep = Sklep("SuperMarket24")

    # Dane startowe
    moj_sklep.dodaj_produkt(Elektronika("Telewizor Samsung", 2999.99, 24))
    moj_sklep.dodaj_produkt(Odziez("Koszula flanelowa", 120.00, "XL"))
    moj_sklep.dodaj_produkt(Elektronika("Sluchawki bezprzewodowe", 199.00, 12))
    
    # Glowne menu programu
    while True:
        print("\n=== MENU SKLEPU ===")
        print("1. Pokaz caly asortyment")
        print("2. Pokaz tylko odziez")
        print("3. Pokaz produkty do danej kwoty")
        print("4. Zakoncz program")
        
        wybor = input("Wybierz opcje (1-4): ")
        
        if wybor == '1':
            moj_sklep.pokaz_asortyment()
        elif wybor == '2':
            moj_sklep.filtruj_tylko_odziez()
        elif wybor == '3':
            kwota = float(input("Podaj maksymalna cene: "))
            moj_sklep.filtruj_tanie_produkty(kwota)
        elif wybor == '4':
            print("Koniec programu.")
            break
        else:
            print("Niepoprawny wybor, sprobuj ponownie.")   