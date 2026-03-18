# Complete Label Layout Example

*Based on JSON file: 4500801837-00000017-205456MK26.json*

## Product Information from JSON

```
Style ID: 205456MK26
Product Type: T-SHIRT
Family: T-shirts (M1WTTT)
Line: WOMAN
Age: ADULT
Gender: FEMALE
Packaging: FOLDED
Origin: Morocco
Destination: Spain (D001 - LLIÇÀ)
```

---

## LABEL LAYOUT BREAKDOWN

### 1. PRODUCT CODE SECTION
**Source:** `TRANSLATIONS&RULES(16).xlsx` → Sheet: `JSON-RULES`

**Lookup Logic:**
- Match: `DESC. GEN.` = "WOMAN" + `PACKAGING` = "FOLDED"
- Result: `ITALIAN CODE` = **"CODE 15"**

**Required Document:**
- ✅ **CODE 15.pdf** - Visual reference sheet for product codes/barcodes

---

### 2. REGULATORY SYMBOLS SECTION
**Source:** `TRANSLATIONS&RULES(16).xlsx` → Sheet: `JSON-RULES`

**Lookup Result:**
- `EAC` = 1 (YES)
- `TRIMAN` = "T-SHIRT" (YES)
- `KOREAN SYMBOL` = (blank/NO)
- `MCA LAW` = (blank/NO)

**Required Documents:**
- ✅ **EAC.pdf** or **EAC.gif** - Eurasian Conformity mark (must appear on label)
- ✅ **triman 1.pdf** (or triman 2.pdf, triman 3.pdf) - French recycling symbol (must appear for T-shirts)
- ❌ KOREAN SYMBOL.png - NOT needed (not required for this product)

---

### 3. COUNTRY OF ORIGIN SECTION
**Source:** `TRANSLATIONS&RULES(16).xlsx` → Sheet: `MADE IN COUNTRY`

**From JSON:** Origin = "Morocco"

**Lookup Logic:**
- Match: `CODE SAP` contains "MA" OR `ENGLISH` contains "MOROCCO"

**Required Translations:**
```
English:    MADE IN MOROCCO
Spanish:    HECHO EN MARRUECOS
French:     FABRIQUE AU MAROC
Italian:    FABBRICATO IN MAROCCO
German:     HERGESTELLT IN MAROKKO
Portuguese: FABRICADO EM MARROCOS
Chinese:    摩洛哥制造
... (33 languages total)
```

**Required Document:**
- ✅ **TRANSLATIONS&RULES(16).xlsx** → Sheet: `MADE IN COUNTRY`

---

### 4. MATERIAL COMPOSITION SECTION
**Source:** `TRANSLATIONS&RULES(16).xlsx` → Sheet: `MATERIALS`

**From JSON:**
- Fabric Code: C005
- Fabric Name: COTTON
- Percentage: 100%

**Lookup Logic:**
- Match: `CODE` = "C005"

**Required Translations:**
```
English:    100% COTTON
Spanish:    100% ALGODÓN
French:     100% COTON
Italian:    100% COTONE
German:     100% BAUMWOLLE
Portuguese: 100% ALGODÃO
Chinese:    100% 棉
... (33 languages total)
```

**Required Document:**
- ✅ **TRANSLATIONS&RULES(16).xlsx** → Sheet: `MATERIALS`

---

### 5. CARE INSTRUCTIONS SECTION
**Source:** `TRANSLATIONS&RULES(16).xlsx` → Sheet: `SAP-WASHING RULES`

**From JSON:**
- Care Code 1: S02 (SAP Code: 2)
- Care Code 2: S12 (SAP Code: 1)
- Care Code 3: S14 (SAP Code: 1)

**Lookup Logic:**
- Match: `CODIGO SAP` = "S02", "S12", "S14"

**Example for S02:**
```
English:    MACHINE WASH MAX 30°C / 85ºF, SHORT SPIN DRY-DELICATE WASH
Spanish:    LAVAR A MAQUINA MÁX. 30°C CENTRIFUGADO CORTO-LAVADO DELICADO
French:     LAVAGE EN MACHINE MAX 30°C ESSORAGE COURT - LAVAGE DÉLICAT
Portuguese: LAVAR À MÁQUINA MÁX. 30°C CENTRIFUGAÇÃO CURTA-LAVAGEM DELICADA
... (8 languages available)
```

**Required Document:**
- ✅ **TRANSLATIONS&RULES(16).xlsx** → Sheet: `SAP-WASHING RULES`

---

### 6. IMPORTER INFORMATION SECTION
**Source:** `TRANSLATIONS&RULES(16).xlsx` → Sheet: `GARMENT IMPORTERS`

**From JSON:** Destination = Spain (D001)

