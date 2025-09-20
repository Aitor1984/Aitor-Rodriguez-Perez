from sqlalchemy import create_engine
import pandas as pd

# Parámetros de conexión
usuario = 'postgres'
contraseña = 'Backagain'
host = 'localhost'
puerto = '5432'
base_datos = 'Northwind'

# Crear el motor de conexión
engine = create_engine(f'postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{base_datos}')

query_tablas = """
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;
"""

tablas = pd.read_sql(query_tablas, engine)
print("Tablas en la base de datos Northwind:")
print(tablas)

query_relaciones = """
SELECT
    tc.table_name AS tabla_origen,
    kcu.column_name AS columna_origen,
    ccu.table_name AS tabla_destino,
    ccu.column_name AS columna_destino
FROM
    information_schema.table_constraints AS tc
    JOIN information_schema.key_column_usage AS kcu
      ON tc.constraint_name = kcu.constraint_name
    JOIN information_schema.constraint_column_usage AS ccu
      ON ccu.constraint_name = tc.constraint_name
WHERE
    constraint_type = 'FOREIGN KEY';
"""

relaciones = pd.read_sql(query_relaciones, engine)
print("Relaciones entre tablas:")
print(relaciones)

df_orders = pd.read_sql("SELECT * FROM orders LIMIT 10;", engine)
print(df_orders)
