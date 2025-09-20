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

# DataFrame de pedidos y clientes
query_pedidos_clientes = """
SELECT o.order_id, o.order_date, o.shipped_date, o.customer_id, c.company_name, c.country
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;
"""
df_pedidos_clientes = pd.read_sql(query_pedidos_clientes, engine)

# DataFrame de productos, proveedores y detalles de pedidos
query_productos_detalles = """
SELECT od.order_id, od.product_id, od.unit_price, od.quantity, p.product_name, p.units_in_stock, p.units_on_order, p.discontinued,
       s.company_name AS supplier_name, s.country AS supplier_country
FROM order_details od
JOIN products p ON od.product_id = p.product_id
JOIN suppliers s ON p.supplier_id = s.supplier_id;
"""
df_productos_detalles = pd.read_sql(query_productos_detalles, engine)


# Estudio de la evolución de los pedidos realizados a lo largo del tiempo
df_pedidos_clientes['order_date'] = pd.to_datetime(df_pedidos_clientes['order_date'])
df_pedidos_clientes['year_month'] = df_pedidos_clientes['order_date'].dt.to_period('M')

evolucion = df_pedidos_clientes.groupby('year_month').size().reset_index(name='num_pedidos')
print("📈 Evolución de pedidos por mes:")
print(evolucion)


# Investiga los países con más ventas y asigna continente
continentes = {
    'Europe': ['Austria', 'Belgium', 'Denmark', 'Finland', 'France', 'Germany', 'Ireland', 'Italy', 'Norway', 'Poland', 'Portugal', 'Spain', 'Sweden', 'Switzerland', 'UK'],
    'America': ['Argentina', 'Brazil', 'Canada', 'Mexico', 'USA', 'Venezuela']
}

def asignar_continente(pais):
    for continente, paises in continentes.items():
        if pais in paises:
            return continente
    return 'Other'

df_pedidos_clientes['continente'] = df_pedidos_clientes['country'].apply(asignar_continente)
distribucion = df_pedidos_clientes['continente'].value_counts().reset_index(name='num_pedidos')
print("🌎 Distribución de pedidos por continente:")
print(distribucion)

# Investiga si la compañía de transporte está relacionada con los retrasos
df_pedidos_clientes['shipped_date'] = pd.to_datetime(df_pedidos_clientes['shipped_date'])
df_pedidos_clientes['retraso_dias'] = (df_pedidos_clientes['shipped_date'] - df_pedidos_clientes['order_date']).dt.days

# Agrupar por país para ver rangos
retrasos_por_pais = df_pedidos_clientes[df_pedidos_clientes['retraso_dias'].notnull()].groupby('country')['retraso_dias'].describe()
print("📦 Estadísticas de retraso por país:")
print(retrasos_por_pais)

# Calcular precio total por pedido
df_productos_detalles['total_precio'] = df_productos_detalles['unit_price'] * df_productos_detalles['quantity']
df_precios = df_productos_detalles.merge(df_pedidos_clientes[['order_id', 'country']], on='order_id')

precio_medio = df_precios.groupby('country')['total_precio'].mean().reset_index(name='precio_medio')
print("💸 Precio medio por pedido según país del cliente:")
print(precio_medio)

# ¿Qué porcentaje de clientes no tienen pedidos registrados?
clientes_con_pedidos = df_pedidos_clientes['customer_id'].unique()
query_clientes = "SELECT customer_id FROM customers;"
df_clientes = pd.read_sql(query_clientes, engine)

sin_pedidos = df_clientes[~df_clientes['customer_id'].isin(clientes_con_pedidos)]
porcentaje = len(sin_pedidos) / len(df_clientes) * 100
print(f"Porcentaje de clientes sin pedidos registrados: {porcentaje:.2f}%")


# Productos más demandados
productos_demandados = df_productos_detalles.groupby('product_name')['quantity'].sum().sort_values(ascending=False).head(10)
print("Top 10 productos más demandados:")
print(productos_demandados)

# Productos que necesitan reabastecimiento urgente
query_restock = """
SELECT product_name, units_in_stock, units_on_order
FROM products
WHERE units_in_stock <= 20 AND units_on_order = 0;
"""
df_restock = pd.read_sql(query_restock, engine)
print("Productos que necesitan reabastecimiento urgente:")
print(df_restock)
