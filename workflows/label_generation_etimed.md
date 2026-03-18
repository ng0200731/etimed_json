# Label Generation Workflow - eTimed System

*Last updated: 2026-03-18*

## Objective

Process JSON label order data and generate compliant product labels for international fashion/textile markets by applying translation rules, regulatory requirements, and visual assets based on destination country.

## Input Requirements

1. **JSON Order File** (e.g., `4500801837-00000017-205456MK26.json`)
   - Contains: Order details, supplier info, style/color data, sizes, materials, care instructions
   - Structure: Array with LabelOrder, Supplier, StyleColor, PrepackData sections

2. **Reference Files Directory** containing:
   - `TRANSLATIONS&RULES(16).xlsx` - Master rules file
   - Regulatory symbol PDFs (EAC, Triman, Korean Symbol)
   - Product code PDFs (CODE 1-16)
   - Additional reference files

## Key Data Mappings

### From JSON Extract:
- `Line` (e.g., "WOMAN", "MAN", "KIDS")
- `Age` (e.g., "ADULT", "KIDS")
- `Gender` (e.g., "FEMALE", "MALE")
- `Packaging` (e.g., "FOLDED", "HANGER")
- `FAMILYID` / `FAMILY` (e.g., "M1WTTT", "T-shirts")
- `ProductType` / `ProductTypeCode`
- `Destination.countryorigin` (destination country)
- `Origin.countryorigin` (manufacturing country)
- `Composition` (material breakdown with percentages)
- `CareInstructions` (washing/care symbols)

### From Excel Rules Apply:

**Sheet: JSON-RULES** (3,110 rules)
- Match on: `DESC. GEN.` (Line/Age), `FAM_CODE`, `PACKAGING`
- Get: `ITALIAN CODE`, `EAC` flag, `TRIMAN` flag, `KOREAN SYMBOL` flag, `MCA LAW` flag

**Sheet: MADE IN COUNTRY**
- Match on: Country code
- Get: Translations in 33 languages (English, Spanish, French, German, Italian, Chinese, Korean, Arabic, etc.)

**Sheet: MATERIALS**
- Match on: Material codes from Composition
- Get: Translated material names per language

**Sheet: WASHING RULES / SAP-WASHING RULES**
- Match on: Care instruction codes
- Get: Translated care instructions per language

**Sheet: GARMENT IMPORTERS / FOOTWEAR IMPORTERS**
- Match on: Destination country
- Get: Legal importer information for label

## Processing Steps

### 1. Parse JSON Order Data
```python
import json
with open('order_file.json', 'r', encoding='utf-8') as f:
    order_data = json.load(f)
```

Extract key fields:
- Order ID, Season, Quantity
- Supplier details
- For each StyleColor: all product attributes
- Size breakdown
- Material composition
- Care instructions

### 2. Load Reference Rules
```python
import pandas as pd
rules = pd.ExcelFile('TRANSLATIONS&RULES(16).xlsx')
json_rules = pd.read_excel(rules, sheet_name='JSON-RULES')
country_trans = pd.read_excel(rules, sheet_name='MADE IN COUNTRY')
materials = pd.read_excel(rules, sheet_name='MATERIALS')
washing = pd.read_excel(rules, sheet_name='SAP-WASHING RULES')
importers = pd.read_excel(rules, sheet_name='GARMENT IMPORTERS')
```

### 3. Apply Business Rules

For each product in the order:

**A. Determine Required Regulatory Symbols**
```python
# Match product attributes to JSON-RULES
rule = json_rules[
    (json_rules['DESC. GEN.'] == product_line) &
    (json_rules['FAM_CODE'] == family_code) &
    (json_rules['PACKAGING'] == packaging_type)
].iloc[0]

# Check which symbols are required
needs_eac = (rule['EAC'] == 1)
needs_triman = (rule['TRIMAN'] == 'T-SHIRT')  # or other condition
needs_korean = (rule['KOREAN SYMBOL'] == 'YES')
needs_mca = (rule['MCA LAW'] == 'YES')
```

**B. Get Product Code Reference**
```python
# Determine which CODE PDF to use
if destination_country == 'Pakistan':
    code_file = rule['ITALIAN CODE CO PAKISTAN']
else:
    code_file = rule['ITALIAN CODE']
# e.g., "CODE 16" -> use CODE 16.pdf
```

