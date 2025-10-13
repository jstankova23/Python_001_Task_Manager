# PROJEKT 1 - TASK MANAGER - SEZNAM PRO SPRÁVU ÚKOLŮ
# ukoly [] = seznam slovníků (1 úkol = 1 slovník)
# ukol {}  = slovník (klíče: nazev, popis)

ukoly = []      # vytvoření seznamu úkolů, což je seznam slovníků

# Funkce hlavni_menu zobrazuje hlavní menu s volbami pro uživatelský vstup (1-4) namapovanými s jednotlivými funkcemi 
# funkce hlavni_menu se spouští stále dokola po dokončení běhu jakékoliv funkce, dokud není přerušena volbou 4 s break
def hlavni_menu():
    while True:   # iterace, po dokončení běhu každé funkce se zobrazuje hlavní menu, dokud ho nepřeruší volba 4 s break
        print("\nSprávce úkolů - Hlavní menu")    # \n odsazení o řádek kvůli přehlednosti
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        
        try:
            volba = int(input("Vyberte možnost (1-4): "))    # uživatel volí akci spojenou s příslušnou funkcí
            # namapování uživatelské volby s příslušnými funkcemi, pouze volba 4 není spojena s funkcí, ale s příkazem break
            if volba == 1:
                pridat_ukol()
            elif volba == 2:
                zobrazit_ukoly()
            elif volba == 3:
                odstranit_ukol()
            elif volba == 4:
                print("Konec programu.")
                break                   # ukončení cyklu while
            else:
                raise IndexError # vyvolání výjimky pro účely PyTestu, i když volby 1-4 nejsou seznam, ale jen tisk, výjimka IndexError je "umělá"
        except IndexError:
            print("Volba akce se zadaným číslem neexistuje. Zadejte číslo v rozsahu 1-4.")        
        except ValueError:
            print("Chybně zadaný datový typ. Zadejte číslo v rozsahu 1-4.")  # výjimka s hláškou, když zadá uživatel jiný datový typ než int


# Funkce pridat_ukol vytvoří nový úkol (slovník) do seznamu úloh
# 1 úkol = 1 slovník (klíč, hodnota), tzn. seznam úkolů je seznam slovníků, kde každý úkol je samostatný slovník
# klíč a hodnota slovníku jsou povinné, tzn. název a popis úkolu jsou oba povinné údaje
# metoda strip() pro odstranění bílých znaků z obou stran textu zadaného uživatelem
def pridat_ukol():
    nazev = input("Zadejte název úkolu: ").strip()  
    popis = input("Zadejte popis úkolu: ").strip()

    if not nazev or not popis:
        print("Nebyl zadán název nebo popis úkolu. Prosím, zadejte obě tyto hodnoty (název, popis úkolu).")
        return              # konec funkce, návrat do hlavního menu, které se znovu zobrazí

    # vytvoření slovníku/úkolu se svým klíčem/názvem úkolu a hodnotou/popisem úkolu (1 úkol = 1 slovník)
    # přiřazení slovníku/úkolu do seznamu úkolů
    ukol = {"nazev": nazev, "popis": popis}      # vytvoření slovníku s úkolem (klíč/nazev, hodnota/popis)
    ukoly.append(ukol)                           # přidání úkolu/slovníku do seznamu úkolů
    print(f"Úkol '{nazev}' byl přidán.")         # hláška pro uživatele


# Funkce zobrazit_ukol zobrazí seznam úkolů, což je seznam slovníků s jejich klíči a hodnotami; 
# očíslování slovníků/úkolů ze seznamu úkolů přes for cyklus s funkcí enumerate() a argumentem start=1 pro počáteční číslo
def zobrazit_ukoly():
    print("\nSeznam úkolů")  # \n odsazení o řádek kvůli přehlednosti, oddělení od řádku s uživatelským vstupem
    if not ukoly:            # pro případ prázdného seznamu úkolů
        print("Seznam úkolů neobsahuje žádné úlohy.")  # tisk oznámení
    else:
        for i, ukol in enumerate(ukoly, start=1):  # iterace, očíslování všech slovníků/úkolů, nutné pro fci odstranit_ukol
            print(f"{i}. {ukol['nazev']} - {ukol['popis']}") # tisk pořadového čísla, klíče a hodnoty daného slovníku


# Funkce odstranit_ukol odstraní úkol dle zadaného pořadového čísla vygenerovaného ve funkci zobrazit_ukoly 
# nejdříve je tedy nutné zobrazit aktuální seznam všech úkolů přes funkci zobrazit_ukoly
def odstranit_ukol():
    zobrazit_ukoly()

    try:
        cislo_ukolu = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
        smazany_ukol = ukoly.pop(cislo_ukolu - 1) # index pozice snížen o 1, Python začíná od 0, zatímco číslování úkolů v seznamu od 1
        print(f"Úkol '{smazany_ukol}' byl odstraněn.")    
    except IndexError:
        print("Úkol se zadaným pořadovým číslem v seznamu neexistuje.") # výjimka s hláškou, když zadá uživatel neexistující číslo
    except ValueError:
        print("Chybně zadaný datový typ, zadejte číslo úkolu určeného ke smazání.")  # výjimka s hláškou, když zadá uživatel jiný datový typ než int


# Spuštění programu
hlavni_menu()







