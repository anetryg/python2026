#Úkol 1

"""Vypočítejte měsíční příjem divadla "La la la", známého cenou jednoho lístku ve výši 12 euro, při průměrně 174 návštěvnic a návštěvníků na každé představení a při 15 představeních měsíčně."""

print(12 * 174 * 15)

#Úkol 2

"""Následně zjistěte, jak se tento měsíční příjem změní, když divadlo začne prodávat studentské vstupné za 65% ceny plného vstupného, a když víme, že polovina návštěvníků jsou studentky a studenti. Výsledek vypište na obrazovku."""

print((12 * 174 * 15) / 2 + (12 * 0.65 * 174 * 15) / 2)

#Úkol 3

"""Vypište řetězec obsahující jméno divadla tak, že sečtete dohromady jednotlivá slova toho jména."""

print("Divadlo" + "Ahoj" + "Ahoj")

#Úkol 4

"""Zkuste vynásobit řetězec celým číslem. Jaký jste dostali výsledek?"""

print("ahoj" * 5)

#Úkol 5

"""Vypište řetězec který vypadá takto: '111111000000', ale místo šesti jedniček a šesti nul obsahuje 256 jedniček a 256 nul."""

print("1" * 256 + "0" * 256 )

#Úkol 6

"""Takzvané Shannonovo číslo má hodnotu 10^123 a udává kolik nejméně lze odehrát různých šachových partií. Vytvořte řetězec, který obsahuje toto číslo zapsané běžným způsobem pomocí cifer. Například 10^3 je 1000, 10^6 je 1000000 atd."""

print(str(10 ** 123))
