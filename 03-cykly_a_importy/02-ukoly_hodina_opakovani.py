#Úkol 1
""" Napište program, který bude vyžadovat vstup od uživatele. Pokud uživatel zadá číslo, program zjistí, zda je to liché nebo sudé. Pokud zadá slovo "konec", program se ukončí. """

cislo = input("Zadejte cislo: ")

if cislo == "konec":
    print("Program se ukončuje")
else:
    if int(cislo) % 2 == 0:
        print("Číslo je sudé")
    elif int(cislo) % 2 != 0:
        print("Číslo je liché")


#Úkol 2
""" Požádejte uživatele o zadání uživatelského jména a hesla. Pokud se zadané údaje shodují s referenčními údaji, tedy uživatelským jménem "admin" a heslem "heslo123", uživateli bude umožněn přístup, jinak program vypíše "Přístup zakázán". """

uzivatelske_jmeno = input("Zadejte uživatelské jméno: ")
heslo = input("Zadejte heslo: ")

if uzivatelske_jmeno == "admin" and heslo == "heslo123":
    print("Přístup povolen.")
else:
    print("Přístup zakázán.")



#Úkol 3
""" Napište program, který požádá uživatele o zadání celého čísla. Program poté zkontroluje, zda je toto číslo dělitelné buď 2 nebo 3, a vytiskne příslušnou zprávu. Pokud číslo není dělitelné ani 2, ani 3, program by měl vypsat, že číslo není dělitelné ani jedním z těchto čísel. """

cislo = int(input("Zadejte celé číslo: "))

if cislo % 2 == 0:
    print("Číslo je dělitelné 2.")
elif cislo % 3 == 0:
    print("Číslo je dělitelné 3.")
else:
    print("Číslo není dělitelné ani 2, ani 3.")



#Úkol 4
""" Napište program, který odstraní všechny opakující se prvky ze seznamu a vytvoří nový seznam bez duplicity."""

seznam = [1, 2, 3, 4, 3, 2, 1]
seznam_bez_duplikat = list(set(seznam))

print("Seznam bez duplicit:", seznam_bez_duplikat)



#Úkol 5
""" Požádejte uživatele o zadání jeho věku, pokud je mu více než 18 - vypiště hlášku, že na stránky může vstoupit, pokud méně, že nemůže. """

vek = int(input("Zadejte svůj věk: "))

if vek > 18:
    print("Na stránky můžete vstoupit.")
else:
    print("Na stránky nemůžete vstoupit.")



#Úkol 6 
""" Načtěte věk uživatele a poté vytvořte podmínku, která do proměnné cena uloží cenu spočítanou podle věku uživatele dle následujících pravidel
    
    0 euro pro návštěvníky mladší 6 let,
    65% ze základní ceny pro návštěvníky 6 až 26 let (žák, student),
    100% ze základní ceny pro návštěvníky 27 až 64 let (dospělý),
    50% ze základní ceny pro ostatní (senior). 
    
Plná cena je 12 euro. 
"""

vek = int(input("Zadejte svůj věk: "))
zakladni_cena = 12

if vek < 6:
    cena = 0
elif 6 <= vek <= 26:
    cena = zakladni_cena * 0.65
elif 27 <= vek <= 64:
    cena = zakladni_cena
else:
    cena = zakladni_cena * 0.5

print("Cena pro vaši kategorii je:", cena, "euro")


