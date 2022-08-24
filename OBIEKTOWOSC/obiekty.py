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


class Ekstra:
    pass

class Student(Pracownik,Sport,Ekstra):

    def __init__(self,imie,wiek,waga,wzrost,id_studenta,kierunek,rok_studiow,
                 firma="",stanowisko="",latapr="",wynagrodzenie="",dyscyplina="",lata_upr="", best_wynik=""):
        Pracownik.__init__(self,imie,wiek,waga,wzrost,firma,stanowisko,latapr,wynagrodzenie)
        Sport.__init__(self,dyscyplina,lata_upr, best_wynik)
        self.id_studenta = id_studenta
        self.kierunek = kierunek
        self.rok_studiow = rok_studiow

    def print_student(self):
        print(f"student: {self.id_studenta}, kierunek: {self.kierunek}, rok studiów: {self.rok_studiow}")

    def czypracownik(self):
        return self.firma != ""


print("******************************************")
st1 = Student("Olga",22,58,173,432423,"informatyka",3,"ABC","junior",1,3300)
st1.print_osoba()
st1.print_pracownik()
st1.print_student()

print(st1.wiekza10lat())

print(f"czy ososba jest pracownikiem? {st1.czypracownik()}")

print(os2.wiekza10lat())

print(f"czy ososba jest pracownikiem? {os2.czypracownik()}")


class Pracownik(Osoba):

    #konstruktor z dziedziczeniem
    def __init__(self,imie,wiek,waga,wzrost,firma,stanowisko,latapr,wynagrodzenie):
        super().__init__(imie,wiek,waga,wzrost)
        self.firma = firma
        self.stanowisko = stanowisko
        self.latapr = latapr
        self.wynagrodzenie = wynagrodzenie

    def print_pracownik(self):
        print(f"pracownik -> firma: {self.firma}, stanowisko pracy: {self.stanowisko}, lata pracy: {self.latapr},"
              f" wynagrodzenie: {self.wynagrodzenie} zł")

    def czypracownik(self):
        return True


pr = Pracownik("Olga",32,54,167,"ABC","dyrektor",5,10900)
pr.print_osoba()
pr.print_pracownik()
print(pr.wiekza10lat())


class Sport:
    
    def __init__(self,dyscyplina,lata_upr, best_wynik):
        self.dyscyplina = dyscyplina
        self.lata_upr = lata_upr
        self.best_wynik = best_wynik
        
    def info_sport(self):
        print(f"dysycyplina: {self.dyscyplina}, lata uprawiania: {self.lata_upr}, życiówka: {self.best_wynik}")
        
        
