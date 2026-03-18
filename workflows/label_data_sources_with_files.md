# LABEL DATA SOURCES - Product 205456MK26

*Showing exactly which file provides each piece of information*

---

## LABEL SECTION 1: PRODUCT INFO

### Style ID: 205456MK26
**Source:** `4500801837-00000017-205456MK26.json`
- Path: `data[0]['StyleColor'][0]['StyleID']`

### Color: 01 - WHITE
**Source:** `4500801837-00000017-205456MK26.json`
- Path: `data[0]['StyleColor'][0]['MangoColorCode']` + `data[0]['StyleColor'][0]['Color']`

### Season: SS2026
**Source:** `4500801837-00000017-205456MK26.json`
- Path: `data[0]['LabelOrder']['Temporada']`

---

## LABEL SECTION 2: SIZES

### Sizes: XXS/XS/S/M/L/XL/XXL/1XL/2XL/3XL/4XL
**Source:** `4500801837-00000017-205456MK26.json`
- Path: `data[0]['StyleColor'][0]['SizeRange'][0]['SizeName']`

---

## LABEL SECTION 3: ORIGIN (33 LANGUAGES)

### "Made in Morocco" translations
**Source:** `TRANSLATIONS&RULES(16).xlsx` → Sheet: **MADE IN COUNTRY**
- Lookup: Match `ENGLISH` column contains "MOROCCO"
- Returns: Translations in 33 languages

**Raw data from JSON:**
- `4500801837-00000017-205456MK26.json`
- Path: `data[0]['StyleColor'][0]['Origin']['countryorigin']` = "Morocco"

**Translations from Excel:**
```
English:    MADE IN MOROCCO          {TRANSLATIONS&RULES(16).xlsx → MADE IN COUNTRY}
Spanish:    HECHO EN MARRUECOS       {TRANSLATIONS&RULES(16).xlsx → MADE IN COUNTRY}
French:     FABRIQUE AU MAROC        {TRANSLATIONS&RULES(16).xlsx → MADE IN COUNTRY}
Italian:    FABBRICATO IN MAROCCO    {TRANSLATIONS&RULES(16).xlsx → MADE IN COUNTRY}
German:     HERGESTELLT IN MAROKKO   {TRANSLATIONS&RULES(16).xlsx → MADE IN COUNTRY}
Portuguese: FABRICADO EM MARROCOS    {TRANSLATIONS&RULES(16).xlsx → MADE IN COUNTRY}
Chinese:    摩洛哥制造                  {TRANSLATIONS&RULES(16).xlsx → MADE IN COUNTRY}
Korean:     모로코 제조                 {TRANSLATIONS&RULES(16).xlsx → MADE IN COUNTRY}
Arabic:     صنع في المغرب            {TRANSLATIONS&RULES(16).xlsx → MADE IN COUNTRY}
... (33 languages total)
```

---

## LABEL SECTION 4: COMPOSITION (33 LANGUAGES)

### "100% Cotton" translations
**Source:** `TRANSLATIONS&RULES(16).xlsx` → Sheet: **MATERIALS**
- Lookup: Match `CODE` = "C005"
- Returns: Material name translations in 33 languages

**Raw data from JSON:**
- `4500801837-00000017-205456MK26.json`
- Path: `data[0]['StyleColor'][0]['Composition'][0]['Fabric'][0]`
  - `FabricCode` = "C005"
  - `FabricName` = "COTTON"
  - `FabricPercent` = "100"

**Translations from Excel:**
```
English:    100% COTTON              {TRANSLATIONS&RULES(16).xlsx → MATERIALS}
Spanish:    100% ALGODÓN             {TRANSLATIONS&RULES(16).xlsx → MATERIALS}
French:     100% COTON               {TRANSLATIONS&RULES(16).xlsx → MATERIALS}
Italian:    100% COTONE              {TRANSLATIONS&RULES(16).xlsx → MATERIALS}
German:     100% BAUMWOLLE           {TRANSLATIONS&RULES(16).xlsx → MATERIALS}
Portuguese: 100% ALGODÃO             {TRANSLATIONS&RULES(16).xlsx → MATERIALS}
Chinese:    100% 棉                  {TRANSLATIONS&RULES(16).xlsx → MATERIALS}
Korean:     면 100%                  {TRANSLATIONS&RULES(16).xlsx → MATERIALS}
Arabic:     ١٠٠٪ قطن                {TRANSLATIONS&RULES(16).xlsx → MATERIALS}
... (33 languages total)
```

