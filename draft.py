import sqlite3
import pandas as pd
from Functions.examples import create_example
from Functions.sql import connect_db

ct_db = sqlite3.connect('tads_2.db')

df = create_example()

df.to_sql(
    'lanchonete',
    conn,
    if_exists='replace',
    index = False
)

query = """
    SELECT product, price 
    FROM lanchonete
    WHERE price >= 6
"""

pd.read_sql(
    query,
    conn
)