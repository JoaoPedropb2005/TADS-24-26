import sqlite3
import pandas as pd

conn = sqlite3.connect("database.db")

client_info = pd.DataFrame({
    "client_id": [1, 2, 3, 4, 5, 6, 7],
    "client_name": ["ronaldo", "david", "fernanda", "glauco", "joão", "marta", "jair"],
    "cnh": ["12345678900", "98765432101", "11223344556", "99887766554", "22334455667", "66554433221", "33445566788"]
})

client_numbers = pd.DataFrame({
    "clients_id": [1, 2, 2, 4, 6, 6, 7],
    "numbers": ["(11) 98765-4321", "(21) 99876-5432", "(31) 92345-6789", "(41) 93456-7890", "(51) 91234-5678", "(61) 94567-8901", "(71) 98765-1234"]
})

cars_info = pd.DataFrame({
    "clients_id": [1, 2, 3, 4, 5, 6, 7],
    "car_id": [1, 2, 3, 4, 5, 6, 7],
    "brand": ["toyota corolla", "chevrolet camaro", "ford mustang", "BMW X5", "Volkswagem golf", "Fiat argo", "renault kwid"],
    "mileage": [90000, 12000, 40000, 129000, 47820, 124009, 0],
    "price": [119.999, 84.999, 94.999, 134.999, 64.999, 44.999, 29.000]
})

# enterprise_info = pd.DataFrame({
#     "enterprise_id": [1],
#     "enterprise_name": ["magiConsessionaria"]
# })

client_info.to_sql("client", conn, index=False, if_exists="replace")
client_numbers.to_sql("numbers", conn, index=False, if_exists="replace")
cars_info.to_sql("cars", conn, index=False, if_exists="replace")
# enterprise_info.to_sql("enterprise", conn, index=False, if_exists="replace")

query_inner_client_numbers = """
SELECT client.client_id, client.client_name, client.cnh, numbers.numbers
FROM client
LEFT JOIN numbers ON client.client_id = numbers.clients_id
"""

query_inner_client_cars = """
SELECT client.client_id, client.client_name, client.cnh, cars.brand, cars.mileage, cars.price
FROM client
INNER JOIN cars ON client.client_id = cars.clients_id
"""

inner_join_df_client_cars = pd.read_sql(query_inner_client_cars, conn)
client_cars = inner_join_df_client_cars
print("-----------------------------------------------------")
print("client and cars:")
print("----------------------------------------------------")
print(client_cars)

inner_join_df_client_numbers = pd.read_sql(query_inner_client_numbers, conn)
client_numbers = inner_join_df_client_numbers
print("-----------------------------------------------------")
print("client and numbers:")
print("----------------------------------------------------")
print(client_numbers)


###############