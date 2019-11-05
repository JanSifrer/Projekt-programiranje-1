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
    return re.findall(vzorec, vsebina_strani, flags=re.DOTALL)

vzorec_oglasa= re.compile(
    r'class="title">(?P<naslov>.*?)'
    r'(<strong>(?P<podnaslov>.*?)</strong>)?</sp'
    r'.*?<strong>(?P<neto_placa>.*?)</str(.*?\((?P<bruto_placa>.*?)\))?'
    r'.*?<strong>'
    r'(?P<lokacija>.*?)</strong>'
    r'.*?<div class="jobContent col">'
    r'.*?<p>(?P<opis>.*?)(\n.*?)?</p>'
    r'.*?<ul>.*?</strong>'
    r'(?P<stevilo_mest>.*?)'
    r'<span.*?</strong>(?P<trajanje>.*?)'
    r'<span.*?(<strong>Delovnik:</strong>(?P<delovnik>.*?)<span class)'
    r'.*?<strong>Šifra:</strong>(?P<sifra>.*?)<.*?'
    r'(<strong>Narava dela:</strong>(?P<narava_dela>.*?)</li.*?)?'
    r'</ul>',
    flags=re.DOTALL
)



ime_datoteke = 'prosta_dela.html'

def pridobi_podatke_o_oglasih(ime_datoteke):
    seznam_oglasov = posamezni_oglasi(ime_datoteke)  #seznam po oglasih
    slovar_iskanih_podatkov = []
    stevec = 0
    for i in seznam_oglasov:
        for zadetek in re.finditer(vzorec_oglasa, i):
            slovar_zadetkov = zadetek.groupdict()
            slovar_iskanih_podatkov.append(slovar_zadetkov)
            stevec += 1
    print(stevec)

    #orodja.zapisi_csv(slovar_iskanih_podatkov, ['naslov', 'podnaslov', 'neto_placa', 'bruto_placa', 'lokacija', 'opis', 'stevilo_mest', 'trajanje', 'delovnik', 'sifra', 'narava_dela'], 'prosta_dela1.csv')
    #print('končano:', len(slovar_iskanih_podatkov))

    orodja.zapisi_json(slovar_iskanih_podatkov, 'prosta_dela2.json')
