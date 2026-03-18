# REAL LABEL DATA EXAMPLE - Product 205456MK26

*Source: 4500801837-00000017-205456MK26.json*
*Date: 2026-03-18*

---

## 1. ORDER INFORMATION (from JSON)

```
Order ID:           4500801837
Season:             SS2026 (Spring/Summer 2026)
Order Quantity:     55,006 units
Type:               ZMFP - Final Product
Status:             Active
Production Date:    March 9, 2026
Version:            00000017
Timestamp:          March 11, 2026 09:44:52
IDOC:               0000001081937354
```

---

## 2. SUPPLIER INFORMATION (from JSON)

```
Supplier Code:      0010002527
Supplier Name:      MARENGTEX
Address:            ZONE INDUSTRIELLE ROUTE DE TETOUANT
                    LOT. 19 BIS ALLEE 1, TANGER
                    Tanger-Asilah, Morocco - 90000
Phone:              938602222-10706
Email:              Receptionmarengtex@gmail.com
                    marengmounir@gmail.com
```

---

## 3. PRODUCT DETAILS (from JSON)

```
Reference ID:       27977159
Style ID:           205456MK26
Color Code:         01
Color Name:         WHITE
Generic Material:   26204321MK001
Line:               WOMAN
Age:                ADULT
Gender:             FEMALE
Packaging:          FOLDED
Generic Name:       T
Generic:            VIRI
Family ID:          M1WTTT
Family:             T-shirts
Product Type Code:  208
Product Type:       T-SHIRT
Product Type (ES):  CAMISETA
RFID Mark:          NO
Iconic:             YES
```

---

## 4. DESTINATION (from JSON)

```
Distribution Center: LLIÇÀ
DC Address:          Polígono Industrial Can Moncau 6
                     Parcelas B1 y B2
                     08186 Lliçá d'Amunt ES
DE Code:             D001
```

**Destination Country:** Spain

---

## 5. ORIGIN (from JSON)

```
Country of Origin:   Morocco
```

---

## 6. MATERIAL COMPOSITION (from JSON)

```
Title:              COMPOSITION (Code: T001)
Fabric:             100% COTTON
Fabric Code:        C005
Fabric Type:        TEXTILE
```

---

## 7. CARE INSTRUCTIONS (from JSON)

```
1. Code: S02 | SAP: 2 | Group: Wash
   MACHINE WASH MAX 30°C / 85ºF, SHORT SPIN

2. Code: S12 | SAP: 1 | Group: Bleach
   DO NOT BLEACH

3. Code: S14 | SAP: 1 | Group: Iron
   IRON UP TO 150°C / 300ºF

4. Code: S23 | SAP: 6 | Group: Dry Clean
   DO NOT DRY CLEAN

5. Code: S25 | SAP: 1 | Group: Dry
   DO NOT DRY IN A TUMBLE DRIER
```

---

## 8. SIZE RANGE (from JSON)

```
SAP Sizes:    440/445/450/455/460/465/470/1310/1320/476/481
COBOL Sizes:  18/19/20/21/22/23/24/25/26/27/28
Size Names:   XXS/XS/S/M/L/XL/XXL/1XL/2XL/3XL/4XL
```

---

## 9. APPLY RULES FROM TRANSLATIONS&RULES(16).xlsx

### Step 1: Match to JSON-RULES Sheet

**Lookup Criteria:**
- DESC. GEN. = "WOMAN"
- PACKAGING = "FOLDED"
- FAMILY = "T-shirts"

**Result from JSON-RULES:**
```
Italian Code:       CODE 15
EAC:                1 (YES - Required)
TRIMAN:             T-SHIRT (YES - Required)
Korean Symbol:      (blank - NOT Required)
MCA Law:            (blank - NOT Required)
```

### Step 2: Translate "Made in Morocco" (MADE IN COUNTRY Sheet)

**Lookup:** Country = "Morocco"

