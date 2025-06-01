class Transaccion:
    def __init__(self, numero, descripcion, monto, tipo, fecha, aplica_iva=False):
        self.numero = numero
        self.descripcion = descripcion
        self.monto = monto
        self.tipo = tipo
        self.fecha = fecha
        self.aplica_iva = aplica_iva

    def mostrar(self):
        print(f"{self.numero}. {self.descripcion} - ${self.monto:.2f} ({self.tipo}) - Fecha: {self.fecha}")