class Magazijn:
    def __init__(self):
        self._lijstVanProducten = []
        self._lijstMetBestellingen = []
        self._lijstMetKlanten = []

    def getKlanten(self):
        return self._lijstMetKlanten
    def getBestellingen(self):
        return self._lijstMetBestellingen
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
        print("Het meest winstgevend product is %s met een winst van %s" %(maxproduct.getNaam(), round(maximum, 2)))

    def addBestelling(self, bestelling):
        self._lijstMetBestellingen.append(bestelling)

    def addKlant(self, klant):
        self._lijstMetKlanten.append(klant)

    def besteKlant(self):
        klantendict = {}
        for bestelling in self._lijstMetBestellingen:
            try: klantendict[bestelling.getKlant()] += bestelling.getWinst()
            except: klantendict[bestelling.getKlant()] = bestelling.getWinst()
        maximum = 0
        for key in klantendict.keys():
            if klantendict[key] > maximum:
                maximum = klantendict[key]
                besteKlant = key

        print("De best klant is %s met een winst van €%s." %(besteKlant.getNaam(), round(maximum, 2)))




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

    def getAankoopprijs(self):
        return self._aankoopprijs
    def getVerkoopprijs(self):
        return self._verkoopprijs

    def bepaalWinst(self):
        return (self._verkoopprijs - self._aankoopprijs) * self._verkocht
    def bepaalWinstPerItem(self):
        return self._verkoopprijs - self._aankoopprijs
    def getAantal(self):
        return self._aantal

    def getInformatie(self):
        return "Naam: %s, aankoopprijs: €%s, verkoopprijs: €%s, aantal: %s" %(self._naam, self._aankoopprijs, self._verkoopprijs, self._aantal)

    def getVerkocht(self):
        return self._verkocht

    def getNaam(self):
        return self._naam

class Klant:
    def __init__(self, naam, klantennummer, magazijn):
        self._naam  = naam
        self._klantennummer = klantennummer
        magazijn.addKlant(self)

    def getNaam(self):
        return self._naam

    def getKlantnummer(self):
        return self._klantennummer

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
    def getProduct(self):
        return self._type
    def getWinst(self):
        return self._aantal * self._type.bepaalWinstPerItem()












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

    Ernie = Klant("Ernie", "01234", magazijn)
    Bert = Klant("Bert", "98765", magazijn)
    bestellingErnie = Bestelling(10, appel, Ernie, magazijn)
    bestellingBert = Bestelling(5, peer, Bert, magazijn)
    print("winst op appels = €%s" %appel.bepaalWinst())
    print("totale winst = €%s" %magazijn.getWinst())
    bestelling2Ernie = Bestelling(20, peer, Ernie, magazijn)
    Holmes = Klant("Ernlock Holmes", "235711", magazijn)
    bestellingHolmes = Bestelling(5, banaan, Holmes, magazijn)
    magazijn.getInfo()
    magazijn.besteKlant()




'''
ALLEMAAL IN EEN FUNCTIE ZETTEN ANDERS PROBLEEM MET VARIABELEN


'''



