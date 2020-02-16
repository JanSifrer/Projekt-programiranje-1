import math


def boljsa_lokacija(x):
    razbitje = x.split()
    if len(razbitje) > 1:
        if "BLED" in razbitje:
            return "BLED"
        if "BLED," in razbitje:
            return "BLED"
        if "BOHINJ," in razbitje:
            return "BOHINJ"
        if "BOHINJSKA" in razbitje:
            return "BOHINJSKA-BISTRICA"
        if "BOROVNICA" in razbitje:
            return "BOROVNICA"
        if "BOROVNICA," in razbitje:
            return "BOROVNICA"
        if "CELJE" in razbitje:
            return "CELJE"
        if "CELJE," in razbitje:
            return "CELJE"
        if "DOMŽALE" in razbitje:
            return "DOMŽALE"
        if "DOMŽALE," in razbitje:
            return "DOMŽALE"
        if "GROSUPLJE" in razbitje:
            return "GROSUPLJE"
        if "KRANJ" in razbitje:
            return "KRANJ"
        if "KRŠKO" in razbitje:
            return "KRŠKO"
        if "KAMNIK" in razbitje:
            return "KAMNIK"
        if "KOPER" in razbitje:
            return "KOPER"
        if "KONJICE" in razbitje:
            return "SLOVENKSE-KONJICE"
        if "KRANJSKA" in razbitje:
            return "KRANJSKA-GORA"
        if "LJUBLJANA" in razbitje:
            return "LJUBLJANA"
        if "LJ" in razbitje:
            return "LJUBLJANA"
        if "LJUBLJANA," in razbitje:
            return "LJUBLJANA"
        if "LJUBLJANI" in razbitje:
            return "LJUBLJANA"
        if "LJUBLJANE" in razbitje:
            return "LJUBLJANA"
        if "LITIJA" in razbitje:
            return "LITIJA"
        if "LITIJI" in razbitje:
            return "LITIJA"
        if "MOZIRJE" in razbitje:
            return "MOZIRJE"
        if "MARIBOR" in razbitje:
            return "MARIBOR"
        if "MARIBORU" in razbitje:
            return "MARIBOR"
        if "MURSKA" in razbitje:
            if "SOBOTA" in razbitje:
                return "MURSKA-SOBOTA"
        if "MIKLAVŽ" in razbitje:
            return "MARIBOR"
        if "NOVO" in razbitje:
            return "NOVO-MESTO"
        if "NOVA" in razbitje:
            if "GORICA" in razbitje:
                return "NOVA-GORICA"
        if "PTUJ" in razbitje:
            return "PTUJ"
        if "POSTOJNA," in razbitje:
            return "POSTOJNA"
        if "PIRAN" in razbitje:
            return "PIRAN"
        if "PORTOROŽ" in razbitje:
            return "PORTOROŽ"
        if "RADOVLJICA" in razbitje:
            return "RADOVLJICA"
        if "RADGONA" in razbitje:
            return "GORNJA-RADGONA"
        if "ROGAŠKA" in razbitje:
            if "SLATINA" in razbitje:
                return "ROGAŠKA-SLATINA"
        if "SAP" in razbitje:
            return "ŠMARJE-SAP"
        if "SLOVENJ" in razbitje:
            return "SLOVENJ-GRADEC"
        if "STARI" in razbitje:
            return "STARI-VRH"
        if "ŠTEPANJSKO" in razbitje:
            return "LJUBLJANA"
        if "ŠKOFJA" in razbitje:
            return "ŠKOFJA-LOKA"
        if "ŽIRI" in razbitje:
            return "ŽIRI"
                
    return x


def koliko_besed_je_v_imenu(x):
    return len(x.split())

def ali_je_neto(c):
    if type(c) == type('21'):
        return 'neto' in c

def zaokrozena_neto_placa(x):
    razbitje = x.split()
    stevilo = razbitje[0].split(',')
    if stevilo[0][0] in '9876543210':
        if len(stevilo[1])==1:
            return math.ceil((int(stevilo[0]) + (0.1)*int(stevilo[1]))*4)/4
        if len(stevilo[1])==2:
            return math.ceil((int(stevilo[0]) + (0.01)*int(stevilo[1]))*4)/4
    return x


