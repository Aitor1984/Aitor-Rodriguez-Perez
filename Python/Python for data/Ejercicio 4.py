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

# ¿Cuándo fue la última vez que se pidió un producto de cada categoría?
query_ultima_vez_categoria = """
SELECT c.category_name, MAX(o.order_date) AS ultima_fecha_pedido
FROM order_details od
JOIN products p ON od.product_id = p.product_id
JOIN categories c ON p.category_id = c.category_id
JOIN orders o ON od.order_id = o.order_id
GROUP BY c.category_name;
"""
df_ultima_vez_categoria = pd.read_sql(query_ultima_vez_categoria, engine)
print(df_ultima_vez_categoria)

# ¿Existe algún producto que nunca se haya vendido por su precio original?
query_no_precio_original = """
SELECT p.product_id, p.product_name
FROM products p
WHERE NOT EXISTS (
    SELECT 1
    FROM order_details od
    WHERE od.product_id = p.product_id AND od.unit_price = p.unit_price
);
"""
df_no_precio_original = pd.read_sql(query_no_precio_original, engine)
print(df_no_precio_original)

# Productos con categoría "Confections": ID del producto, nombre y ID de categoría
query_confections = """
SELECT p.product_id, p.product_name, p.category_id
FROM products p
JOIN categories c ON p.category_id = c.category_id
WHERE c.category_name = 'Confections';
"""
df_confections = pd.read_sql(query_confections, engine)
print(df_confections)

# ¿Existe algún proveedor del que se pueda prescindir porque todos sus productos están descontinuados?
query_proveedores_descontinuados = """
SELECT s.supplier_id, s.company_name
FROM suppliers s
WHERE NOT EXISTS (
    SELECT 1
    FROM products p
    WHERE p.supplier_id = s.supplier_id AND p.discontinued = 0
);
"""
df_proveedores_descontinuados = pd.read_sql(query_proveedores_descontinuados, engine)
print(df_proveedores_descontinuados)

# Extraer los clientes que compraron más de 30 artículos "Chai" en un único pedido
query_chai_30 = """
SELECT o.customer_id, o.order_id, SUM(od.quantity) AS total_chai
FROM order_details od
JOIN products p ON od.product_id = p.product_id
JOIN orders o ON od.order_id = o.order_id
WHERE p.product_name = 'Chai'
GROUP BY o.customer_id, o.order_id
HAVING SUM(od.quantity) > 30;
"""
df_chai_30 = pd.read_sql(query_chai_30, engine)
print(df_chai_30)

# Clientes cuya suma total de carga en los pedidos sea mayor de 1000
query_carga_mayor_1000 = """
SELECT customer_id, SUM(freight) AS total_carga
FROM orders
GROUP BY customer_id
HAVING SUM(freight) > 1000;
"""
df_carga_mayor_1000 = pd.read_sql(query_carga_mayor_1000, engine)
print(df_carga_mayor_1000)

# Seleccionar los nombres de las ciudades con 5 o más empleadas
query_ciudades_empleadas = """
SELECT city, COUNT(*) AS num_empleados
FROM employees
GROUP BY city
HAVING COUNT(*) >= 5;
"""
df_ciudades_empleadas = pd.read_sql(query_ciudades_empleadas, engine)
print(df_ciudades_empleadas)
