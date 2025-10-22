"""
==========================================
 Task Manager - Jednoduchý správce úkolů
==========================================

Popis:
    Konzolová aplikace pro správu úkolů.
    Umožňuje uživateli:
        • přidat nový úkol (název + popis),
        • zobrazit seznam všech úkolů,
        • odstranit vybraný úkol,
        • ukončit program.

Struktura dat:
    - Seznam 'ukoly' obsahuje jednotlivé úkoly jako slovníky.
      Každý úkol má klíče: {"nazev": <str>, "popis": <str>}

Funkce:
    - hlavni_menu()     : zobrazí hlavní menu, řídící smyčka programu s cyklem while true (nevrací hodnotu), volá ostatní funkce podle uživatelské volby
    - pridat_ukol()     : přidá nový úkol, vrací True/False podle úspěchu
    - zobrazit_ukoly()  : vypíše seznam úkolů (nevrací hodnotu)
    - odstranit_ukol()  : odstraní úkol podle pořadového čísla, vrací True/False podle úspěchu

Autor:        Jana Staňková
Verze:        1.3
Datum:        2025-10-22
Licence:      MIT License
Python:       3.10+

Poznámky:
    - Aplikace je určena pro konzolové použití.
    - Ošetřuje běžné chyby uživatelského vstupu bez použití výjimek.
    - Program neukládá data trvale (seznam úkolů je pouze v paměti). 
    - Vytvořeno v rámci Projektu 1 po ukončení kurzu Engeto Testing Akademie.
    - Program s ukládáním dat s MySQL databází spolu s rozšířením funkcí je součástí Projektu 2.

------------------------------------------
"""


ukoly = []      # vytvoření seznamu úkolů, což je seznam slovníků

# Funkce hlavni_menu() zobrazuje hlavní menu s volbami pro uživatelský vstup (1-4) namapovanými s jednotlivými funkcemi 
# funkce hlavni_menu() se spouští stále dokola po dokončení běhu jakékoliv funkce, dokud není přerušena volbou 4 s break
def hlavni_menu():
    while True:   # iterace, po dokončení běhu každé funkce se zobrazuje hlavní menu, dokud ho nepřeruší volba 4 s break
        print("\nSprávce úkolů - Hlavní menu")    # \n odsazení o řádek kvůli přehlednosti
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        
        vstup_volba = input("Vyberte možnost (1-4): ").strip()        # string, bez převodu na int, odstranění mezer před a po stringu

        # kontrola dat z uživatelského vstupu ještě před voláním funkce
        # 1) kontrola správnosti datového typu (celé číslo/integer) - místo vyvolávání výjimky ValueError
        if not vstup_volba.isdecimal():                                         # Pokud uživatel nezadal celé číslo (integer),
            print("Chybně zadaný datový typ. Zadejte číslo v rozsahu 1-4.") # vytiskni mu hlášku
            continue  # a vráť ho do hl. menu (ukončení dané iterace a návrat na začátek nekonečného while true cyklu / hl. menu).

        volba = int(vstup_volba) # převod už prověřené uživatelské hodnoty (čísla) na datový typ integer

        # 2) kontrola správnosti rozsahu zadaného čísla (1-4) - místo vyvolávání výjimky IndexError
        if volba < 1 or volba > 4:                                      # Pokud uživatel nezadal číslo v rozsahu 1-4,
            print("Volba akce se zadaným číslem neexistuje. Zadejte číslo v rozsahu 1-4.")
            continue  # tak ho program vrátí do hl. menu.
        
        # namapování uživatelské volby s příslušnými funkcemi, pouze volba 4 není spojena s funkcí, ale s příkazem break
        # funkce se volá s už jen ověřenými platnými vstupy (integer v rozsahu 1-4)
        if volba == 1:
            pridat_ukol()
        elif volba == 2:
            zobrazit_ukoly()
        elif volba == 3:
            odstranit_ukol()
        elif volba == 4:
            print("Konec programu.")
            break                   # ukončení věčného cyklu while true / zobrazování hl. menu, konec programu



# Funkce pridat_ukol() vytvoří nový úkol (slovník) do seznamu úloh
# 1 úkol = 1 slovník (klíč, hodnota), tzn. seznam úkolů je seznam slovníků, kde každý úkol je samostatný slovník
# klíč a hodnota slovníku jsou povinné, tzn. název a popis úkolu jsou oba povinné údaje
# metoda strip() pro odstranění bílých znaků z obou stran textu zadaného uživatelem
def pridat_ukol():
    nazev = input("Zadejte název úkolu: ").strip()  
    popis = input("Zadejte popis úkolu: ").strip()

    if not nazev or not popis:      # pokud uživatel nezadá název nebo popis (obě hodnoty jsou povinné)
        print("Nebyl zadán název nebo popis úkolu. Prosím, zadejte obě tyto hodnoty (název, popis úkolu).") # vytiskni hlášku
        return False             # a vrať stav False; konec funkce, návrat do hlavního menu

    # vytvoření slovníku/úkolu se svým klíčem/názvem úkolu a hodnotou/popisem úkolu (1 úkol = 1 slovník)
    # přiřazení slovníku/úkolu do seznamu úkolů
    ukol = {"nazev": nazev, "popis": popis}      # vytvoření slovníku s úkolem (klíč/nazev, hodnota/popis)
    ukoly.append(ukol)                           # přidání úkolu/slovníku do seznamu úkolů
    print(f"Úkol '{nazev}' byl přidán.")         # hláška pro uživatele
    return True                                  # vrácení stavu True; konec funkce, návrat do hlavního menu


