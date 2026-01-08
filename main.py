## Description
#This project analyzes resale profitability for sellers.

## Description (FR)
#Ce projet analyse la rentabilité de produits pour la revente.

# TODO: Export results to CSV
# TODO: Add web interface and dashboard
# TODO: Connect to database
import csv
import os

# Constants
INPUT_FILE = "data/products.csv"
OUTPUT_DIR = "output"
OUTPUT_FILE = "analysis_results.csv"


def analyze_products(input_path):
    results = []

    profit_total = 0
    margin_total = 0

    total_excellent = 0
    total_correct = 0
    total_bad = 0

    with open(input_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                buy = float(row["buy_price"])
                sell = float(row["sell_price"])

                if buy <= 0 or sell <= 0:
                    continue

                profit = sell - buy
                margin = (profit / buy) * 100

                if margin >= 100:
                    status = "🟢 EXCELLENT"
                    total_excellent += 1
                elif margin >= 50:
                    status = "🟡 CORRECT"
                    total_correct += 1
                else:
                    status = "🔴 MAUVAIS"
                    total_bad += 1

                profit_total += profit
                margin_total += margin

                results.append({
                    "name": row["name"],
                    "buy_price": buy,
                    "sell_price": sell,
                    "profit": round(profit, 2),
                    "margin": round(margin, 2),
                    "status": status
                })

            except (ValueError, KeyError):
                continue

    # Summary
    if len(results) > 0:
        margin_average = round(margin_total / len(results), 2)
    else:
        margin_average = 0

    print("\n📊 RÉSUMÉ")
    print(f"Produits analysés : {len(results)}")
    print(f"Profit total : {round(profit_total, 2)} €")
    print(f"Marge moyenne : {margin_average} %")
    print(f"🟢 EXCELLENT : {total_excellent}")
    print(f"🟡 CORRECT : {total_correct}")
    print(f"🔴 MAUVAIS : {total_bad}")

    return results


def export_to_csv(results, output_path):
    with open(output_path, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "name",
            "buy_price",
            "sell_price",
            "profit",
            "margin",
            "status"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    results = analyze_products(INPUT_FILE)
    export_to_csv(results, os.path.join(OUTPUT_DIR, OUTPUT_FILE))

    print("\n✅ Analyse terminée — fichier généré avec succès")


if __name__ == "__main__":
    main()