import sqlite3
import pandas as pd

conn = sqlite3.connect("magiConsessionaria.db")

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

subsidiaryAdress_info = pd.DataFrame({
    "subsidiary_id": [1, 2, 3, 4, 5, 6, 7],
    "subsidiary_Adress": ["recife", "salvador", "rio de janeiro", "santa catarina", "florianopólis", "são luiz", "alagoas"],
})

subsidiarystock_info = pd.DataFrame({
    "subsidiaryAdress_id": [1, 2, 3, 4, 5, 6, 7],
    "stock_id": [1, 2, 3, 4, 5, 6, 7],
    "subsidiary_stockCars": [90, 99, 192, 219, 109, 132, 89]
})

client_info.to_sql("client", conn, index=False, if_exists="replace")
client_numbers.to_sql("numbers", conn, index=False, if_exists="replace")
cars_info.to_sql("cars", conn, index=False, if_exists="replace")
subsidiaryAdress_info.to_sql("subsidiary_Adress", conn, index=False, if_exists="replace")
subsidiarystock_info.to_sql("subsidiary_stock", conn, index=False, if_exists="replace")

query_inner_client_numbers = """
SELECT client.client_id, client.client_name, client.cnh, numbers.numbers
FROM client
LEFT JOIN numbers ON client.client_id = numbers.clients_id
"""

query_inner_client_cars = """
SELECT client.client_id, client.client_name, cars.brand, cars.mileage, cars.price
FROM client
INNER JOIN cars ON client.client_id = cars.clients_id
"""

query_inner_Adress_stock = """
SELECT subsidiary_Adress.subsidiary_id, subsidiary_Adress.subsidiary_Adress, subsidiary_stock.subsidiary_stockCars
FROM subsidiary_Adress
INNER JOIN subsidiary_stock ON subsidiary_Adress.subsidiary_id = subsidiary_stock.subsidiaryAdress_id
"""

query_inner_cars_price = """
SELECT cars.car_id, cars.brand, cars.price
FROM cars
"""

inner_join_df_client_cars = pd.read_sql(query_inner_client_cars, conn)
client_cars = inner_join_df_client_cars

left_join_df_client_numbers = pd.read_sql(query_inner_client_numbers, conn)
client_numbers = left_join_df_client_numbers

inner_join_df_subsidiary = pd.read_sql(query_inner_Adress_stock, conn)
subsidiary_info = inner_join_df_subsidiary

select_cars_price = pd.read_sql(query_inner_cars_price, conn)
cars_price = select_cars_price
##############

print("-----------------------------------------------------")
print("client and numbers:")
print("----------------------------------------------------")
display(client_numbers)
#print(client_numbers)

print("-----------------------------------------------------")
print("cars price:")
print("----------------------------------------------------")
display(cars_price)
#print(cars_price)

print("-----------------------------------------------------")
print("subsidiary info:")
print("----------------------------------------------------")
display(subsidiary_info)
#print(subsidiary_info)

print("-----------------------------------------------------")
print("client and cars:")
print("----------------------------------------------------")
display(client_cars)
#print(client_cars)
