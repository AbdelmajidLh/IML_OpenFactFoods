# IML_OpenFactFoods - idée
Ce projet a été réalisé dans le cadre de la formation ingénieur en machine learning (OpenClassrooms).<br>
## Contexte
L'[Agence Santé Publique](lien) France lance un appel à projets pour recueillir des idées innovantes en lien avec l'alimentation. Les candidats sont invités à se baser sur les données collectées par l'initiative [Open Food Facts](lien) pour soumettre leurs projets. <br>

## Besoin
> L'objectif de ce projet est de faire une analyse exploratoire approfondie des données fournies.<br>

## Installtion et execution
### Prérequis
Pour executer ces scripts python correctement, il est necessaire d'avoir ces elements sur votre machine / ou serveur : <br>
* Python 3.9 et +
* librairies du fichier ``requirements.txt`` : un fichier `setup.py` est fourni pour vous aider à installer les bibliothèques. <br>

### Executer le code
#### Windows
"""
python src/workflow.py
"""







# ML_NutriScore - Classification des produits alimentaires sur la base de leur qualité nutritionnelle
Ce projet vise à améliorer la santé publique des populations via le choix des aliments. L'idée du projet consiste à développer un algorithme qui va aider le consommateur à choisir ses aliments sur la base du NutriScore; un score des aliments calculé à partir des informations produit.


## Source des données - OpenFoodFacts (https://world.openfoodfacts.org/data)
La base de données Open Food Facts est disponible sous licence Open Database Licence (Odbl). <br>
Les données sont compressées et au format csv (GZIP format). Il s'agit de données structurées et opensource (données publiques). <br>
Le lien pour télécharger les données (Un module python permetra de telecharger les données automatiquement): <br>
https://static.openfoodfacts.org/data/en.openfoodfacts.org.products.csv.gz