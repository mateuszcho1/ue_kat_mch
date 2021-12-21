class Developer:
    def __init__(self, Nazwa, Siedziba, Rok_zalozenia, Strona):
        self.Nazwa = Nazwa
        self.Siedziba = Siedziba
        self.Rok_zalozenia = Rok_zalozenia
        self.Strona = Strona

    def __str__(self):
        return 'Developer = ( Nazwa firmy : ' + self.Nazwa + ', Siedziba : ' + self.Siedziba + \
            ', Rok założenia : ' + self.Rok_zalozenia + ', Strona internetowa : ' + self.Strona + ').'


Developer_1 = Developer(
    "Cristal Park",
    'ul. Białej Koniczyny Warszawa',
    1990,
    'biuro@cristalpar.eu')
Developer_2 = Developer(
    'Villastok',
    'ul. Żeromskiego 96, Łódź',
    1995,
    'biuro@villastok.pl')