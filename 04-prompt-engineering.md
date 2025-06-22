# Část 4: Nejlepší praktiky Prompt Engineeringu

## Úvod
V této části se naučíte, jak efektivně vytvářet prompty pro modely OpenAI, abyste získali co nejlepší výsledky. Budeme vycházet z oficiálních doporučení OpenAI a ukážeme si konkrétní příklady pro náš nástroj na překlad textu do emoji.

## Zásady a doporučení pro tvorbu promptů

### 1. Používejte nejnovější model
Pro nejlepší výsledky vždy používejte nejnovější a nejvýkonnější modely.

### 2. Instrukce na začátek a oddělujte je od vstupu
Dejte jasné instrukce na začátek promptu a oddělte je od vstupního textu pomocí znaků jako `"""` nebo `###`.

**Méně efektivní:**

Převeď následující text na emoji: {text}

**Lepší:**

Převeď následující text na emoji.
Text: """{text}"""

### 3. Buďte konkrétní, popisní a detailní
Specifikujte přesně, co očekáváte – kontext, výsledek, délku, formát, styl atd.

**Méně efektivní:**

Napiš báseň o AI.

**Lepší:**

Napiš krátkou inspirativní báseň o umělé inteligenci, zaměřenou na generování videa, ve stylu Franze Kafky.

### 4. Ukažte požadovaný formát výstupu na příkladech
Modely lépe reagují, když jim ukážete konkrétní příklad požadovaného výstupu.

**Méně efektivní:**

Extrahuj entity z textu: {text}

**Lepší:**

Extrahuj entity z textu níže. Nejprve firmy, pak osoby, pak témata, nakonec obecná témata.
Formát:
Firmy: <seznam>
Osoby: <seznam>
Témata: <seznam>
Obecná témata: <seznam>
Text: {text}

### 5. Začněte zero-shot, pak few-shot, případně fine-tune
- **Zero-shot:**
  Převeď následující text na emoji.
  Text: {text}
  Emoji:
- **Few-shot:**
  Převeď následující texty na emoji.
  Text 1: "Dívka jde do školy."
  Emoji 1: 👧 🏫
  Text 2: "Pes běží v parku."
  Emoji 2: 🐕 🏃‍♂️ 🌳
  Text 3: {text}
  Emoji 3:

### 6. Vyhýbejte se vágním a nejasným instrukcím
**Méně efektivní:**

Popis by měl být krátký, jen pár vět.

**Lepší:**

Použij 3–5 vět pro popis produktu.

### 7. Neříkejte jen, co nedělat – řekněte, co dělat místo toho
**Méně efektivní:**

Nedávej osobní údaje.

**Lepší:**

Pokud uživatel požádá o osobní údaje, odkaž ho na stránku s nápovědou.

### 8. Pro generování kódu používejte "nápovědné slovo"
Například pro Python začněte prompt slovem `import`.

### 9. Experimentujte a iterujte
Prompt engineering je iterativní proces. Zkoušejte různé varianty a sledujte, co funguje nejlépe.

## Tipy pro práci s parametry modelu
- `model`: Vyberte nejnovější model pro lepší výsledky.
- `temperature`: Pro kreativní úlohy zvyšte, pro fakta snižte (např. 0).
- `max_completion_tokens`: Nastavte maximální délku výstupu.
- `stop`: Definujte (text), kdy má model přestat generovat výstup.

## Zdroj

[OpenAI Prompt Engineering Guide](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api).
