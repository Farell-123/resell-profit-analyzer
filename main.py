## Description
#This project analyzes resale profitability for sellers.

## Description (FR)
#Ce projet analyse la rentabilité de produits pour la revente.

# TODO: Export results to CSV
# TODO: Add web interface

import csv

# TODO: Export results to CSV
# TODO: Add web dashboard
# TODO: Connect to database



def analyze_products(file_path):
    results = []

    with open(file_path, newline="", encoding="utf-8") as file:
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
                elif margin >= 50:
                    status = "🟡 CORRECT"
                else:
                    status = "🔴 MAUVAIS"

                result = {
                    "name": row["name"],
                    "buy_price": buy,
                    "sell_price": sell,
                    "profit": profit,
                    "margin": round(margin, 1),
                    "status": status
                }

                results.append(result)

            except (ValueError, KeyError):
                continue

    return results


def export_to_csv(results, output_path):
    if not results:
        print("Aucun résultat à exporter.")
        return

    with open(output_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)


if __name__ == "__main__":
    results = analyze_products("data/products.csv")
    export_to_csv(results, "output/analysis_results.csv")
    print("Analyse terminée – fichier généré avec succès ✅")
