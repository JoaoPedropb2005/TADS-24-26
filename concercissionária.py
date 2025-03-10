import sqlite3
import pandas as pd

conn = sqlite3.connect("database.db")

client_info = pd.DataFrame({
    "client_id": [1, 2, 3, 4, 5, 6, 7],
    "client_name": ["ronaldo", "david", "fernanda", "glauco", "joão", "marta", "jair"],
    "cnh": ["12345678900", "98765432101", "11223344556", "99887766554", "22334455667", "66554433221", "33445566788"]
})

#print(client_info)

cars_info = pd.DataFrame({
    "clients_id": [1, 2, 3, 4, 5, 6, 7],
    "car_id": [1, 2, 3, 4, 5, 6, 7],
    "brand": ["toyota corolla", "chevrolet camaro", "ford mustang", "BMW X5", "Volkswagem golf", "Fiat argo", "renault kwid"],
    "mileage": [90000, 12000, 40000, 129000, 47820, 124009, 0],
    "price": [120.000, 85.000, 95.000, 135.000, 65.000, 45.000, 30.000]
})

enterprise_info = pd.DataFrame({
    "enterprise_id": [1],
    "enterprise_name": ["magiConsessionaria"]
})

client_info.to_sql("client", conn, index=False, if_exists="replace")
cars_info.to_sql("cars", conn, index=False, if_exists="replace")
enterprise_info.to_sql("enterprise", conn, index=False, if_exists="replace")

query_inner = """
SELECT client.client_id, client.client_name, client.cnh, cars.brand, cars.mileage, cars.price
FROM client
INNER JOIN cars ON client.client_id = cars.clients_id
"""

inner_join_df = pd.read_sql(query_inner, conn)
print("INNER JOIN:")
print(inner_join_df)