---

## LABEL SECTION 5: CARE INSTRUCTIONS (8 LANGUAGES)

### Care Instruction 1: "Machine wash max 30°C, short spin"
**Source:** `TRANSLATIONS&RULES(16).xlsx` → Sheet: **SAP-WASHING RULES**
- Lookup: Match `CODIGO SAP` = "S02"
- Returns: Care instruction translations in 8 languages

**Raw data from JSON:**
- `4500801837-00000017-205456MK26.json`
- Path: `data[0]['StyleColor'][0]['CareInstructions'][0]`
  - `CareCode` = "S02"
  - `CareSAPCode` = "2"

**Translations from Excel:**
```
English:    MACHINE WASH MAX 30°C / 85ºF, SHORT SPIN DRY-DELICATE WASH
            {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Spanish:    LAVAR A MAQUINA MÁX. 30°C CENTRIFUGADO CORTO-LAVADO DELICADO
            {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
French:     LAVAGE EN MACHINE MAX 30°C ESSORAGE COURT - LAVAGE DÉLICAT
            {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Portuguese: LAVAR À MÁQUINA MÁX. 30°C CENTRIFUGAÇÃO CURTA-LAVAGEM DELICADA
            {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Russian:    МАШИННАЯ СТИРКА МАКС. 30°C КОРОТКИЙ ОТЖИМ-ДЕЛИКАТНАЯ СТИРКА
            {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Indonesian: CUCI MESIN MAKS 30°C / 85ºF, PUTAR PENDEK KERING-CUCI HALUS
            {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Turkish:    MAKİNEDE KISA PROGRAMDA MAKSİMUM 30°C'DE YIKAYIN-NAZİK YIKAMA
            {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
```

### Care Instruction 2: "Do not bleach"
**Source:** `TRANSLATIONS&RULES(16).xlsx` → Sheet: **SAP-WASHING RULES**
- Lookup: Match `CODIGO SAP` = "S12"

**Raw data from JSON:**
- Path: `data[0]['StyleColor'][0]['CareInstructions'][1]`
  - `CareCode` = "S12"
  - `CareSAPCode` = "1"

**Translations from Excel:**
```
English:    DO NOT BLEACH            {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Spanish:    NO USAR LEJÍA            {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
French:     NE PAS UTILISER D'EAU DE JAVEL
                                     {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Portuguese: NÃO USAR LIXÍVIA         {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Russian:    НЕ ОТБЕЛИВАТЬ            {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Indonesian: JANGAN GUNAKAN PEMUTIH   {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Turkish:    AĞARTICI KULLANMAYIN     {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
```

### Care Instruction 3: "Iron up to 150°C"
**Source:** `TRANSLATIONS&RULES(16).xlsx` → Sheet: **SAP-WASHING RULES**
- Lookup: Match `CODIGO SAP` = "S14"

**Raw data from JSON:**
- Path: `data[0]['StyleColor'][0]['CareInstructions'][2]`
  - `CareCode` = "S14"

**Translations from Excel:**
```
English:    IRON UP TO 150°C / 300ºF {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Spanish:    PLANCHAR MÁXIMO 150°C    {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
French:     REPASSER MAX 150°C       {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Portuguese: PASSAR A FERRO MÁX. 150°C{TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Russian:    ГЛАДИТЬ ПРИ ТЕМПЕРАТУРЕ ДО 150°C
                                     {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Indonesian: SETRIKA HINGGA 150°C / 300ºF
                                     {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Turkish:    150°C / 300ºF'YE KADAR ÜTÜLEYIN
                                     {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
```

### Care Instruction 4: "Do not dry clean"
**Source:** `TRANSLATIONS&RULES(16).xlsx` → Sheet: **SAP-WASHING RULES**
- Lookup: Match `CODIGO SAP` = "S23"

**Raw data from JSON:**
- Path: `data[0]['StyleColor'][0]['CareInstructions'][3]`
  - `CareCode` = "S23"

