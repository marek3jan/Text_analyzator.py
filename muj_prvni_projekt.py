'''
môj_prvý_projekt
autor : Marek Trojan
email : troj3marek@gmail.com
git   : marek3jan
'''
# moj prvy commit
# Vstupný text, z ktorého budem vyberať textové stringy.
TEXTS = [''' Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive topographic feature 
that rises sharply some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
         '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
         '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''',
         ''' Gradual increase of microplastics in the 
environment has currently become an emerging
environmental threat over the last 50 years, which 
for its severe impacts on the environmental system deserves 
public attention. Despite more than 1000 scientific reviews and 
publications addressing this topic, there is still so
much unknown, which requires further investigation. As 
it is already clear, microplastic particles, after they 
enter soil, can submit to complex transformation processes
and are capable to transport in many ways. These processes 
depend on the mass and shape of a particle, its chemical 
structure, native climate, and complex parameters of the soil system. 
Therefore, processes of fate, transport, and transformation of 
microplastics in soils are in many ways an extremely complex and 
uncovered fields to study.''']

# HLAVIČKA : Vstupné parametre a úvodné uvítanie
vstupy = {"Bob": "123", "Ann": "pass123", "Mike": "password123", "Liz": "pass123", 'Marek': 'engeto'}
uvitanie = "Vitajte v aplikácii Text Analyzátor - Prosím vstúpte:"
medzera = len(uvitanie) * '-'
print(medzera)
print(uvitanie.upper())
print(medzera)

# ÚVOD 1: Zadanie vstupných údajov: meno a heslo
#                          - následne vyhodnotenie, či sa meno a heslo zhoduje
#                          - zamietnutie vstupu ak sa táto podmienka nespĺňa
meno = input("meno : ")
heslo = input("heslo: ")
if vstupy.get(meno) != heslo:
    print(medzera)
    print("Vstup zamietnutý".upper())
    print(medzera)
    quit()

# ÚVOD 2: Po zadaní správnych údajov - privítanie člena a výber čísla textu na analyzovanie
#                                    - vyselektovanie chýb, pokiaľ sa zadalo namiesto čísla písmeno, alebo zlé číslo
selekcia = len(TEXTS)
print(medzera)
print(f"Vitaj v aplikácii, {meno}.")
print(f"Máme texty na analýzu v počte: {selekcia} ")
print(medzera)
moznosti = input("Vlož číslo textu: ")

if moznosti.isalpha():
    print(medzera)
    print("Nie je zadané číslo!".upper())
    print(medzera)
    quit()
elif (int(moznosti)-1) not in range(4):
    print(medzera)
    print("Nesprávne zadané číslo!".upper())
    print(medzera)
    quit()

# Jadro programu 1. časť: rozdelenie slov v texte, vyčistenie slov od zavadzajúcich znamienok
#                       - roztriedenie slovíčok do jednotlivých kategórií podľa zadaného popisu
#                       - výpočet sumy všetkých čísel v texte
else:
    text = TEXTS[int(moznosti)-1]
    neupravene_slova = text.split()
    slova = []

    for slovo in neupravene_slova:
        slovo = slovo.strip(".,?:!;|/'")
        if slovo: slova.append(slovo)

    titlecase = 0
    uppercase = 0
    lowercase = 0
    numeric = 0
    numeric_suma = 0
    pocty_pismen = {}

    for slovo in slova:
        if slovo.istitle():
            titlecase += 1
        elif slovo.isupper():
            uppercase += 1
        elif slovo.islower():
            lowercase += 1
        elif slovo.isdigit():
            numeric += 1
            numeric_suma += int(slovo)

# Jadro programu 2. časť: rozdelenie slov v texte podľa kategórie dĺžky
#                       - usporiadanie slov podľa kategórie dĺžky
        l = len(slovo)
        pocty_pismen[l] = pocty_pismen.setdefault(l, 0)+1
    usporiadane_pocty = sorted(pocty_pismen)

# Ukončenie programu 1. časť: vypísanie počtu slov v texte
#                           - vypísanie počtu slov podľa prerozdelenia do jednotlivých kategórií
#                           - vypísanie celkovej sumy číslic v texte
    print(medzera)
    print(f"Počet slov vo vybranom texte je:  {len(slova)}")
    print(f"Počet slov s veľkým písmenom na začiatku je: {titlecase}")
    print(f"Počet slov so všetkými písmenami veľkými je: {uppercase}")
    print(f"Počet slov so všetkými písmenami malými je: {lowercase}")
    print(f"Počet číslic je: {numeric}")
    print(f"Suma všetkých číslic je: {numeric_suma}")
    print(medzera)

# Ukončenie programu 2. časť:
#   -  vytvorenie  hlavičky stĺpcového grafu popisujúceho usporiadanie počtu slov podľa dĺžky
    print(f"DĹŽKA SLOV |{'VÝSKYT': ^24}| VÝSKYT ČÍSELNE")
    hlavicka = len("DLZKA SLOV")

#   - vytvorenie cyklu, ktorým sa generuje stĺpcový graf
    for i in usporiadane_pocty:
        dlzka = pocty_pismen[i]
        print(f"{' ' * (hlavicka - len(str(i))) + str(i): ^3} | {'*' * dlzka +  ' '* (22 - dlzka)} | {dlzka}")
    print(f"{' ' * hlavicka}   {'koniec grafu'.upper(): ^22}")
    print(medzera)