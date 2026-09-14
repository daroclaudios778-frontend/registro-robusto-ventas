def registrar_venta():
    try:
        precio = float(input("Ingrese el precio unitario: "))
        cantidad = int(input("Ingrese la cantidad vendida: "))

        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        total = precio * cantidad

    except ValueError as error:
        print(f"Error: {error}")

    else:
        print(f"Venta registrada. Total: ${total:.2f}")

    finally:
        print("La operación de venta finalizó.")


if __name__ == "__main__":
    registrar_venta()