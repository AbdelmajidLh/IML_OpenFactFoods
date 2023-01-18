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
url2 = 'https://github.com/AbdelmajidLh/datasets/blob/main/en.openfoodfacts.org.products-df5.csv.gz'
zip_url_file = "https://github.com/AbdelmajidLh/datasets/raw/main/en.openfoodfacts.org.products-df5.zip"
save_as = 'data/raw/raw_data.csv'


# LOGs
logfile = "log/logfile.log"