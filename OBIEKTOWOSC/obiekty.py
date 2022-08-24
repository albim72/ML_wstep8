class Osoba:

    #opis stanu -> konstuktor klasy -> funkcja konstrukcyjna
    def __init__(self,imie,wiek,waga,wzrost):
        self.imie = imie
        self.wiek  = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.info()

    #opis zachowania -> metody -> funkcje klasy

    def info(self):
        print("tworzenie nowej osoby...")

    def print_osoba(self):
        print(f"osoba -> imię: {self.imie}, wiek: {self.wiek}, waga: {self.waga} kg, "
              f"wzrost: {self.wzrost} cm")

    def wiekza10lat(self):
        return self.wiek+10

    def czypracownik(self):
        return False

os1 = Osoba("Jan",34,69,171)
os1.print_osoba()

print(os1.wiekza10lat())

print(f"czy ososba jest pracownikiem? {os1.czypracownik()}")


print("******************************************")
os2 = Osoba("Olga",42,77,174)
os2.print_osoba()

print(os2.wiekza10lat())

print(f"czy ososba jest pracownikiem? {os2.czypracownik()}")
