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
            print(f"[Ostrzeżenie] Cena produktu '{self.nazwa}' nie może być ujemna! Ustawiono 0.0 zł.")
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


if __name__ == "__main__":
    print("--- SKLEP INTERNETOWY - BAZA PRODUKTÓW ---")
    
    tv = Elektronika("Telewizor Samsung", 2999.99, 24)
    koszula = Odziez("Koszula flanelowa", 120.00, "XL")
    zepsuty_telefon = Elektronika("Tani Smartfon", -50.00, 12)
    
    print(tv.pokaz_szczegoly())
    print(koszula.pokaz_szczegoly())
    print(zepsuty_telefon.pokaz_szczegoly())