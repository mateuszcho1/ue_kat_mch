# Zad. 1
class Kurs:
    def __init__(self, Kierowca, Pojazd, FirmaTransportowa, Odcinek, FirmaSpozywcza):
        self.Kierowca = Kierowca
        self.Pojazd = Pojazd
        self.FirmaTransportowa = FirmaTransportowa
        self.Odcinek = Odcinek
        self.FirmaSpozywcza = FirmaSpozywcza 

    def __str__(self):
        return 'Kurs = ( Kierowca : ' + self.Kierowca + ' , Pojazd = ' + self.Pojazd + ' , Firma Transportowa = ' + self.FirmaTransportowa + ' , Odcinek : ' + self.Odcinek + ' , Firma Spożywcza : ' + self.FirmaSpozywcza + ' )'

class Kierowca:
    def __init__(self, Imie, Nazwisko, Rok_urodzenia, Miejscowosc, Kod_pocztowy):
        self.Imie = Imie
        self.Nazwisko = Nazwisko
        self.Rok_urodzenia = str(Rok_urodzenia)
        self.Miejscowosc = Miejscowosc
        self.Kod_pocztowy = Kod_pocztowy

    def __str__(self):
        return 'Kierowca = ( Imię :' + self.Imie + ' , Nazwisko : ' + self.Nazwisko + ' , Rok urodzenia : ' + self.Rok_urodzenia + ' , Miejscowość : ' + self.Miejscowosc + ' , Kod pocztowy : ' + self.Kod_pocztowy + ' )'

kier_1 = Kierowca("Mateusz" , "Chojnacki", 1997, "Waśniów", "27-425")

class Pojazd:
    def __init__(self, Marka, Rok, Typ, Moc):
        self.Marka = Marka
        self.Rok = str(Rok)
        self.Typ = Typ
        self.Moc = str(Moc)

    def __str__(self):
        return 'Pojazd = ( Marka : ' + self.Marka + ' , Rok produkcji : ' + self.Rok + ' , Typ = ' + self.Typ + ' , Moc[KM] : ' + self.Moc + ' )'

p_1 = Pojazd("MAN", 2017, "Ciąfnik siodłowy", 410)

class FirmaTransportowa:
    def __init__(self, NazwaFirmy, RokZalozenia, Miejscowosc, Kod_pocztowy,  Liczba_pracownikow):
        self.NazwaFirmy = NazwaFirmy
        self.RokZalozenia = str(RokZalozenia)
        self.Miejscowosc = Miejscowosc
        self.kod_pocztowy = Kod_pocztowy
        self.Liczba_pracownikow = str(Liczba_pracownikow)

    def __str__(self):
        return ' Firma = ( Nazwa Firmy : ' + self.NazwaFirmy + ' , Rok założenia : ' + self.RokZalozenia + ' , Miejscowosc : ' + self.Miejscowosc + ' , Kod pocztowy : ' + self.kod_pocztowy +  ' , Liczba pracowników : ' + self.Liczba_pracownikow + ' )'

ft_1 = FirmaTransportowa("Trans-Spo", 1995, "Kielce", "25-001", 23)

class Odcinek:
    def __init__(self, Mj_poczatkowa, Mj_koncowa, LiczbaKm):
        self.Mj_poczatkowa = Mj_poczatkowa
        self.Mj_koncowa = Mj_koncowa
        self.LiczbaKm = str(LiczbaKm)
    
    def __str__(self):
        return ' Odcinek = ( Miejscowość początkowa : ' + self.Mj_poczatkowa + ' , Miejscowość końcowa : ' + self.Mj_koncowa + ' Dystans : ' + self.LiczbaKm + ' )'

odc_1 = Odcinek("Kielce", "Słomniki", 92)
odc_2 = Odcinek("Słomniki", "Kraków", 25)

class FirmaSpozywcza:
    def __init__(self, Nazwa, Rok_zalozenia, Miejscowosc, ilosc_oddzialow, kod_pocztowy):
        self.Nazwa = Nazwa
        self.Rok_zalozenia = str(Rok_zalozenia)
        self.Miejscowosc = Miejscowosc
        self.ilosc_oddzialow = str(ilosc_oddzialow)
        self.kod_pocztowy = kod_pocztowy
    
    def __str__(self):
        return ' Firma spożywcza = ( Nazwa Firmy : ' + self.Nazwa + ' , Rok założenia : ' + self.Rok_zalozenia + ', Miejscowość : ' + self.Miejscowosc + ' , Kod pocztowy : ' + self.kod_pocztowy + ' , Ilość oddziałów : ' + self.ilosc_oddzialow + ' )'

fs_1 = FirmaSpozywcza("Fruit Good", 2001, "Słomniki", 1, "32-090")

km_1 = str(print(int(odc_1.LiczbaKm) + int(odc_2.LiczbaKm)))
kurs_1 = Kurs(kier_1.Imie + ' ' + kier_1.Nazwisko, p_1.Marka, ft_1.NazwaFirmy, odc_1.LiczbaKm + odc_2.LiczbaKm, fs_1.Nazwa)
print(kurs_1)