def consoleMain():
    magazijn = Magazijn()
    fileProduct = open('magazijnProducten.txt')
    for line in fileProduct.readlines():
        lijstProduct = line.split('\t')
        exec('%s = Producttype("%s", float(%s), float(%s), %s)' % (
        lijstProduct[0].lower(), lijstProduct[0], lijstProduct[1], lijstProduct[2], 'magazijn'))
        eval(lijstProduct[0].lower()).addToStock(float(lijstProduct[3]))
    fileProduct.close()

    fileKlant = open('magazijnKlanten.txt')
    for line in fileKlant.readlines():
        lijstKlant = line.split('\t')
        if len(lijstKlant) == 1:
            hoogsteKlantnummer = int(lijstKlant[0])
            continue
        exec('%s = Klant("%s", int(%s), %s)' % (lijstKlant[0].lower(), lijstKlant[0], lijstKlant[1], 'magazijn'))
    fileKlant.close()

    fileBestelling = open('magazijnBestellingen.txt')
    for line in fileBestelling.readlines():
        lijstBestelling = line.split('\t')
        Bestelling(int(lijstBestelling[0]), eval(lijstBestelling[1].lower()), eval(lijstBestelling[2].lower()), magazijn)
    fileBestelling.close()

    while True:
        print("Wat wilt u doen?\n"
              "1: Info \n"
              "2: Voeg klant toe\n"
              "3: Voeg bestelling toe\n"
              "4: Nieuw produt / wijziging\n"
              "5: Sluit af"
              )
        inputt = int(input(">>> "))

        if inputt == 1:
            print("1: Info product\n"
                  "2: Winst product\n"
                  "3: Info magazijn\n"
                  "4: Verkoopwaarde magazijn\n"
                  "5: Winst magazijn\n"
                  "6: Meest winstgevend product\n"
                  "7: Beste klant\n"
                  )
            inputt = int(input(">>> "))

            if inputt == 1:
                product = input("Product: ")
                print(eval(product.lower()).getInformatie())
            if inputt == 2:
                product = input("Product: ")
                print(product, "heeft €%s winst gemaakt." % round(eval(product.lower()).bepaalWinst(), 2))
            if inputt == 3:
                magazijn.getInfo()
            if inputt == 4:
                print("De verkoopwaarde van het magazijn is €%s." % magazijn.getVerkoopwaardeStock())
            if inputt == 5:
                print("Het magzijn heeft €%s winst gemaakt." % magazijn.getWinst())
            if inputt == 6:
                magazijn.meestWintstgevendProduct()
            if inputt == 7:
                magazijn.besteKlant()

        elif inputt == 2:
            naam = input("Naam klant: ")
            hoogsteKlantnummer += 1
            klantNummer = hoogsteKlantnummer
            exec("%s = Klant('%s', '%s', %s)" % (naam.lower(), naam, klantNummer, 'magazijn'))

        elif inputt == 3:
            klant = eval(input("Klant: ").lower())
            product = input("Product: ")
            aantal = int(input("Aantal: "))
            Bestelling(aantal, eval(product.lower()), klant, magazijn)

        elif inputt == 4:
            print("1: Nieuw product\n"
                  "2: Stock aanvullen"
                  )
            inputt = int(input(">>> "))

            if inputt == 1:
                product = input("Naam product: ")
                aankoopprijs = float(input("Aankoopprijs: "))
                verkoopprijs = float(input("Verkoopprijs: "))
                exec("%s = Producttype('%s', %s, %s, %s)" % (product.lower(), product, aankoopprijs, verkoopprijs, "magazijn"))

            elif inputt == 2:
                product = input("Naam product: ")
                aantal = int(input("Toegevoegd aan stock: "))
                eval(product.lower()).addToStock(aantal)

            else:
                print("Number not valid")

        elif inputt == 5:
            fileProduct = open('magazijnProducten.txt', 'w')
            for product in magazijn.getProducten():
                lijstProduct = [product.getNaam(), str(product.getAankoopprijs()), str(product.getVerkoopprijs()),
                                str(product.getAantal())]
                fileProduct.write('\t'.join(lijstProduct) + '\n')
            fileProduct.close()

            fileKlant = open('magazijnKlanten.txt', 'w')
            fileKlant.write(str(hoogsteKlantnummer) + '\n')
            for klant in magazijn.getKlanten():
                lijstKlant = [klant.getNaam(), str(klant.getKlantnummer())]
                fileKlant.write('\t'.join(lijstKlant) + '\n')
            fileKlant.close()

            fileBestelling = open('magazijnBestellingen.txt', 'w')
            for bestelling in magazijn.getBestellingen():
                lijstBestelling = [str(bestelling.getAantal()), bestelling.getProduct().getNaam(),
                                   bestelling.getKlant().getNaam()]
                fileBestelling.write('\t'.join(lijstBestelling) + '\n')
            fileBestelling.close()
            return None

        else:
            print("Number not valid")

        print("")



# def startOp():
#     magazijn = Magazijn()
#     fileProduct = open('magazijnProducten.txt')
#     for line in fileProduct.readlines():
#         lijstProduct = line.split('\t')
#         exec('%s = Producttype("%s", float(%s), float(%s), %s)' % (lijstProduct[0].lower(), lijstProduct[0], lijstProduct[1], lijstProduct[2], 'magazijn'))
#         eval(lijstProduct[0].lower()).addToStock(float(lijstProduct[3]))
#     fileProduct.close()
#
#     fileKlant = open('magazijnKlanten.txt')
#     for line in fileKlant.readlines():
#         lijstKlant = line.split('\t')
#         if len(lijstKlant) == 1:
#             hoogsteKlantnummer = int(lijstKlant[0])
#             continue
#         exec('%s = Klant("%s", int(%s), %s)' % (lijstKlant[0].lower(), lijstKlant[0], lijstKlant[1], 'magazijn'))
#     fileKlant.close()
#
#     fileBestelling = open('magazijnBestellingen.txt')
#     for line in fileBestelling.readlines():
#         lijstBestelling = line.split('\t')
#         Bestelling(int(lijstBestelling[0]), eval(lijstBestelling[1]), eval(lijstBestelling[2]), magazijn)
#     fileBestelling.close()
#
#     return magazijn, hoogsteKlantnummer



consoleMain()