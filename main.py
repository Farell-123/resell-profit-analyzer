## Description
#This project analyzes resale profitability for sellers.

## Description (FR)
#Ce projet analyse la rentabilité de produits pour la revente.

import csv

with open("data/products.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        #print(row)
        buy=float(row["buy_price"])
        sell=float(row["sell_price"])
        profit=sell-buy
        margin=(profit/buy)*100
        if margin >= 100:
                status = "🟢 EXCELLENT"
        elif margin >= 50 and margin<100:
                status = "🟡 CORRECT"
        else:
             status = "🔴 MAUVAIS"
        print(f"{row['name']} | Profit: {profit}€ | Marge: {margin:.1f}% | {status}")



