import sqlite3
import pandas as pd

# Criar conexão SQLite em memória
conn = sqlite3.connect(":memory:")

# Criando DataFrames
customers_df = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"]
})

orders_df = pd.DataFrame({
    "id": [1, 2, 3],
    "customer_id": [1, 2, 1],
    "product": ["Laptop", "Mouse", "Keyboard"]
})

# Salvando os DataFrames no banco SQLite
customers_df.to_sql("customers", conn, index=False, if_exists="replace")
orders_df.to_sql("orders", conn, index=False, if_exists="replace")

# Executar INNER JOIN
query_inner = """
SELECT customers.id, customers.name, orders.product
FROM customers
INNER JOIN orders ON customers.id = orders.customer_id
"""
inner_join_df = pd.read_sql(query_inner, conn)
print("INNER JOIN:")
print(inner_join_df)

# Executar LEFT JOIN
query_left = """
SELECT customers.id, customers.name, orders.product
FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id
"""
left_join_df = pd.read_sql(query_left, conn)
print("\nLEFT JOIN:")
print(left_join_df)

# Fechar conexão
conn.close()

#############################################

import sqlite3
import pandas as pd

# Criar conexão SQLite em memória
conn = sqlite3.connect(":memory:")

# Criando DataFrame de estudantes com "student_id"
students_df = pd.DataFrame({
    "student_id": [1, 2, 3],  
    "name": ["Carlos", "Mariana", "João"]
})

# Criando DataFrame de cursos com "course_id" e "student_id"
courses_df = pd.DataFrame({
    "course_id": [101, 102, 103],  # ID do curso
    "student_id": [1, 2, 1],  # ID do aluno
    "course_name": ["Matemática", "História", "Física"]
})

# Salvando os DataFrames no banco SQLite
students_df.to_sql("students", conn, index=False, if_exists="replace")
courses_df.to_sql("courses", conn, index=False, if_exists="replace")

# Executar INNER JOIN
query_inner = """
SELECT students.student_id, students.name, courses.course_name
FROM students
INNER JOIN courses ON students.student_id = courses.student_id
"""
inner_join_df = pd.read_sql(query_inner, conn)
print("INNER JOIN:")
print(inner_join_df)

# Executar LEFT JOIN
query_left = """
SELECT students.student_id, students.name, courses.course_name
FROM students
LEFT JOIN courses ON students.student_id = courses.student_id
"""
left_join_df = pd.read_sql(query_left, conn)
print("\nLEFT JOIN:")
print(left_join_df)

# Fechar conexão
conn.close()