# Analyse de Variants Génétiques pour les Maladies Héréditaires

## Description

Ce projet vise à analyser des variants génétiques associés à des maladies héréditaires à partir de fichiers VCF (Variant Call Format), en utilisant une architecture Big Data et des techniques de traitement de données massives.

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

## Data Information

⚠️ **The ClinVar VCF file is too large to upload here.**

You can manually download the dataset from:

👉 [ClinVar VCF Download Link](https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/clinvar.vcf.gz)




