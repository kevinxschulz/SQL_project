import sqlite3

# connecting to the database
conn = sqlite3.connect('skp_data.db')

# total margin generated by signature products over the last 2 months
margin_query = """
SELECT SUM(Marge_Nette_Magasin) AS Total_Margin
FROM transactions
WHERE (date_transaction LIKE '2022-02%' OR date_transaction LIKE '2022-03%')
AND Modele_Couleur_Ref IN (
    SELECT "CODE MODELE COULEUR ACTUEL"
    FROM product
    WHERE "SIGNATURE PRODUCT?" = 'WAHR'
)
"""

# margin-query result
margin_result = conn.execute(margin_query).fetchall()
print("Total margin generated by signature products over the last 2 months:")
for row in margin_result:
    print(row)


# Revenue split per day
revenue_query = """
SELECT date_transaction, SUM(CA_Net_TTC) AS Total_Revenue
FROM transactions
WHERE date_transaction LIKE '2022%'
GROUP BY date_transaction
"""

# revenue-query result
revenue_result = conn.execute(revenue_query).fetchall()
print("Revenue per day:")
for row in revenue_result:
    print(row)

# top 10 products in terms of units sold
unit_sales_query = """
SELECT Modele_Couleur_Ref, SUM(Quantite_Vendue) AS Total_Units_Sold
FROM transactions
GROUP BY Modele_Couleur_Ref
ORDER BY Total_Units_Sold DESC
LIMIT 10;
"""

# unit_sales-query result
unit_sales_result = conn.execute(unit_sales_query).fetchall()
print("Top 10 products in terms of sold units:")
for row in unit_sales_result:
    print(row)


# number of transactions per store
transactions_per_store_query = """
SELECT Point_de_Vente, COUNT(Numero_Transaction) AS Number_of_Transactions
FROM transactions
GROUP BY Point_de_Vente;
"""

# transactions_per_store-query result
transactions_per_store_result = conn.execute(transactions_per_store_query).fetchall()
print("The number of transactions per store:")
for row in transactions_per_store_result:
    print(row)


# close connection to db
conn.close()