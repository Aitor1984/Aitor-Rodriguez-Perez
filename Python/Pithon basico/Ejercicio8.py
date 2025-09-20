# Ejercicio 8. Función encontrar_puesto_empleado
# Descripción: Crea una función que tome un nombre completo y una lista de empleados, y devuelva el puesto del empleado si está en la lista.
def encontrar_puesto_empleado(nombre_completo, empleados):
    for empleado in empleados:
        if f"{empleado['nombre']} {empleado['apellido']}" == nombre_completo:
            return empleado['puesto']
    return "La persona no trabaja aquí."