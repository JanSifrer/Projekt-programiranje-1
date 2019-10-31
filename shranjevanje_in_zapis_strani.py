import json
import re
import requests
import orodja

def shrani_toliko_del(stevilo_prostih_del=3017):
    url = 'https://www.studentski-servis.com/index.php?t=prostaDela&hp=true&page=1&perPage={}&sort=1&workType=1&keyword='.format(stevilo_prostih_del)
    orodja.shrani_spletno_stran(url, 'prosta_dela.html')

def vsebina_datoteke(ime_datoteke):
    with open(ime_datoteke, 'r', encoding='utf-8') as r:
        return r.read()

def posamezni_oglasi(ime_datoteke):
    vsebina_strani = vsebina_datoteke(ime_datoteke)
    vzorec = r'<div class="col jobTitle(.*?)<div class="col actionBlock">'

    #stevec = 0
    #for zadetek in re.finditer(vzorec, vsebina_strani, flags=re.DOTALL):
       # print(zadetek.groupdict())
       # stevec += 1
    #print(stevec)
    return re.findall(vzorec, vsebina_strani, flags=re.DOTALL)

vzorec_oglasa= re.compile(
    r'class="title">(?P<naslov>.*?)'
    r'(<strong>(?P<podnaslov>.*?)</strong>)?'
    r'</sp.*?<strong>(?P<placa>.*?)'
    r'</strong>.*?<strong>'
    r'(?P<lokacija>.*?)</strong>.*?'
    r'<div class="jobContent col">.*?<p>'
    r'(?P<opis>.*?)'
    r'</p>.*?<ul>.*?</strong>'
    r'(?P<stevilo_mest>.*?)'
    r'<span.*?</strong>(?P<trajanje>.*?)'
    r'<span.*?(<strong>Delovnik:</strong>(?P<delovnik>.*?)<span class)'
    r'.*?<strong>Šifra:</strong>(?P<sifra>.*?)<.*?'
    r'(<strong>Narava dela:</strong>(?P<narava_dela>.*?)</li.*?)?'
    r'</ul>',
    flags=re.DOTALL
)



ime_datoteke = 'prosta_dela.html'

def pridobi_podatke_o_oglasih(ime_datoteke):                    #Nekaj vrednosti mi ponovi!
    vsebina_strani = vsebina_datoteke(ime_datoteke)
    count = 0
    slovar=[]
    for zadetek in re.finditer(vzorec_oglasa, vsebina_strani):
        slovar_zadetkov = zadetek.groupdict()
        count += 1
        slovar.append(slovar_zadetkov)

    orodja.zapisi_csv(slovar, ['naslov', 'lokacija', 'stevilo_mest', 'delovnik', 'narava_dela', 'sifra', 'trajanje', 'naslov', 'podnaslov', 'opis', 'placa'], 'prosta_dela.csv')
    print('končano:', count)

