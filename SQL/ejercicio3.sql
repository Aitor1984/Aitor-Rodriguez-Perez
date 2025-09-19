/* 1. Crea una tabla llamada "Productos" con las columnas: "id" (entero, clave primaria), "nombre" (texto) y "precio" (numérico). */
CREATE TABLE Productos (
  id INT PRIMARY KEY,
  nombre TEXT,
  precio NUMERIC
);

/* 2. Inserta al menos cinco registros en la tabla "Productos". */
INSERT INTO Productos (id, nombre, precio) VALUES
(1, 'Camisa', 40),
(2, 'Pantalón', 60),
(3, 'Zapatos', 80),
(4, 'Chaqueta', 100),
(5, 'Gorra', 20);

/* 3. Actualiza el precio de un producto en la tabla "Productos". */
UPDATE Productos
SET precio = 65
WHERE id = 2;

/* 4. Elimina un producto de la tabla "Productos". */
DELETE FROM Productos
WHERE id = 5;

/* 5. Realiza una consulta que muestre los nombres de los usuarios junto con los nombres de los productos que han comprado (utiliza un INNER JOIN con la tabla "Productos"). */
SELECT Usuarios.nombre, Productos.nombre
FROM Pedidos
INNER JOIN Usuarios ON Pedidos.id_usuario = Usuarios.id
INNER JOIN Productos ON Pedidos.id_producto = Productos.id;