**Translations:**
```
English:            MADE IN MOROCCO
Spanish:            HECHO EN MARRUECOS
French:             FABRIQUE AU MAROC
Italian:            FABBRICATO IN MAROCCO
German:             HERGESTELLT IN MAROKKO
Portuguese:         FABRICADO EM MARROCOS
Catalan:            FABRICAT AL MARROC
Dutch:              GEMAAKT IN MAROKKO
Hungarian:          KÉSZÜLT MAROKKÓBAN
Romanian:           FABRICAT ÎN MAROC
Latvian:            RAŽOTS MAROKĀ
Czech:              VYROBENO V MAROKU
Lithuanian:         PAGAMINTA MAROKE
Polish:             WYPRODUKOWANO W MAROKU
Danish:             FREMSTILLET I MAROKKO
Basque:             MAROKON EGINA
Galician:           FEITO EN MARROCOS
Russian:            СДЕЛАНО В МАРОККО
Greek:              ΚΑΤΑΣΚΕΥΑΣΜΕΝΟ ΣΤΟ ΜΑΡΟΚΟ
Slovak:             VYROBENÉ V MAROKU
Slovenian:          IZDELANO V MAROKU
Bulgarian:          ПРОИЗВЕДЕНО В МАРОКО
Indonesian:         DIBUAT DI MAROKO
Turkish:            FABRİKA MAROC
Finnish:            VALMISTETTU MAROKOSSA
Swedish:            TILLVERKAD I MAROCKO
Chinese:            摩洛哥制造
Taiwanese:          摩洛哥製造
Korean:             모로코 제조
Japanese:           モロッコ製
Arabic:             صنع في المغرب
```

### Step 3: Translate Material (MATERIALS Sheet)

**Lookup:** Code = "C005"

**Translations:**
```
English:            100% COTTON
Spanish:            100% ALGODÓN
French:             100% COTON
Italian:            100% COTONE
German:             100% BAUMWOLLE
Portuguese:         100% ALGODÃO
Catalan:            100% COTÓ
Dutch:              100% KATOEN
Hungarian:          100% PAMUT
Romanian:           100% BUMBAC
Latvian:            100% KOKVILNA
Czech:              100% BAVLNA
Lithuanian:         100% MEDVILNĖ
Polish:             100% BAWEŁNA
Danish:             100% BOMULD
Basque:             %100 KOTOIA
Galician:           100% ALGODÓN
Russian:            100% ХЛОПОК
Greek:              100% ΒΑΜΒΑΚΙ
Slovak:             100% BAVLNA
Slovenian:          100% BOMBAŽ
Bulgarian:          100% ПАМУК
Indonesian:         100% KAPAS
Turkish:            %100 PAMUK
Finnish:            100% PUUVILLA
Swedish:            100% BOMULL
Chinese:            100% 棉
Taiwanese:          100% 棉
Korean:             면 100%
Japanese:           綿100%
Arabic:             ١٠٠٪ قطن
```

### Step 4: Translate Care Instructions (SAP-WASHING RULES Sheet)

**Care Code S02 (SAP: 2):**
```
English:            MACHINE WASH MAX 30°C / 85ºF, SHORT SPIN DRY-DELICATE WASH
Spanish:            LAVAR A MAQUINA MÁX. 30°C CENTRIFUGADO CORTO-LAVADO DELICADO
French:             LAVAGE EN MACHINE MAX 30°C ESSORAGE COURT - LAVAGE DÉLICAT
Portuguese:         LAVAR À MÁQUINA MÁX. 30°C CENTRIFUGAÇÃO CURTA-LAVAGEM DELICADA
Russian:            МАШИННАЯ СТИРКА МАКС. 30°C КОРОТКИЙ ОТЖИМ-ДЕЛИКАТНАЯ СТИРКА
Indonesian:         CUCI MESIN MAKS 30°C / 85ºF, PUTAR PENDEK KERING-CUCI HALUS
Turkish:            MAKİNEDE KISA PROGRAMDA MAKSİMUM 30°C'DE YIKAYIN-NAZİK YIKAMA
```

**Care Code S12 (SAP: 1):**
```
English:            DO NOT BLEACH
Spanish:            NO USAR LEJÍA
French:             NE PAS UTILISER D'EAU DE JAVEL
Portuguese:         NÃO USAR LIXÍVIA
Russian:            НЕ ОТБЕЛИВАТЬ
Indonesian:         JANGAN GUNAKAN PEMUTIH
Turkish:            AĞARTICI KULLANMAYIN
```

