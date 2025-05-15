# Část 4: Prompt Engineering pro efektivní interakce s AI

## Úvod
V této části prozkoumáme, jak vytvářet efektivní prompty pro Large Language Models (LLMs), přičemž využijeme náš nástroj pro překlad emoji v příkazové řádce jako praktický příklad. Dobrý prompt engineering je zásadní pro získání nejlepších výsledků z AI modelů.

## Základní principy Prompt Engineeringu

### 1. Buďte konkrétní a jasní
- Používejte přesný jazyk a vyhýbejte se nejednoznačnosti
- Zahrňte veškerý potřebný kontext v promptu
- Příklad z našeho CLI nástroje:
```python
"Převeď následující příběh nebo zprávu do série emoji, které nejlépe reprezentují jeho význam, postavy, emoce a klíčové události. Použij 10-25 emoji:"
```

### 2. Strukturujte své prompty
- Rozdělte komplexní úlohy na jasné komponenty
- Používejte konzistentní formát
- Zahrňte omezení a požadavky (jako je náš limit počtu emoji)

### 3. Poskytněte příklady (Few-Shot Learning)
Zvažte vylepšení našeho současného promptu o příklady:
```python
"""
Převeď následující příběh do emoji (10-25):
Příklad:
Vstup: "Šťastná dívka šla na pláž za slunečného dne a postavila hrad z písku"
Výstup: 👧 😊 🏖️ ☀️ 🏰 

Váš text: {text}
"""
```

## Praktická cvičení

### Cvičení 1: Variace promptu
Zkuste upravit náš základní prompt k dosažení různých výsledků:

1. Původní prompt:
```python
text_to_emojis("Převeď tento text na emoji")
```

2. Vylepšený prompt s více kontextem:
```python
text_to_emojis("Analyzuj emoční tón a klíčové prvky tohoto textu, poté je znázorni vhodnými emoji")
```

### Cvičení 2: Přidání parametrů
Experimentujte s přidáním specifických požadavků:
- Zaměření na emoce
- Časová osa příběhu
- Důraz na postavy

## Tipy pro náš CLI nástroj

1. **Úprava délky výstupu**
   - Upravte omezení "10-25 emoji" podle vašich potřeb
   - Zvažte délku textu ve vztahu k počtu emoji

2. **Vylepšení kontextu**
   - Přidejte specifické instrukce pro zpracování různých typů textu
   - Zahrňte pokyny pro zachování soudržnosti příběhu

3. **Zpracování chyb**
   - Přidejte validační instrukce do promptu
   - Specifikujte chování pro nouzové situace

## Běžné chyby, kterým se vyhnout

1. **Příliš složité prompty**
   - Udržujte instrukce jasné a stručné
   - Vyhněte se protichůdným požadavkům

2. **Nedostatek specifičnosti**
   - Zahrňte jasné parametry
   - Definujte očekávaný formát výstupu

3. **Chybějící kontext**
   - Poskytněte nezbytné informace o pozadí
   - Specifikujte zamýšlený případ použití

## Praktické cvičení

Upravte prompt v našem CLI nástroji tak, aby:
1. Zaměřil se na emocionální reprezentaci
2. Zachoval chronologii příběhu
3. Přidal specifické zpracování různých textových žánrů

```python
@magentic.prompt("""
Analyzuj následující text a vytvoř sekvenci emoji, která:
1. Zachycuje hlavní emoční cestu (prioritizuj emoji související s emocemi)
2. Sleduje chronologické pořadí událostí
3. Používá 10-25 emoji, oddělených mezerami
4. Přizpůsobuje styl podle žánru (příběh/zprávy/konverzace)

Text k převodu: {text}
""", model=chat_model)
```

## Další kroky
- Experimentujte s různými strukturami promptů
- Testujte různé typy a žánry textů
- Dokumentujte, které prompty fungují nejlépe pro konkrétní případy použití
- Zvažte implementaci šablon promptů pro různé scénáře

Pamatujte: Dobrý prompt engineering je iterativní. Testujte různé přístupy a zdokonalujte je na základě výsledků.
