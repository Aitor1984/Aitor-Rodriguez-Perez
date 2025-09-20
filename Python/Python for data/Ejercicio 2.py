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

# ¿Cuántos empleados tenemos contratados en 'Global Importaciones'? Indica su id, nombre, apellido, ciudad y país.
query_empleados = """
SELECT employee_id, first_name, last_name, city, country
FROM employees;
"""
df_empleados = pd.read_sql(query_empleados, engine)
print(df_empleados)

# ¿Qué productos tenemos? Indica el id del producto, id del proveedor, nombre del producto, precio por unidad, unidades en stock, unidades pedidas al proveedor y productos descontinuados.
query_productos = """
SELECT product_id, supplier_id, product_name, unit_price, units_in_stock, units_on_order, discontinued
FROM products;
"""
df_productos = pd.read_sql(query_productos, engine)
print(df_productos)

# ¿Tenemos productos descontinuados? Indica el nombre del producto y cantidad que nos queda en stock.
query_descontinuados = """
SELECT product_name, units_in_stock
FROM products
WHERE discontinued = 1;
"""
df_descontinuados = pd.read_sql(query_descontinuados, engine)
print(df_descontinuados)

# ¿Qué proveedores tenemos? Indica el id de la compañía, nombre de la compañía, ciudad y país.
query_proveedores = """
SELECT supplier_id, company_name, city, country
FROM suppliers;
"""
df_proveedores = pd.read_sql(query_proveedores, engine)
print(df_proveedores)

# ¿Qué pedidos hemos tenido? Indica el número de pedido, id del cliente, id del transportista, día del pedido, día requerido de llegada y día de llegada real.
query_pedidos = """
SELECT order_id, customer_id, ship_via, order_date, required_date, shipped_date
FROM orders;
"""
df_pedidos = pd.read_sql(query_pedidos, engine)
print(df_pedidos)

# ¿Cuántos pedidos hemos tenido?
query_total_pedidos = """
SELECT COUNT(*) AS total_pedidos
FROM orders;
"""
df_total_pedidos = pd.read_sql(query_total_pedidos, engine)
print(df_total_pedidos)

# ¿Cuántos clientes tenemos? Indica el id del cliente, nombre de la compañía, ciudad y país.
query_clientes = """
SELECT customer_id, company_name, city, country
FROM customers;
"""
df_clientes = pd.read_sql(query_clientes, engine)
print(df_clientes)

# ¿Con qué empresas de transporte trabajamos? Indica su id del transportista y el nombre de la compañía.
query_transportistas = """
SELECT shipper_id, company_name
FROM shippers;
"""
df_transportistas = pd.read_sql(query_transportistas, engine)
print(df_transportistas)

# ¿Cómo son las relaciones de reporte de resultados entre los empleados?
query_relaciones_empleados = """
SELECT e.employee_id, e.first_name || ' ' || e.last_name AS empleado,
       m.employee_id AS manager_id, m.first_name || ' ' || m.last_name AS manager
FROM employees e
LEFT JOIN employees m ON e.reports_to = m.employee_id
ORDER BY e.employee_id;
"""
df_relaciones = pd.read_sql(query_relaciones_empleados, engine)
print(df_relaciones)