**Translations from Excel:**
```
English:    DO NOT DRY CLEAN         {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Spanish:    NO LIMPIAR EN SECO       {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
French:     NE PAS NETTOYER À SEC    {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Portuguese: NÃO LIMPAR A SECO        {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Russian:    НЕ ПОДВЕРГАТЬ ХИМИЧЕСКОЙ ЧИСТКЕ
                                     {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Indonesian: JANGAN DRY CLEAN         {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Turkish:    KURU TEMİZLEME YAPMAYIN  {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
```

### Care Instruction 5: "Do not tumble dry"
**Source:** `TRANSLATIONS&RULES(16).xlsx` → Sheet: **SAP-WASHING RULES**
- Lookup: Match `CODIGO SAP` = "S25"

**Raw data from JSON:**
- Path: `data[0]['StyleColor'][0]['CareInstructions'][4]`
  - `CareCode` = "S25"

**Translations from Excel:**
```
English:    DO NOT DRY IN A TUMBLE DRIER
                                     {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Spanish:    NO SECAR EN SECADORA     {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
French:     NE PAS SÉCHER AU SÈCHE-LINGE
                                     {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Portuguese: NÃO SECAR NA MÁQUINA     {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Russian:    НЕ СУШИТЬ В БАРАБАННОЙ СУШИЛКЕ
                                     {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Indonesian: JANGAN KERINGKAN DI PENGERING PUTAR
                                     {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
Turkish:    ÇAMAŞIR KURUTMA MAKİNESİNDE KURUTMAYIN
                                     {TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}
```

---

## LABEL SECTION 6: REGULATORY SYMBOLS

### EAC Mark (Eurasian Conformity)
**Source:** `EAC.pdf` or `EAC.gif`
- Visual symbol file to be embedded in label

**Decision logic from:**
- `TRANSLATIONS&RULES(16).xlsx` → Sheet: **JSON-RULES**
- Lookup: Match `DESC. GEN.` = "WOMAN" + `PACKAGING` = "FOLDED"
- Result: `EAC` column = 1 (YES, required)

### Triman Symbol (French Recycling)
**Source:** `triman 1.pdf` (or `triman 2.pdf`, `triman 3.pdf`)
- Visual symbol file to be embedded in label

**Decision logic from:**
- `TRANSLATIONS&RULES(16).xlsx` → Sheet: **JSON-RULES**
- Lookup: Match `DESC. GEN.` = "WOMAN" + `PACKAGING` = "FOLDED"
- Result: `TRIMAN` column = "T-SHIRT" (YES, required)

---

## LABEL SECTION 7: PRODUCT CODE REFERENCE

### CODE 15
**Source:** `CODE 15.pdf`
- Visual reference sheet for product codes/barcodes

**Decision logic from:**
- `TRANSLATIONS&RULES(16).xlsx` → Sheet: **JSON-RULES**
- Lookup: Match `DESC. GEN.` = "WOMAN" + `PACKAGING` = "FOLDED"
- Result: `ITALIAN CODE` column = "CODE 15"

---

## LABEL SECTION 8: IMPORTER INFORMATION

### Legal Importer for Spain
**Source:** `TRANSLATIONS&RULES(16).xlsx` → Sheet: **GARMENT IMPORTERS**
- Lookup: Match `COUNTRY` = "Spain" or `COUNTRY CODE` = "ES"
- Returns: Company name, legal address, tax ID, registration number

**Raw data from JSON:**
- `4500801837-00000017-205456MK26.json`
- Path: `data[0]['StyleColor'][0]['Destination']['de_code']` = "D001"
- Path: `data[0]['StyleColor'][0]['Destination']['dc_address']` contains "ES" (Spain)

---

## LABEL SECTION 9: SUPPLIER INFORMATION

### Supplier: MARENGTEX
**Source:** `4500801837-00000017-205456MK26.json`
- Path: `data[0]['Supplier']`
  - `SupplierCode` = "0010002527"
  - `SupplierName` = "MARENGTEX"
  - `Address` = "ZONE INDUSTRIELLE ROUTE DE TETOUANT LOT. 19 BIS ALLEE 1, TANGER, Tanger-Asilah, Morocco - 90000"
  - `PhoneNumber` = "938602222-10706"
  - `MailAddress` = "Receptionmarengtex@gmail.com, marengmounir@gmail.com"

