# Analyse de Variants Génétiques pour les Maladies Héréditaires

## Description

Ce projet vise à analyser des variants génétiques associés à des maladies héréditaires à partir de fichiers VCF (Variant Call Format), en utilisant une architecture Big Data et des techniques de traitement de données massives.

---

## Technologies utilisées

- **Hadoop** / **Spark** : Traitement Big Data
- **MongoDB** : Base de données NoSQL pour stocker les résultats
- **Python** : Scripts de traitement, nettoyage et machine learning
- **Talend** : Processus ETL (Extraction - Transformation - Chargement)

---

## Processus du projet

1. **Conversion VCF → CSV**  
   - Script Python pour parser et convertir les fichiers `.vcf` en `.csv`.

2. **Nettoyage des données**  
   - Suppression des colonnes inutiles.
   - Traitement des valeurs manquantes.
   - Transformation des types de données.

3. **Sélection des attributs**  
   - Utilisation d'un classifieur **Random Forest** pour estimer l'importance des variables.

4. **Création d'un Cube OLAP**  
   - Structuration multidimensionnelle : par gènes, maladies, types de mutations.

5. **Interface de Visualisation**  
   - Graphiques de répartition (`seaborn.histplot`, `seaborn.countplot`).
   - Diagrammes de corrélation (`seaborn.heatmap`).
   - Tableaux dynamiques pour l'exploration des données.

---

## Arborescence du projet

```bash
.
├── data/              # Données brutes et fichiers de travail
├── scripts/           # Scripts Python pour conversion et traitement
├── results/           # Résultats du nettoyage et des analyses
├── figures/           # Graphiques générés
├── README.md          # Ce fichier
