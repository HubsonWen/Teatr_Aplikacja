class MIEJSCE_TEATRALNE:

    def __init__(self, numer_miejsca, dostepnosc_miejsca, cena_miejsca):
        self.numer_miejsca = numer_miejsca
        self.dostepnosc_miejsca = dostepnosc_miejsca
        self.cena_miejsca = cena_miejsca



class MIEJSCE_ZWYKLE(MIEJSCE_TEATRALNE):
    def __init__(self, numer_miejsca, dostepnosc_miejsca, cena_miejsca=30):
        MIEJSCE_TEATRALNE.__init__(self,numer_miejsca,dostepnosc_miejsca,cena_miejsca)


    def __str__(self):
        return f"Miejsce o numerze {self.numer_miejsca}, jest dostepne: {self.dostepnosc_miejsca}, cena za miejsce: {self.cena_miejsca} zł"



class MIEJSCE_VIP(MIEJSCE_TEATRALNE):
    def __init__(self, numer_miejsca, dostepnosc_miejsca, cena_miejsca=50, dodatkowa_oplataVIP=20):
        MIEJSCE_TEATRALNE.__init__(self, numer_miejsca, dostepnosc_miejsca, cena_miejsca)
        self.dodatkowa_oplataVIP = dodatkowa_oplataVIP

    def __str__(self):
        return f"Miejsce VIP o numerze {self.numer_miejsca}, jest dostepne: {self.dostepnosc_miejsca}, cena za miejsce: {self.cena_miejsca} {self.dodatkowa_oplataVIP}"



class MIEJSCE_DLA_NIEPELNOSPRAWNYCH(MIEJSCE_TEATRALNE):
    def __init__(self,numer_miejsca, dostepnosc_miejsca, cena_miejsca=27, ulga_SPEC=10):
        MIEJSCE_TEATRALNE.__init__(self,numer_miejsca, dostepnosc_miejsca, cena_miejsca)
        self.ulga_SPEC = ulga_SPEC

    def __str__(self):
        return f"Miejsce Specjalne o numerze {self.numer_miejsca}, jest dostepne: {self.dostepnosc_miejsca}, cena za miejsce: {self.cena_miejsca} {self.ulga_SPEC}"




