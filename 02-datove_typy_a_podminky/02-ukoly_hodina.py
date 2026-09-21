#**Úkol 1: Věk**

""" Umožněte uživateli zadat svůj věk. Zajistěte, aby byl věk uložen jako číslo (nikoli jako řetězec) a poté vypište věk na obrazovku. """

print(int(input("Zadejte věk")))


#**Úkol 2: Přihlašovací údaje**

""" Požádejte uživatele, aby zadal uživatelské jméno a heslo. Pokud heslo nesouhlasí s referenčním heslem "simsalabim", vypište "Přístup zakázán" a ukončete program. """

heslo = input("zadejte heslo")

if heslo != "simsalabim":
    print("Přístup zakázán")


#**Úkol 3: Kontrola věku**

""" Po dokončení hlavního programu přidejte dotaz na věk uživatele. Pokud je uživatel starší 18 let, vypište "Vstup povolen". V opačném případě vypište "Vstup povolen pouze od 18 let". """

vek_retezec = input("zadejte věk")
vek_cislo = int(vek_retezec)

if vek_cislo >= 18:
    print("Vstup povolen")
else:
    print("Vstup povolen pouze od 18 let")


#**Úkol 4: Úvod programu**

""" Vytvořte program, který na první řádek vypíše "Divadlo AhojAhoj", na druhý řádek "Vítejte v online rezervaci vstupenek" a na třetí řádek "Pro vstup do systému je potřeba registrace". Poté získejte od uživatele uživatelské jméno a věk. """

print("DivadloAhojAhoj")
print("Vítejte v online rezervaci vstupenek")
print("Pro vstup do systému je potřeba registrace")

jmeno = input("zadejte jméno")
vek = int(input("zadejte věk"))

#**Úkol 5: Cena vstupenky**

""" Pokračujte v předešlém úkolu. Vytvořte proměnnou `plna_cena` s hodnotou 12. Podle věku uživatele vypočítejte cenu vstupenky s následujícími pravidly: 0 euro pro návštěvníky mladší 6 let, 65% základní ceny pro návštěvníky 6 až 26 let, 100% základní ceny pro návštěvníky 27 až 64 let a 50% základní ceny pro ostatní. Zaokrouhlete cenu na celé centy. """

plna_cena = 12

if vek < 6:
    cena = 0
elif vek <= 26:
    cena = plna_cena * 0.65
elif vek <= 64:
    cena = plna_cena
else:
    cena = plna_cena * 0.5
    
print(round(cena, 2)) # zaokrouhlení na 2 desetinná místa

#**Úkol 6: Bezpečné heslo**

""" Požádejte uživatele, aby si zvolil uživatelské jméno a heslo. Heslo nechte zadat dvakrát a zkontrolujte, zda se obě zadaná hesla shodují a zda jsou delší než 8 znaků. """

jmeno = input("zadejte jméno")
heslo = input("zadejte heslo")
heslo2 = input("zadejte heslo podruhé")

if heslo == heslo2 and len(heslo) > 8:
    print("přístup umožněn")

#**Úkol 7: Přestupný rok**

""" Napište program, který po zadání kalendářního roku vypíše, zda je daný rok přestupný nebo ne. Rok je přestupný, pokud je dělitelný 4. Roky dělitelné 100 jsou přestupné pouze tehdy, jsou-li zároveň dělitelné 400. """

rok = int(input("Zadejte kalendářní rok:"))

if (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0):
    print(f"Rok {rok} je přestupný")
else:
    print(f"Rok {rok} není přestupný")

#**Úkol 8: Soutěž o lístky**

""" Vytvořte program pro soutěž o lístky na premiéru představení "Zločin v podmínce" v Divadle AhojAhoj. Uživatele zeptejte, zda sdílel alespoň 5 příspěvků divadla na sociálních sítích a zda letos navštívil alespoň 5 představení. Pokud je uživatel členem Klubu přátel Divadla AhojAhoj, umožněte mu účast v soutěži i bez splnění podmínek. """

sdileni_prispevku = int(input("Kolik příspěvků divadla jste sdíleli na sociálních sítích? "))
navsteva_predstaveni = int(input("Kolik představení jste letos navštívili? "))
clen_klubu_pratel = input("Jste členem Klubu přátel Divadla AhojAhoj? (ano/ne): ")

if clen_klubu_pratel == "ano":
    print("Gratulujeme! Máte možnost účastnit se soutěže o lístky.")
elif sdileni_prispevku >= 5 and navsteva_predstaveni >= 5:
    print("Gratulujeme! Máte možnost účastnit se soutěže o lístky.")
else:
    print("Omlouváme se, neplníte podmínky pro účast v soutěži o lístky.")

#**Úkol 9: E-mailová validace**

""" Napište program, který bude ověřovat platnost e-mailové adresy. Požádejte uživatele, aby zadal svou e-mailovou adresu. Zkontrolujte, zda adresa obsahuje znak "@" a alespoň jeden ".". Pokud adresa splňuje podmínky, vypište "E-mailová adresa je platná." Jinak vypište "Neplatná e-mailová adresa." """

mail = input("zadejte mailovou adresu")

if "@" in mail and "." in mail:
    print("E-mailová adresa je platná")
else:
    print("Neplatná e-mailová adresa")

#**Úkol 10: Sudé/liché**
""" Napište program, který zjistí, zda zadané číslo je sudé nebo liché, a výsledek vypište na obrazovku.  """

cislo = int(input("zadejte číslo"))

if cislo % 2 == 0:
    print("číslo je sudé")
elif cislo % 2 != 0:
    print("číslo je liché")

