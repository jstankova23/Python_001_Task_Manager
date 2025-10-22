# Projekt 1 – Task Manager (Správce úkolů)

Jednoduchá **konzolová aplikace v Pythonu** pro správu osobních úkolů.  
Umožňuje přidávat, zobrazovat a mazat úkoly prostřednictvím textového menu.
Program neukládá data trvale (seznam úkolů je pouze v paměti).

Autor: **Jana Staňková**  
Rok: **2025**

---

## Cíl projektu

Tento projekt byl vytvořen po ukončení kurzu **ENGETO Testing Akademie – Projekt 1**.  
Cílem je procvičit:
- práci s funkcemi a cykly,  
- manipulaci se seznamy a slovníky,  
- kontrolu a validaci uživatelského vstupu,  
- návratové hodnoty funkcí (`True` / `False`),  
- interaktivní vstup od uživatele a výpis do konzole.

---

## Popis programu

Program představuje **Task Manager (Správce úkolů)** – jednoduchý systém pro evidenci úkolů,  
který umožňuje:

1. **Přidat nový úkol**  
   - Uživatel zadá název a popis úkolu.  
   - Oba údaje jsou povinné (kontrola prázdných hodnot).  
   - Funkce nyní vrací logický stav (`True` / `False`) podle úspěšnosti přidání úkolu.  
   - Úkol je uložen jako slovník (`{"nazev": ..., "popis": ...}`) do seznamu všech úkolů.

2. **Zobrazit všechny úkoly**  
   - Program vypíše všechny uložené úkoly v přehledném seznamu s pořadovým číslem.  
   - Pokud je seznam prázdný, zobrazí hlášku **„Seznam úkolů je prázdný.“**

3. **Odstranit úkol**  
   - Uživatel zadá pořadové číslo úkolu, který chce odstranit.  
   - Kontrola vstupu probíhá **před voláním funkce** pomocí metody `isdecimal()`  
     a kontroly rozsahu (`0 < číslo <= len(ukoly)`).  
   - Záporná a desetinná čísla nejsou považována za platný vstup.  
   - Pokud je seznam úkolů prázdný, funkce ihned vypíše hlášku a vrátí se do hlavního menu.  
   - Funkce vrací stav (`True` / `False`) podle úspěšnosti odstranění úkolu.  
   - Program již nevyužívá výjimky `IndexError` ani `ValueError`.

4. **Ukončit program**  
   - Volbou čísla 4 se program ukončí.

---

## Novinky ve verzi z 22. 10. 2025

### Úpravy ve zdrojovém kódu (`task_manager_p1.py`)
- Funkce `hlavni_menu()`, `odstranit_ukol()` validace vstupů přesunuta **před volání funkcí** – odstraněny bloky `try/except`.  
- Funkce `pridat_ukol()` a `odstranit_ukol()` nově vracejí hodnoty `True` / `False`.  
- Funkce `odstranit_ukol()` úprava chování při prázdném seznamu úkolů, změna hlášky – okamžitý návrat do hlavního menu.  
- Změna hlášky:  
  > „Seznam úkolů neobsahuje žádné úlohy.“ → „Seznam úkolů je prázdný.“  
- Aktualizace hlavičky programu (informace o autorovi a verzi).

### Úpravy v testovacích scénářích (`Task_Manager_Test_Cases.xlsx`)
- Odstranění duplicitního kroku „Spustit program“ ze všech testů. 
- Oprava názvu a popisu TC17 pro test zobrazení prázdného seznamu úkolů 
- Aktualizace testů TC02, TC03, TC17, TC24 podle nové hlášky pro zobrazení prázdného seznamu úkolů.  
- Zohlednění odstranění výjimek (`IndexError`, `ValueError`) ve funkcích `hlavni_menu()` a `odstranit_ukol()`.  
- Přidány nové testovací scénáře pro funkci `odstranit_ukol()`:
  - **TC22** – zadání desetinného čísla (float)  
  - **TC25** – zadání hodnoty `0`  
  - **TC26** – zadání záporného čísla  
  - **TC28** – prázdný seznam úkolů při pokusu o výmaz  
  Pozn.: Hláška pro TC22 a TC26 odpovídá chybě špatného datového typu,  
  protože metoda `isdecimal()` povoluje pouze číslice 0–9.
- Zohlednění změny kontroly a hlášky u prázdného seznamu úkolů ve funkci odstranit_ukol() v TC03
---

## Spuštění programu

### Požadavky
- Python 3.x (doporučeno 3.10 nebo novější)
- Konzolové prostředí (např. VS Code, IDLE, terminál)

### Postup instalace a spuštění
```bash
# Naklonuj repozitář
git clone https://github.com/<tvoje_jmeno>/<nazev_repozitare>.git
cd <nazev_repozitare>

# Spusť aplikaci
python task_manager_p1.py
```

---

## Struktura projektu

```
Python_001_Task_Manager
├── task_manager_p1.py             # hlavní skript aplikace
├── Task_Manager_Test_Cases.xlsx   # testovací případy (manuální testy)
└── README.md                      # dokumentace projektu
```

---

## Testování projektu

Testování probíhá manuálně dle dokumentu **Task_Manager_Test_Cases.xlsx**,  
který obsahuje:

- popisy funkcí programu,  
- vstupní podmínky a testovací kroky,  
- očekávané a skutečné výsledky.  

Manuální testy ověřují běžné i hraniční vstupy (např. nečíselné, záporné či desetinné hodnoty)  
a slouží také jako základ pro možné budoucí automatizované testování.

---

## Ukázka výstupu

```
Správce úkolů - Hlavní menu
1. Přidat nový úkol
2. Zobrazit všechny úkoly
3. Odstranit úkol
4. Konec programu
Vyberte možnost (1-4): 3

Seznam úkolů
1. nákup - pečivo, máslo, brambory
2. knihovna - vrátit 3 půjčené knihy
Zadejte číslo úkolu, který chcete odstranit: 2
Úkol 'knihovna' byl odstraněn.

Správce úkolů - Hlavní menu
1. Přidat nový úkol
2. Zobrazit všechny úkoly
3. Odstranit úkol
4. Konec programu
Vyberte možnost (1-4):
```

---

## Klíčové prvky kódu

- **`hlavni_menu()`** – hlavní navigační funkce programu, řídící smyčka programu s cyklem while true (nevrací hodnotu), volá ostatní funkce podle uživatelské volby  
- **`pridat_ukol()`** – přidání nového úkolu, vrací `True` / `False`  
- **`zobrazit_ukoly()`** – přehled uložených úkolů (nevrací hodnotu) 
- **`odstranit_ukol()`** – mazání úkolu podle zadaného pořadí, vrací True/False podle úspěchu 
---

## Licence
Projekt vytvořen pro studijní účely po ukončení kurzu **ENGETO Testing Akademie**.