**Lookup Logic:**
- Match: `COUNTRY` = "Spain" OR `COUNTRY CODE` = "ES"

**Expected Output:**
```
Importer: MANGO MNG KFT.
Address: [Legal address in Spain]
Tax ID: [Spanish tax registration number]
```

**Required Document:**
- ✅ **TRANSLATIONS&RULES(16).xlsx** → Sheet: `GARMENT IMPORTERS`

---

### 7. BRAND/DISTRIBUTION MARKING
**Source:** Direct PDF file

**Required Document:**
- ✅ **ADHEDIST-mango.pdf** - Mango brand adhesive/distribution marking

---

### 8. ADDITIONAL ELEMENTS (if applicable)
**Source:** Direct PDF file

**Required Document:**
- ⚠️ **ÉLÉMENTS.pdf** - Additional French regulatory elements (may be needed depending on destination)

---

### 9. ARABIC NUMBER CONVERSION (if needed)
**Source:** `numeros_equivalente_arabe_valores.xlsx` OR `TRANSLATIONS&RULES(16).xlsx` → Sheet: `ARABIC NUMBER`

**Use Case:** If label needs Arabic numerals for Middle East destinations

**Required Document:**
- ⚠️ **numeros_equivalente_arabe_valores.xlsx** (conditional - only for Arabic markets)

---

## COMPLETE LABEL LAYOUT VISUALIZATION

```
┌─────────────────────────────────────────────────────────┐
│  [MANGO LOGO - ADHEDIST-mango.pdf]                      │
├─────────────────────────────────────────────────────────┤
│  Style: 205456MK26                                      │
│  [BARCODE - from CODE 15.pdf reference]                 │
├─────────────────────────────────────────────────────────┤
│  REGULATORY SYMBOLS:                                    │
│  [EAC.pdf]  [triman 1.pdf]                             │
├─────────────────────────────────────────────────────────┤
│  MADE IN MOROCCO                                        │
│  HECHO EN MARRUECOS                                     │
│  FABRIQUE AU MAROC                                      │
│  FABBRICATO IN MAROCCO                                  │
│  (from MADE IN COUNTRY sheet)                           │
├─────────────────────────────────────────────────────────┤
│  100% COTTON                                            │
│  100% ALGODÓN                                           │
│  100% COTON                                             │
│  100% COTONE                                            │
│  (from MATERIALS sheet)                                 │
├─────────────────────────────────────────────────────────┤
│  CARE INSTRUCTIONS:                                     │
│  • MACHINE WASH MAX 30°C, SHORT SPIN DRY               │
│  • LAVAR A MAQUINA MÁX. 30°C CENTRIFUGADO CORTO        │
│  • LAVAGE EN MACHINE MAX 30°C ESSORAGE COURT           │
│  (from SAP-WASHING RULES sheet)                         │
├─────────────────────────────────────────────────────────┤
│  IMPORTER:                                              │
│  MANGO MNG KFIT.                                        │
│  [Address and Tax ID]                                   │
│  (from GARMENT IMPORTERS sheet)                         │
└─────────────────────────────────────────────────────────┘
```

---

## SUMMARY: REQUIRED FILES FOR THIS LABEL

### ✅ MUST HAVE (7 files):
1. **4500801837-00000017-205456MK26.json** - Source data
2. **TRANSLATIONS&RULES(16).xlsx** - Master reference (5 sheets used):
   - JSON-RULES
   - MADE IN COUNTRY
   - MATERIALS
   - SAP-WASHING RULES
   - GARMENT IMPORTERS
3. **CODE 15.pdf** - Product code reference
4. **EAC.pdf** (or EAC.gif) - Regulatory symbol
5. **triman 1.pdf** (or 2, or 3) - Regulatory symbol
6. **ADHEDIST-mango.pdf** - Brand marking

### ❌ NOT NEEDED for this specific product:
- KOREAN SYMBOL.png (not required by rules)
- CODE 1-14, 16.pdf (only CODE 15 is needed)
- numeros_equivalente_arabe_valores.xlsx (destination is Spain, not Arabic market)
- ÉLÉMENTS.pdf (may not be required for this specific product)
- GI000DPO-SAP_1.pdf (SAP reference, not for label printing)
- GI001BAW-GI001BAC.pdf (additional codes, not matched)
- PVPV0102-PVP002XG.pdf (price codes, not for label)

---

## KEY INSIGHT

**The JSON-RULES sheet is the MASTER DECISION MAKER** that determines:
- Which CODE PDF to use (CODE 15 in this case)
- Which regulatory symbols are required (EAC + Triman)
- Which additional rules apply (MCA, Korean, etc.)

All other sheets provide the **translation data** that populates the label text in multiple languages.

The **PDF files** provide the **visual assets** (symbols, logos, code references) that must be embedded in the final label layout.