# Funkce zobrazit_ukol() zobrazí seznam úkolů, což je seznam slovníků s jejich klíči a hodnotami; 
# očíslování slovníků/úkolů ze seznamu úkolů přes for cyklus s funkcí enumerate() a argumentem start=1 pro počáteční číslo
def zobrazit_ukoly():
    print("\nSeznam úkolů")  # \n odsazení o řádek kvůli přehlednosti, oddělení od řádku s uživatelským vstupem
    if not ukoly:            # pro případ prázdného seznamu úkolů
        print("Seznam úkolů je prázdný.")  # tisk oznámení
    else:
        for i, ukol in enumerate(ukoly, start=1):  # iterace, očíslování všech slovníků/úkolů, nutné pro fci odstranit_ukol()
            print(f"{i}. {ukol['nazev']} - {ukol['popis']}") # tisk pořadového čísla, klíče a hodnoty daného slovníku


# Funkce odstranit_ukol() odstraní úkol dle pořadového čísla zobrazeného funkcí zobrazit_ukoly() 
# nejdříve je tedy nutné zobrazit aktuální seznam všech úkolů přes funkci zobrazit_ukoly()
# ošetřuje běžné chyby uživatelského vstupu a vrací jako stav False (ne výjimky): a) prázdný seznam úkolů, b) špatný datový typ (ne celé číslo), c) číslo mimo rozsah existujících úkolů
# kontroluje hraniční hodnoty: 0, záporná čísla, větší než délka seznamu.
# funkce odstranit_ukoly() vrací stav výsledku akce (True/False) s příslušnými hláškami
def odstranit_ukol():
    # případ prázdného seznamu úkolů
    if not ukoly:               # Pokud je seznam úkolů prázdný,
        print("Seznam úkolů je prázdný. Žádné úkoly k odstranění.") # vytiskni hlášku
        return False   # a vráť stav False a uživatele do hl. menu (ukončení funkce a návrat na začátek nekonečného while true cyklu / hl. menu).
    
    zobrazit_ukoly()

    vstup_cislo_ukolu = input("Zadejte číslo úkolu, který chcete odstranit: ").strip()  # string, bez převodu na int, odstranění mezer před a po stringu

    # kontrola dat z uživatelského vstupu ještě před voláním funkce, ukončení funkce s příslušnou hláškou a návrat do hl. menu u špatných vstupních hodnot
    # 1) kontrola správnosti datového typu (celé číslo/integer) - místo vyvolávání výjimky ValueError
    # kontrola, zda vstup obsahuje pouze číslice 0–9
    if not vstup_cislo_ukolu.isdecimal():                   # Pokud uživatel nezadal celé číslo (integer),
        print("Chybně zadaný datový typ. Zadejte pořadové číslo úkolu ze seznamu (celé kladné číslo).") # vytiskni mu hlášku
        return False  # a vráť stav False a uživatele do hl. menu (ukončení funkce a návrat na začátek nekonečného while true cyklu / hl. menu).

    cislo_ukolu = int(vstup_cislo_ukolu) # převod už prověřené uživatelské hodnoty (čísla) na datový typ integer

    # 2) kontrola správnosti zadaného čísla z rozsahu existujících úkolů - místo vyvolávání výjimky IndexError
    if cislo_ukolu < 1 or cislo_ukolu > len(ukoly):  # Pokud uživatel zadal číslo úkolu menší než 1 a větší než aktuální číselný rozsah úkolů, 
        print(f"Úkol se zadaným pořadovým číslem v seznamu neexistuje. Zadejte číslo od 1 do {len(ukoly)}.") # vytisknu mu hlášku
        return False  # a vráť stav False a uživatele do hl. menu (ukončení funkce a návrat na začátek nekonečného while true cyklu / hl. menu).

    # úspěšně smazaný úkol ze seznamu
    smazany_ukol = ukoly.pop(cislo_ukolu - 1)  # index pozice snížen o 1, Python začíná od 0, zatímco číslování úkolů v seznamu od 1
    print(f"Úkol '{smazany_ukol['nazev']}' byl odstraněn.")
    return True


# Spuštění programu
hlavni_menu()