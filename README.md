# Projekt 1 – Task Manager (Správce úkolů)

Jednoduchá **konzolová aplikace v Pythonu** pro správu osobních úkolů.  
Umožňuje přidávat, zobrazovat a mazat úkoly prostřednictvím textového menu.

Autor: **Jana Staňková**  
Rok: **2025**

---

## Cíl projektu

Tento projekt byl vytvořen v rámci kurzu **ENGETO Python Developer – Projekt 1**  
Cílem je procvičit:
- práci s funkcemi a cykly,  
- manipulaci se seznamy a slovníky,  
- ošetření chyb pomocí výjimek (`try/except`),  
- interaktivní vstup od uživatele a výpis do konzole.

---

## Popis programu

Program představuje **Task Manager (Správce úkolů)** – jednoduchý systém pro evidenci úkolů,  
který umožňuje:

1. **Přidat nový úkol**  
   - Uživatel zadá název a popis úkolu.  
   - Oba údaje jsou povinné (kontrola prázdných hodnot).  
   - Úkol je uložen jako slovník (`{"nazev": ..., "popis": ...}`) do seznamu všech úkolů.

2. **Zobrazit všechny úkoly**  
   - Program vypíše všechny uložené úkoly v přehledném seznamu s pořadovým číslem.  
   - Pokud je seznam prázdný, vypíše se odpovídající hláška.

3. **Odstranit úkol**  
   - Uživatel zadá číslo úkolu, který chce odstranit.  
   - Program ošetřuje chybné vstupy (`IndexError`, `ValueError`).  
   - Po úspěšném odstranění úkolu se vypíše potvrzení.

4. **Ukončit program**  
   - Volbou čísla 4 se program ukončí.

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

---

## Testování projektu

Pro ověření funkčnosti programu byl vytvořen přehled testovacích scénářů
v souboru Task_Manager_Test_Cases.xlsx.

Tento dokument obsahuje:
- seznam jednotlivých funkcí programu,
- očekávané vstupy a výstupy,
- kroky k provedení testu,
- očekávaný výsledek a skutečný výsledek testu.

Díky tomuto souboru je možné jednoduše ověřit, že všechny klíčové části aplikace
fungují správně (např. přidání úkolu, mazání úkolu, ošetření chybných vstupů apod.).

Testy jsou koncipovány jako manuální testovací případy a lze je použít i jako
základ pro budoucí automatizované testování (např. pomocí modulu unittest).

---

## Ukázka výstupu

```
Správce úkolů - Hlavní menu
1. Přidat nový úkol
2. Zobrazit všechny úkoly
3. Odstranit úkol
4. Konec programu

Vyberte možnost (1-4): 1
Zadejte název úkolu: nakoupit
Zadejte popis úkolu: mléko, chléb, máslo
Úkol 'nakoupit' byl přidán.
```

---

## Klíčové prvky kódu

- **Funkce `hlavni_menu()`**  
  Nekonečný cyklus zobrazující nabídku akcí a zajišťující navigaci mezi funkcemi.

- **Funkce `pridat_ukol()`**  
  Přidává nový úkol do seznamu `ukoly`.

- **Funkce `zobrazit_ukoly()`**  
  Vypisuje všechny uložené úkoly s pořadovým číslem v seznamu, jejich názvem a popisem.

- **Funkce `odstranit_ukol()`**  
  Odstraňuje úkol podle zadaného pořadového čísla a ošetřuje chybné vstupy.

---

## Použité konstrukce a principy

- Seznamy (`list`) a slovníky (`dict`)  
- Funkce (`def`)  
- Cykly a podmínky  
- Výjimky (`try / except`)  
- F-stringy pro formátování textu  
- Opakované zobrazování menu pomocí nekonečného cyklu `while True`

---
