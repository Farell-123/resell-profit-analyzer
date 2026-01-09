# Resell Profit Analyzer

## 🎯 À quoi ça sert ?
Cet outil aide les revendeurs (Vinted, sneakers, e-commerce, etc.)
à savoir **quels produits sont vraiment rentables** avant d’acheter.

## ⚙️ Fonctionnalités
- Calcul automatique du profit
- Calcul de la marge (%)
- Score de rentabilité :
  - 🟢 EXCELLENT
  - 🟡 CORRECT
  - 🔴 MAUVAIS
- Export des résultats en CSV

## 📂 Comment l’utiliser

1. Installer Python (version 3.10 ou plus)
2. Mettre vos produits dans : data/products.csv
3. Lancer le script python : main.py
4. Résultat généré dans : output/analysis_results.csv

## 👤 Pour qui ?
- Revendeurs débutants ou confirmés
- Dropshippers
- Micro-entrepreneurs
- Étudiants qui veulent analyser la rentabilité

## 🚀 Pourquoi l’utiliser ?
- Gain de temps
- Décisions plus intelligentes
- Outil simple et rapide

## ⚙️ Configuration

Les seuils de rentabilité sont configurables via le fichier `config.json`.

Exemple :
```json
{
  "excellent_margin": 100,
  "correct_margin": 50
}

Les seuils peuvent être modifiés sans changer le code, 
simplement en ajustant le fichier `config.json`.



