#Ce script analyse la rentabilité de produits à partir d’un fichier CSV
import csv

with open("data/products.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        #print(row)
        achat=float(row["prix_achat"])
        vente=float(row["prix_vente"])
        benef=vente-achat
        marge=(benef/achat)*100
        if benef >= 10:
                status = "🟢 EXCELLENT"
        if benef >= 5 and benef<10:
                status = "🟡 CORRECT"
        if benef<5:
                status = "🔴 MAUVAIS"
        print(f"{row['nom']} | Profit: {benef}€ | Marge: {marge:.1f}% | {status}")