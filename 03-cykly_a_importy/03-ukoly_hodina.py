#Úkol 1
""" Vytvořte seznam jmen. Za každé jméno chceme přidat pomocí cyklu konec e-mailové adresy (například máme v seznamu jméno "Aneta" a chceme za něj přidat "@gmail.com"). Vypište maily na obrazovku. """


seznam_jmen = ["katka", "honza", "jana"]

for jmeno in seznam_jmen:
    print(f"{jmeno}@gmail.com")


#Úkol 2
""" Vytvořte seznam školních známek. Následně pomocí cyklu spočítejte počet jedniček. """
znamky = [1, 2, 4, 5, 1]
pocet_znamek = 0

for znamka in znamky:
    if znamka == 1:
        pocet_znamek = pocet_znamek + 1
        
print(pocet_znamek)



#Úkol 3
""" Vytvořte program, který spočítá součet všech lichých čísel v zadaném seznamu čísel."""

seznam = [1, 2 ,3, 4, 5, 6]
liche = []

for cislo in seznam:
    if cislo % 2 != 0:
        liche.append(cislo)

soucet_licha = sum(liche)
print(sum(seznam))
print(soucet_licha)
    
    


#Úkol 4
""" Vytvořte program, který uživateli pomocí cyklu while umožní hádat číslo, které si počítač "myslí" (uložte na začátku libovolné číslo do proměnné). Uživatel hádá, dokud se netrefí. Pak se program ukončí. Rozšiřte program tak, aby uživatel dostával zpětnou vazbu, zda je číslo větší nebo menší"""

moje = 51

while True:
    uzivatel = int(input("Zadaj číslo od 1-100: "))
    if moje < uzivatel:
        print("moc vysoké číslo")
    elif moje > uzivatel:
        print("moc nízke číslo")
    elif moje == uzivatel:
        print("Je to tak")
        break
    



#Úkol 5
""" Máte seznam hesel viz níže. Pomocí cyklu vypište všechny hesla na obrazovku. Upravte váš program tak, aby vypisoval jen bezpečná hesla, tedy taková, jež jsou delší než 8 znaků."""

hesla = [
    "xyz101",
    "punťa!",
    "razor-blade",
    "1234",
    "12011986",
    "martin111",
    "trhnisi",
    "hokuspokus!",
    "jeník15",
    "kristus-te-spasi",
    "beruška",
    "strčprstskrzkrk",
]

novy_seznam = []

for bezpecne_hesla in hesla:
    if len(bezpecne_hesla) > 8:
        novy_seznam.append(bezpecne_hesla)

print(novy_seznam)

#Úkol 6
""" Napište cyklus, který projde zadaný seznam celých čísel a najde v něm největší hodnotu. """

seznam_cisel = [56, 23, 100, 2, 59]
nejvetsi_hodnota = seznam_cisel[0]

for cislo in seznam_cisel:
    if cislo > nejvetsi_hodnota:
        nejvetsi_hodnota = cislo
        
print(nejvetsi_hodnota)

# nebo jednodušeji
print(max(seznam_cisel))




 
 