**C. Translate Country of Origin**
```python
# Get "Made in [Country]" in all required languages
origin_translations = country_trans[
    country_trans['CODE SAP'] == origin_country_code
]
# Returns: "Made in Morocco", "Hecho en Marruecos", "Fabriqué au Maroc", etc.
```

**D. Translate Material Composition**
```python
# For each material in composition (e.g., "100% Cotton")
for material in product_composition:
    material_trans = materials[
        materials['CODE'] == material['code']
    ]
    # Get translated material name in target languages
```

**E. Translate Care Instructions**
```python
# For each care symbol code
for care_code in product_care_instructions:
    care_trans = washing[
        washing['CODE'] == care_code
    ]
    # Get care instruction text in target languages
```

**F. Get Legal Importer Information**
```python
# Based on destination country
importer_info = importers[
    importers['COUNTRY'] == destination_country
]
# Returns: Company name, address, registration numbers
```

### 4. Assemble Label Data Structure

Create a complete label data object:
```python
label_data = {
    'order_id': order_id,
    'style_id': style_id,
    'color': color,
    'sizes': size_breakdown,
    'barcode': barcode,
    'origin_text': {
        'en': 'Made in Morocco',
        'es': 'Hecho en Marruecos',
        'fr': 'Fabriqué au Maroc',
        # ... all languages
    },
    'composition': {
        'en': '100% Cotton',
        'es': '100% Algodón',
        # ... all languages
    },
    'care_instructions': {
        'en': ['Machine wash cold', 'Do not bleach', ...],
        'es': ['Lavar a máquina en frío', 'No usar lejía', ...],
        # ... all languages
    },
    'importer': {
        'name': 'Mango MNG Kft.',
        'address': '...',
        'registration': '...'
    },
    'regulatory_symbols': {
        'eac': needs_eac,
        'triman': needs_triman,
        'korean': needs_korean,
        'mca': needs_mca
    },
    'product_code_ref': 'CODE 16'
}
```

### 5. Generate Label Output

**Option A: Generate PDF Label**
- Use label template
- Insert translated text fields
- Place regulatory symbol images (EAC.pdf, triman.pdf, KOREAN SYMBOL.png)
- Add barcode
- Include product code reference

**Option B: Export to Database**
- Store label data in SQLite for batch processing
- Schema: orders, products, labels, translations

**Option C: Export to Print System**
- Format as XML/JSON for label printer system
- Include all text and image references

## Edge Cases & Validation

### Missing Rules
- If no matching rule in JSON-RULES: Log warning, use default/fallback
- If country not in MADE IN COUNTRY: Use English only

### Multiple Destinations
- Some orders may have multiple destination countries
- Generate separate label variants for each destination
- Apply country-specific rules independently

### Material Code Not Found
- If material code missing from MATERIALS sheet: Use raw code as fallback
- Log for manual review

### Special Characters
- Handle Unicode properly (Arabic, Chinese, Korean, Greek, etc.)
- Use UTF-8 encoding throughout
- Test rendering in label generation system

### Packaging Variations
- HANGER vs FOLDED may require different label sizes/layouts
- Different CODE PDFs may apply

## Output

1. **Label Data Files** (JSON/XML per order)
2. **Print-Ready PDFs** (if generating labels directly)
3. **Validation Report** (missing translations, unmatched rules)
4. **Processing Log** (orders processed, errors encountered)

## Tools Required

- `tools/parse_label_json.py` - Parse JSON order files
- `tools/apply_label_rules.py` - Apply Excel rules to order data
- `tools/translate_label_fields.py` - Get translations for all fields
- `tools/generate_label_pdf.py` - Create print-ready label (if needed)
- `tools/validate_label_data.py` - Check completeness and compliance

## Success Criteria

- All required fields translated to target languages
- Correct regulatory symbols identified per destination
- Legal importer information included
- Material composition accurately translated
- Care instructions properly mapped
- No missing or invalid data in output

## Notes

- The system handles 33 languages across multiple markets
- Regulatory compliance is critical - missing symbols can block customs
- Product codes (CODE 1-16) are visual reference sheets, not data
- Excel file has 3,110+ rules covering product family/packaging combinations
- Always validate against latest TRANSLATIONS&RULES file version
