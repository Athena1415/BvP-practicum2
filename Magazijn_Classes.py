class Magazijn:
    def __init__(self):
        self._lijstVanProducten = []
        self._lijstMetBestellingen = []
    def getProducten(self):
        return self._lijstVanProducten
    def addProduct(self, product):
        self._lijstVanProducten.append(product)

    def getVerkoopwaardeStock(self):
        return round(sum([product.getVerkoopwaarde() for product in self._lijstVanProducten]),2)
    def getWinst(self):
        return round(sum([product.bepaalWinst() for product in self._lijstVanProducten]),2)
    def getInfo(self):
        for product in self._lijstVanProducten:
            print(product.getInformatie())

    def meestWintstgevendProduct(self):
        maximum = 0
        for product in self._lijstVanProducten:
            if product.bepaalWinst() > maximum:
                maximum = product.bepaalWinst()
                maxproduct = product
        return maxproduct, maximum

    def addBestelling(self, bestelling):
        self._lijstMetBestellingen.append(bestelling)

    def besteKlant(self):
        klantendict = {}
        for bestelling in self._lijstMetBestellingen:
            try: klantendict[bestelling.getKlant()] += bestelling.getAantal()
            except: klantendict[bestelling.getKlant()] = bestelling.getAantal()
        maximum = 0
        for key in klantendict.keys():
            if klantendict[key] > maximum:
                maximum = klantendict[key]
                besteKlant = key

        print("De best klant is %s met een winst van €%s." %(besteKlant.getNaam(), maximum))




class Producttype:

    def __init__(self, naam, aankoopprijs, verkoopprijs, naamVanMagazijn):
        self._naam = naam
        self._aankoopprijs = aankoopprijs
        self._verkoopprijs = verkoopprijs
        self._aantal = 0
        self._verkocht = 0
        naamVanMagazijn.addProduct(self)

    def addToStock(self, aantal):
        self._aantal += int(aantal)
    def removeFromStock(self, aantal):
        if aantal < self._aantal:
            self._aantal -= int(aantal)
            self._verkocht += aantal
        else:
            print("Te weinig stock")

    def getVerkoopwaarde(self):
        return self._verkoopprijs * self._aantal

    def bepaalWinst(self):
        return (self._verkoopprijs - self._aankoopprijs)*self._verkocht
    def getAantal(self):
        return self._aantal

    def getInformatie(self):
        return "aantal: %s, aankoopprijs: €%s, verkoopprijs: €%s, aantal: %s" %(self._naam, self._aankoopprijs, self._verkoopprijs, self._aantal)

    def getVerkocht(self):
        return self._verkocht
class Klant:

    def __init__(self, naam, klantennummer):
        self._naam  = naam
        self._klantennummer = klantennummer
    def getNaam(self):
        return self._naam

    def __repr__(self):
        s = "De beste klant is %s" %self.getNaam()
        return s

class Bestelling:

    def __init__(self, aantal, type, klant, magazijn):
        self._aantal = aantal
        self._type = type
        self._klant = klant
        type.removeFromStock(self._aantal)
        magazijn.addBestelling(self)
    def getKlant(self):
        return self._klant
    def getAantal(self):
        return self._aantal












def simulatie():
    magazijn = Magazijn()
    appel = Producttype("appel", 1, 1.5, magazijn)
    peer = Producttype("peer", 1.5, 2.5, magazijn)
    banaan = Producttype("banana", 0.5, 0.7, magazijn)
    appel.addToStock(50)
    peer.addToStock(100)
    banaan.addToStock(10)
    print("verkoopwaarde appels = €%s" %appel.getVerkoopwaarde())
    print("verkoopwaarde van het magazijn = €%s" %magazijn.getVerkoopwaardeStock())

    Ernie = Klant("Ernie", "01234")
    Bert = Klant("Bert", "98765")
    bestellingErnie = Bestelling(10, appel, Ernie, magazijn)
    bestellingBert = Bestelling(5, peer, Bert, magazijn)
    print("winst op appels = €%s" %appel.bepaalWinst())
    print("totale winst = €%s" %magazijn.getWinst())
    bestelling2Ernie = Bestelling(20, peer, Ernie, magazijn)
    Holmes = Klant("Ernlock Holmes", "235711")
    bestellingHolmes = Bestelling(5, banaan, Holmes, magazijn)
    magazijn.getInfo()
    magazijn.besteKlant()





def main():
    # makeBackup()
    print("Wat wilt u doen?\n"
          "1: iets aanmaken\n"
          "2: bestelling opgeven\n"
          "3: info printen\n"
          "4: winst tonen")
    inputt = input(">>> ")

main()