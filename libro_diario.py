import csv
from datetime import datetime
from transaccion import Transaccion

class LibroDiario:
    def __init__(self):
        self.transacciones = []

    def agregar_transaccion(self, descripcion, monto, tipo, aplica_iva=False):
        numero = len(self.transacciones) + 1
        fecha = datetime.now().strftime("%d/%m/%Y")
        nueva = Transaccion(numero, descripcion, monto, tipo, fecha, aplica_iva)
        self.transacciones.append(nueva)
        print("✅ Transacción registrada.")

    def mostrar_todas(self):
        print("\n--- TRANSACCIONES REGISTRADAS ---")
        for t in self.transacciones:
            t.mostrar()

    def generar_reporte(self):
        fecha_actual = datetime.now().strftime("%d/%m/%Y")
        print(f"\nREPORTE DEL {fecha_actual}")
        print("-" * 30)
        for t in self.transacciones:
            t.mostrar()

    def calcular_totales(self):
        ingresos = sum(t.monto for t in self.transacciones if t.tipo == "Ingreso")
        egresos = sum(t.monto for t in self.transacciones if t.tipo == "Egreso")
        balance = ingresos + egresos
        iva_total = sum(t.monto * 0.16 for t in self.transacciones if t.tipo == "Ingreso" and t.aplica_iva)
        print("\n--- CÁLCULOS ---")
        print(f"Total Ingresos: ${ingresos:.2f}")
        print(f"Total Egresos: ${-egresos:.2f}")
        print(f"Balance Neto: ${balance:.2f}")
        print(f"IVA (16%): ${iva_total:.2f}")

    def exportar_csv(self, nombre_archivo="reporte.csv"):
        with open(nombre_archivo, mode='w', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["#", "Descripción", "Monto", "Tipo", "Fecha", "IVA"])
            for t in self.transacciones:
                writer.writerow([t.numero, t.descripcion, t.monto, t.tipo, t.fecha, "Sí" if t.aplica_iva else "No"])
        print(f"Reporte exportado como '{nombre_archivo}'")