# Playwright – automatizované smoke testy

Tento projekt obsahuje sadu jednoduchých **smoke testů** pro web  
https://engeto.cz, napsaných v Pythonu pomocí **Playwright** a **pytest-playwright**.

Cílem testů je rychle ověřit, že:
- stránka je dostupná,
- má správný title,
- obsahuje hlavní nadpis (H1),
- je přítomen a viditelný odkaz na kontakt.

Testy jsou záměrně krátké, čitelné a zaměřené na stabilitu.

---

## Použité technologie
- Python 3
- Playwright (sync API)
- pytest
- pytest-playwright

---

## Struktura testů
Testy využívají:
- **Playwright expect API** (`expect(locator).to_be_visible()` apod.)  
  → zajišťuje automatické čekání a vyšší stabilitu UI testů
- **fixture s BASE_URL**, aby se neopakovalo `page.goto()` v každém testu
- **role-based selektory** (`get_by_role`) místo křehkých CSS selektorů
- kontrolu **jednoznačnosti prvků** (`to_have_count(1)`)

---

## Spuštění testů

Nejprve nainstaluj závislosti:

```bash
pip install pytest playwright pytest-playwright
playwright install

Poté spusť testy:
pytest -v

## Poznámka

Projekt je koncipován jako smoke test suite – nejedná se o plnohodnotný E2E framework, ale o rychlé a spolehlivé ověření, že web funguje a klíčové prvky jsou dostupné.
