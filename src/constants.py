"""
Constantes utilisées par le projet. Importer ce module pour utiliser dans le projet.
"""
# etapes dans le fichier config
GENERAL = "general"
EXTRACTION = "extraction"
CLEANING = "cleaning"
FEATURE = "feature_engineering"
SELECTION = "selection"
CLUSTERING = "clustering"

# les étapes valides dans le fichier log
ACCEPTED_STEPS = [EXTRACTION, CLEANING, FEATURE, SELECTION,
                  CLUSTERING]

# Valid steps for the output
ACCEPTED_OUTPUT_STEPS = [EXTRACTION, CLEANING, FEATURE,
                         CLUSTERING]







# DATA
## raw data
RAW_DATA = "data/raw"
CSV_file = "en.openfoodfacts.org.products-df5.csv"

## from url
url = 'https://static.openfoodfacts.org/data/en.openfoodfacts.org.products.csv.gz'
zip_url_file = "https://github.com/AbdelmajidLh/datasets/raw/main/en.openfoodfacts.org.products-df5.zip"
save_as = 'data/raw/raw_data.csv'


# LOGs
logfile = "log/logfile.log"


# Cleaning 
## columns to keep
KEEP_COLS = ['code', 'created_t','product_name',\
            'categories','countries','nutriscore_score',\
            'nutriscore_grade','pnns_groups_1','pnns_groups_2',
            'energy_100g','fat_100g','saturated-fat_100g',\
            'carbohydrates_100g','sugars_100g','fiber_100g',\
            'proteins_100g','salt_100g','sodium_100g']

## columns to remove nan
DROP_NA_COLS = ['nutriscore_grade','nutriscore_score','pnns_groups_1','pnns_groups_2','categories']

## column rename
NEW_COLNAMES = {"code": "code_barres",
             "created_t":"date_creation",
             "product_name": "nom_produit",
             "categories": "categories",
             "nutriscore_score": "nutriscore_score",
             "nutriscore_grade": "nutriscore_grade",
             "pnns_groups_1": "pnns_groupes_1",
             "pnns_groups_2": "pnns_groupes_2",
             "energy_100g": "energie_100g",
             "fat_100g": "matieres_grasses_100g",
             "saturated-fat_100g": "matieres_grasses_saturees_100g",
             "carbohydrates_100g": "glucides_100g",
             "sugars_100g": "glucides_sucres_100g",
             "fiber_100g": "fibres_100g",
             "proteins_100g": "proteines_100g",
             "salt_100g": "sel_100g",
             "sodium_100g": "sodium_100g"}

## cols to convert date
DATE_COLS = ['date_creation']