import json
import re
import requests
import orodja

def shrani_toliko_del(n=50):
    stevilo_prostih_del = n
    url = 'https://www.studentski-servis.com/index.php?t=prostaDela&hp=true&page=1&perPage={}&sort=1&workType=1&keyword='.format(stevilo_prostih_del)
    orodja.shrani_spletno_stran(url, 'prosta_dela.html')

def vsebina_datoteke(ime_datoteke):
    with open(ime_datoteke, 'r', encoding='utf-8') as r:
        return r.read()

def posamezni_oglasi(ime_datoteke):
    vsebina_strani = vsebina_datoteke(ime_datoteke)
    vzorec = r'<div class="col jobTitle clear ">(.*?)<div class="col actionBlock">'

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
    r'</p>.*<ul>.*?</strong>'
    r'(?P<stevilo_mest>.*?)'
    r'<span.*?</strong>(?P<trajanje>.*?)'
    r'<span.*?</strong>(?P<delovnik>.*?)'
    r'(<span.*?<li class.*?/strong>'
    r'(?P<narava_dela>.*?)</li>)?',
    flags=re.DOTALL
)

def podatki_iz_oglasov(ime_datoteke): #to funkcijo moramše popravit!!
    seznam_oglasov = posamezni_oglasi(ime_datoteke)
    stevec = 0
    sez = []
    for i in range(len(seznam_oglasov)):
        stevec += 1
        joj = re.findall(vzorec_oglasa, seznam_oglasov[i])
        sez += joj
    print(stevec)
    print(len(sez))

