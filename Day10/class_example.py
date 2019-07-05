# class Samochod:
#     pass
#
# sam1 = Samochod()
# sam1.marka = 'VW'
# print(sam1)
# print(sam1.marka)
#
# sam2 = Samochod()
# sam2.marka = 'Seat'
# int(sam2)
# print(sam2.marka)

class Silnik:
    def __init__(self, nadana_pojemnosc):
        self.pojemnosc = nadana_pojemnosc

silnik1 = Silnik(2000)
print(silnik1)
print(silnik1.pojemnosc)


class Samochod:
    def __init__(self, nadana_marka, nadany_kolor = 'bialy'):
        self.marka = nadana_marka
        self.kolor = nadany_kolor
        self.silnik = silnik


sam1 = Samochod('VW', silnik1, 'czerwony')
# sam1.marka = 'VW'
# print(sam1)
print(sam1.marka)
print(sam1.kolor)
print(sam1.silnik.pojemnosc)

sam2 = Samochod('Seat')
# sam2.marka = 'Seat'
# int(sam2)
print(sam2.marka)
print(sam2.kolor)