**Care Code S14 (SAP: 1):**
```
English:            IRON UP TO 150°C / 300ºF
Spanish:            PLANCHAR MÁXIMO 150°C
French:             REPASSER MAX 150°C
Portuguese:         PASSAR A FERRO MÁX. 150°C
Russian:            ГЛАДИТЬ ПРИ ТЕМПЕРАТУРЕ ДО 150°C
Indonesian:         SETRIKA HINGGA 150°C / 300ºF
Turkish:            150°C / 300ºF'YE KADAR ÜTÜLEYIN
```

**Care Code S23 (SAP: 6):**
```
English:            DO NOT DRY CLEAN
Spanish:            NO LIMPIAR EN SECO
French:             NE PAS NETTOYER À SEC
Portuguese:         NÃO LIMPAR A SECO
Russian:            НЕ ПОДВЕРГАТЬ ХИМИЧЕСКОЙ ЧИСТКЕ
Indonesian:         JANGAN DRY CLEAN
Turkish:            KURU TEMİZLEME YAPMAYIN
```

**Care Code S25 (SAP: 1):**
```
English:            DO NOT DRY IN A TUMBLE DRIER
Spanish:            NO SECAR EN SECADORA
French:             NE PAS SÉCHER AU SÈCHE-LINGE
Portuguese:         NÃO SECAR NA MÁQUINA
Russian:            НЕ СУШИТЬ В БАРАБАННОЙ СУШИЛКЕ
Indonesian:         JANGAN KERINGKAN DI PENGERING PUTAR
Turkish:            ÇAMAŞIR KURUTMA MAKİNESİNDE KURUTMAYIN
```

### Step 5: Get Importer Information (GARMENT IMPORTERS Sheet)

**Lookup:** Destination = Spain (ES)

**Expected Result:**
```
Importer Name:      MANGO MNG KFIT.
Address:            [Legal registered address in Spain]
Tax ID:             [Spanish CIF/NIF number]
Registration:       [EU registration number]
```

---

## 10. REQUIRED DOCUMENTS FOR THIS LABEL

### ✅ MUST HAVE:

1. **CODE 15.pdf**
   - Product code reference sheet
   - Determined by JSON-RULES match

2. **EAC.pdf** or **EAC.gif**
   - Eurasian Conformity mark
   - Required because EAC = 1 in JSON-RULES

3. **triman 1.pdf** (or triman 2.pdf, triman 3.pdf)
   - French recycling symbol
   - Required because TRIMAN = "T-SHIRT" in JSON-RULES

4. **ADHEDIST-mango.pdf**
   - Mango brand logo/adhesive marking

5. **TRANSLATIONS&RULES(16).xlsx**
   - Sheets used:
     - JSON-RULES (determine requirements)
     - MADE IN COUNTRY (33 language translations)
     - MATERIALS (33 language translations)
     - SAP-WASHING RULES (8 language translations)
     - GARMENT IMPORTERS (legal info for Spain)

### ❌ NOT NEEDED:

- **KOREAN SYMBOL.png** - Not required (blank in JSON-RULES)
- **CODE 1-14, 16.pdf** - Only CODE 15 is needed
- **numeros_equivalente_arabe_valores.xlsx** - Destination is Spain, not Arabic market
- **ÉLÉMENTS.pdf** - May not be required for this product
- **GI000DPO-SAP_1.pdf** - SAP reference, not for label
- **GI001BAW-GI001BAC.pdf** - Not matched
- **PVPV0102-PVP002XG.pdf** - Price codes, not for label

---

## 11. COMPLETE LABEL LAYOUT WITH REAL DATA

