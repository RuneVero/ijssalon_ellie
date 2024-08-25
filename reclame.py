def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak} van {prijs:.2f} euro voor {nieuwe_prijs:.2f} euro."

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    totale_btw = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal:.2f} euro, waarover {btw:.2f} euro btw betaald dient te worden."

def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return hoogste, laagste

def gemiddelde(mijn_lijst):
    gemiddelde = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."

def meervoudig(invoer_lijst):
    hoogste, laagste, _ = laag_en_hoog(invoer_lijst)
    return [hoogste, laagste]

def mijn_functie_2(korte_lijst):
    """Voer een bewerking uit op de korte lijst. Hier: bereken de som van de elementen."""
    return sum(korte_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig(invoer_lijst_2)
    
    resultaat = mijn_functie_2(korte_lijst)
    
    return resultaat
    