---

## LABEL SECTION 10: BRAND LOGO

### Mango Logo
**Source:** `ADHEDIST-mango.pdf`
- Visual brand logo/adhesive marking to be embedded in label

---

## COMPLETE FILE DEPENDENCY MAP

```
LABEL GENERATION FOR PRODUCT 205456MK26
│
├─ JSON DATA SOURCE
│  └─ {4500801837-00000017-205456MK26.json}
│     ├─ Style ID, Color, Season, Sizes
│     ├─ Origin country (Morocco)
│     ├─ Material codes (C005)
│     ├─ Care codes (S02, S12, S14, S23, S25)
│     ├─ Destination (Spain)
│     └─ Supplier details
│
├─ TRANSLATION & RULES ENGINE
│  └─ {TRANSLATIONS&RULES(16).xlsx}
│     │
│     ├─ Sheet: JSON-RULES
│     │  └─ Determines: CODE 15 + EAC + TRIMAN required
│     │
│     ├─ Sheet: MADE IN COUNTRY
│     │  └─ Translates "Made in Morocco" → 33 languages
│     │
│     ├─ Sheet: MATERIALS
│     │  └─ Translates "100% Cotton" (C005) → 33 languages
│     │
│     ├─ Sheet: SAP-WASHING RULES
│     │  └─ Translates 5 care instructions → 8 languages each
│     │
│     └─ Sheet: GARMENT IMPORTERS
│        └─ Provides legal importer info for Spain
│
├─ VISUAL ASSETS (SYMBOLS)
│  ├─ {EAC.pdf} or {EAC.gif}
│  │  └─ Eurasian Conformity mark
│  │
│  ├─ {triman 1.pdf} (or triman 2.pdf, triman 3.pdf)
│  │  └─ French recycling symbol
│  │
│  └─ {ADHEDIST-mango.pdf}
│     └─ Mango brand logo
│
└─ REFERENCE DOCUMENTS
   └─ {CODE 15.pdf}
      └─ Product code reference sheet
```

---

## SUMMARY: FILE USAGE BY LABEL SECTION

| Label Section | File(s) Required |
|--------------|------------------|
| Product Info (Style, Color, Season) | `4500801837-00000017-205456MK26.json` |
| Sizes | `4500801837-00000017-205456MK26.json` |
| Origin (33 languages) | `4500801837-00000017-205456MK26.json` + `{TRANSLATIONS&RULES(16).xlsx → MADE IN COUNTRY}` |
| Composition (33 languages) | `4500801837-00000017-205456MK26.json` + `{TRANSLATIONS&RULES(16).xlsx → MATERIALS}` |
| Care Instructions (8 languages × 5) | `4500801837-00000017-205456MK26.json` + `{TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}` |
| Regulatory Symbols | `{TRANSLATIONS&RULES(16).xlsx → JSON-RULES}` + `{EAC.pdf}` + `{triman 1.pdf}` |
| Product Code | `{TRANSLATIONS&RULES(16).xlsx → JSON-RULES}` + `{CODE 15.pdf}` |
| Importer Info | `{TRANSLATIONS&RULES(16).xlsx → GARMENT IMPORTERS}` |
| Supplier Info | `4500801837-00000017-205456MK26.json` |
| Brand Logo | `{ADHEDIST-mango.pdf}` |

---

## KEY INSIGHT

Every translation requires **{TRANSLATIONS&RULES(16).xlsx}** with the specific sheet name:
- Origin → `{TRANSLATIONS&RULES(16).xlsx → MADE IN COUNTRY}`
- Composition → `{TRANSLATIONS&RULES(16).xlsx → MATERIALS}`
- Care → `{TRANSLATIONS&RULES(16).xlsx → SAP-WASHING RULES}`
- Importer → `{TRANSLATIONS&RULES(16).xlsx → GARMENT IMPORTERS}`
- Rules → `{TRANSLATIONS&RULES(16).xlsx → JSON-RULES}`

Visual assets are separate PDF/image files: `{EAC.pdf}`, `{triman 1.pdf}`, `{CODE 15.pdf}`, `{ADHEDIST-mango.pdf}`
