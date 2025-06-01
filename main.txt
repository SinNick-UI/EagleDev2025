from libro_diario import LibroDiario

def menu():
    print("\n--- SISTEMA DE GESTIÓN CONTABLE ---")
    print("1. Registrar transacción")
    print("2. Ver transacciones")
    print("3. Generar reporte")
    print("4. Calcular totales e IVA")
    print("5. Exportar reporte CSV")
    print("6. Salir")

def ejecutar():
    libro = LibroDiario()
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            desc = input("Descripción: ")
            try:
                monto = float(input("Monto (positivo para ingreso, negativo para egreso): "))
                tipo = "Ingreso" if monto > 0 else "Egreso"
                iva = input("¿Aplica IVA? (s/n): ").lower() == "s"
                libro.agregar_transaccion(desc, monto, tipo, iva)
            except ValueError:
                print("❌ Monto inválido.")
        elif opcion == "2":
            libro.mostrar_todas()
        elif opcion == "3":
            libro.generar_reporte()
        elif opcion == "4":
            libro.calcular_totales()
        elif opcion == "5":
            libro.exportar_csv()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    ejecutar()