```
┌─────────────────────────────────────────────────────────────────┐
│  [MANGO LOGO - from ADHEDIST-mango.pdf]                         │
├─────────────────────────────────────────────────────────────────┤
│  Style: 205456MK26                                              │
│  Color: 01 - WHITE                                              │
│  Season: SS2026                                                 │
│  [BARCODE - reference from CODE 15.pdf]                         │
├─────────────────────────────────────────────────────────────────┤
│  REGULATORY SYMBOLS:                                            │
│  [EAC.pdf symbol]  [triman 1.pdf symbol]                       │
├─────────────────────────────────────────────────────────────────┤
│  MADE IN MOROCCO                                                │
│  HECHO EN MARRUECOS                                             │
│  FABRIQUE AU MAROC                                              │
│  FABBRICATO IN MAROCCO                                          │
│  HERGESTELLT IN MAROKKO                                         │
│  FABRICADO EM MARROCOS                                          │
│  摩洛哥制造                                                        │
│  (from MADE IN COUNTRY sheet)                                   │
├─────────────────────────────────────────────────────────────────┤
│  COMPOSITION                                                    │
│  100% COTTON                                                    │
│  100% ALGODÓN                                                   │
│  100% COTON                                                     │
│  100% COTONE                                                    │
│  100% BAUMWOLLE                                                 │
│  100% ALGODÃO                                                   │
│  100% 棉                                                         │
│  (from MATERIALS sheet - Code C005)                             │
├─────────────────────────────────────────────────────────────────┤
│  CARE INSTRUCTIONS:                                             │
│  • MACHINE WASH MAX 30°C, SHORT SPIN                           │
│  • DO NOT BLEACH                                                │
│  • IRON UP TO 150°C                                             │
│  • DO NOT DRY CLEAN                                             │
│  • DO NOT DRY IN A TUMBLE DRIER                                 │
│                                                                 │
│  • LAVAR A MAQUINA MÁX. 30°C CENTRIFUGADO CORTO                │
│  • NO USAR LEJÍA                                                │
│  • PLANCHAR MÁXIMO 150°C                                        │
│  • NO LIMPIAR EN SECO                                           │
│  • NO SECAR EN SECADORA                                         │
│                                                                 │
│  • LAVAGE EN MACHINE MAX 30°C ESSORAGE COURT                   │
│  • NE PAS UTILISER D'EAU DE JAVEL                              │
│  • REPASSER MAX 150°C                                           │
│  • NE PAS NETTOYER À SEC                                        │
│  • NE PAS SÉCHER AU SÈCHE-LINGE                                │
│  (from SAP-WASHING RULES sheet - Codes S02, S12, S14, S23, S25)│
├─────────────────────────────────────────────────────────────────┤
│  SIZES: XXS/XS/S/M/L/XL/XXL/1XL/2XL/3XL/4XL                    │
├─────────────────────────────────────────────────────────────────┤
│  IMPORTER:                                                      │
│  MANGO MNG KFIT.                                                │
│  [Legal address in Spain]                                       │
│  [Tax ID / Registration number]                                 │
│  (from GARMENT IMPORTERS sheet - Spain)                         │
├─────────────────────────────────────────────────────────────────┤
│  SUPPLIER: MARENGTEX                                            │
│  Order: 4500801837 | Qty: 55,006 units                         │
└─────────────────────────────────────────────────────────────────┘
```

---

## 12. DATA FLOW SUMMARY

```
JSON FILE (4500801837-00000017-205456MK26.json)
    ↓
    ├─→ Product Attributes (WOMAN, FOLDED, T-shirt)
    │       ↓
    │   JSON-RULES Sheet
    │       ↓
    │   Determines: CODE 15 + EAC + TRIMAN
    │
    ├─→ Origin (Morocco)
    │       ↓
    │   MADE IN COUNTRY Sheet
    │       ↓
    │   33 language translations
    │
    ├─→ Material (C005 - Cotton 100%)
    │       ↓
    │   MATERIALS Sheet
    │       ↓
    │   33 language translations
    │
    ├─→ Care Codes (S02, S12, S14, S23, S25)
    │       ↓
    │   SAP-WASHING RULES Sheet
    │       ↓
    │   8 language translations
    │
    └─→ Destination (Spain)
            ↓
        GARMENT IMPORTERS Sheet
            ↓
        Legal importer information

FINAL OUTPUT: Multi-language compliant label with regulatory symbols
```

---

## KEY INSIGHTS

1. **JSON-RULES is the master controller** - It determines which CODE PDF and which regulatory symbols are mandatory based on product attributes.

2. **33 languages for origin and materials** - The system supports comprehensive international labeling.

3. **8 languages for care instructions** - Washing rules have fewer language options but cover major markets.

4. **Regulatory compliance is automatic** - The system ensures EAC and Triman symbols are included based on product type.

5. **Real production data** - This is an actual order for 55,006 white women's t-shirts manufactured in Morocco for Spring/Summer 2026 season.