class TEATR:
    def __init__(self):
        self.listaMiejsc = {1:{"Dostępność":True,"Cena":30},
                            2:{"Dostępność":True,"Cena":30},
                            3:{"Dostępność":True,"Cena":30},
                            4:{"Dostępność":True,"Cena":30},
                            5:{"Dostępność":True,"Cena":30}}

        self.listaMiejscVIP = {6:{"Dostępność":True,"Cena":50},
                               7:{"Dostępność":True,"Cena":50},
                               8:{"Dostępność":True,"Cena":50}}

        self.listaMiejscSPEC = {9:{"Dostępność":True,"Cena":27},
                                10:{"Dostępność":True,"Cena":27}}

        self.listaMiejsc2 = {}


        self.rezerwacje = {}


    # Utworzenie miejsca
    def utworzenieMiejsca(self,numer_miejsca,dostepnosc,cena):
        self.numer_miejsca = numer_miejsca
        self.dostepnosc = dostepnosc
        self.cena = cena

        self.listaMiejsc2[self.numer_miejsca] = [self.dostepnosc,self.cena]
        print(self.listaMiejsc2)


    # Dokonywanie rezerwacji

    def dokonanieRezewacji(self, imie, nazwisko, numer_miejsca):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_miejsca = int(numer_miejsca)

        try:
            if self.numer_miejsca in self.listaMiejsc:
                if self.listaMiejsc[self.numer_miejsca]["Dostępność"] == True:
                    self.rezerwacje[
                        f"Miejsce numer:, {self.numer_miejsca}, przydzielone dla"] = self.imie, self.nazwisko
                    print(
                        f"Miejsce zwykłe numer {self.numer_miejsca} zostało zarezerwowany dla {self.imie} {self.nazwisko}, Cena wyniosła {self.listaMiejsc[self.numer_miejsca]["Cena"]} zł (bez uwzględnienu dodatkowych opłat i zniżek)")

                    self.listaMiejsc[self.numer_miejsca] = {"Typ miejsca": "Zwykłe", "Dostępność": None, "Cena": 30}
                    print(self.rezerwacje)
                    # print(self.listaMiejsc)

                else:
                    print("Miejsce jest już zarezerwoane. Wybierz inne miejsce.")



            elif self.numer_miejsca in self.listaMiejscVIP:
                if self.listaMiejscVIP[self.numer_miejsca]["Dostępność"] == True:
                    self.rezerwacje[
                        f"Miejsce numer:, {self.numer_miejsca}, przydzielone dla"] = self.imie, self.nazwisko
                    print(
                        f"Miejsce VIP numer {self.numer_miejsca} zostało zarezerwowane dla {self.imie} {self.nazwisko}, Cena wyniosła {self.listaMiejscVIP[self.numer_miejsca]["Cena"]} zł (w cenie dodatkowa opłata 20 zł)")

                    self.listaMiejscVIP[self.numer_miejsca] = {"Typ miejsca": "VIP", "Dostępność": None, "Cena": 50}
                    print(self.rezerwacje)
                    # print(self.listaMiejscVIP)

                else:
                    print("Miejsce jest już zarezerwoane. Wybierz inne miejsce.")


            elif self.numer_miejsca in self.listaMiejscSPEC:
                if self.listaMiejscSPEC[self.numer_miejsca]["Dostępność"] == True:
                    self.rezerwacje[
                        f"Miejsce numer:, {self.numer_miejsca}, przydzielone dla"] = self.imie, self.nazwisko
                    print(
                        f"Miejsce Specjalne numer {self.numer_miejsca} zostało zarezerwowany dla {self.imie} {self.nazwisko}, Cena wyniosła {self.listaMiejscSPEC[self.numer_miejsca]["Cena"]} zł (w cenie dodatkowa opłata 20 zł)")

                    self.listaMiejscSPEC[self.numer_miejsca] = {"Typ miejsca": "Specjalne", "Dostępność": None,"Cena": 27}
                    print(self.rezerwacje)
                    # print(self.listaMiejscSPEC)

                else:
                    print("Miejsce jest już zarezerwoane. Wybierz inne miejsce.")


            else:
                print("Podaj numer od 1 do 10")

        except:
            pass



    def anulowanieRezerwacji(self, imie, nazwisko, miejsce_rezerw):
        self.imie = imie
        self.nazwisko = nazwisko
        self.miejsce_rezerw = miejsce_rezerw

        self.lista_rezerwacji = {1:["Jan","Kowalski"],
                                 2:["Ola","Nowak"]}  ###### Przykładowa lista rezerwacji

        print(self.lista_rezerwacji)

        if self.miejsce_rezerw in self.lista_rezerwacji.keys() and self.imie == self.lista_rezerwacji[self.miejsce_rezerw][0]:
            del self.lista_rezerwacji[self.miejsce_rezerw]
            print("Wybrany numer miejsca został usunięty z rezerwacji")

        else:
            print("Niepoprawne dane")

        print(self.lista_rezerwacji)

class KLIENT:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.konta_klientow = {}


    # Tworzenie unikalnego ID dla klienta
    def tworzenieKlienta(self):
        import random
        identyfikator = random.randint(10000, 99999)
        self.konta_klientow[identyfikator] = [self.imie + " " + self.nazwisko]
        print(f"Dla {self.imie} {self.nazwisko} został utworzony identyfikator o numerze: {identyfikator}")

        print("Konto klienta: ",self.konta_klientow)



################################################# Utworzenie miejsca

u1 = TEATR()
u1.utworzenieMiejsca(1,True,30)

print("")

################################################# Dokonywanie rezerwacji

rezerw1=TEATR()
rezerw1.dokonanieRezewacji("Jan","Kowalski",1)

print("")


################################################ Anulowanie rezerwacji

a1 = TEATR()
a1.anulowanieRezerwacji("Jan","Kowalski",1)

print("")

################################################ Utworzenie konta klienta
k1=KLIENT("Jan","Kowalski")
k1.tworzenieKlienta()
















