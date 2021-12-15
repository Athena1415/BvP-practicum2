def consoleMain():
    startOp()

    print("1: Info \n"
          "2: Voeg klant toe\n"
          "3: Voeg bestelling toe\n"
          "4: Nieuw produt / wijziging\n"
          "5: Sluit af"
          )
    inputt = int(input(">>> "))

    if inputt == 1:
        consoleInfo()
    elif inputt == 2:
        consoleKlant(hoogsteKlantnummer, magazijn)
    elif inputt == 3:
        consoleBestelling()
    elif inputt == 4:
        consoleProduct(magazijn)
    elif inputt == 5:
        sluitAf()
    else:
        print("Number not valid")

def consoleInfo():
    print("1: Info product\n"
          "2: Winst product\n"
          "3: Info magazijn\n"
          "4: Verkoopwaarde magazijn\n"
          "5: Winst magazijn\n"
          "6: Meest winstgevend product\n"
          "7: Beste klant\n"
          )
    inputt = int(input(">>> "))


    if inputt == 2:
        print() #info prod
        '''
        totaalWinst
        totaal
        winst voor prod
        
        '''

    if inputt == 3:


def consoleKlant(hoogsteKlantnummer, magazijn):
    naam = input("Naam klant: ")
    hoogsteKlantnummer += 1
    klantNummer = hoogsteKlantnummer
    eval("%s = Klant(%s, %s, %s)" %(naam.lower(), naam, klantNummer, magazijn))

def consoleBestelling(magazijn):
    product = input("Product: ")
    aantal = int(input("Aantal: "))
    klant = eval(input("Klant: ").lower())
    Bestelling(eval(product.lower()), aantal, eval(klant.lower()), magazijn)

def consoleProduct(magazijn):
    print("1: Nieuw product\n"
          "2: Stock aanvullen\n"
          )
    inputt = int(input(">>> "))

    if inputt == 1:
        product = input("Naam product: ")
        aankoopprijs = float(input("Aankoopprijs: "))
        verkoopprijs = float(input("Verkoopprijs: "))
        eval("%s = ProductType(%s, %s, %s, %s)" % (product.lower(), product, aankoopprijs, verkoopprijs, magazijn))

    elif inputt == 2:
        product = input("Naam product: ")
        aantal = input("Toegevoegd aan stock: ")
        eval(product.lower()).addStock(aantal)

    else:
        print("Number not valid")

def sluitAf():
    pass

def startOp()