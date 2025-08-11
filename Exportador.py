from openpyxl import Workbook
from datetime import datetime

class Exportador:
    @staticmethod
    def exportar_pedidos_excel(list_pedidos):
        wb = Workbook()
        hoja = wb.active
        hoja["A1"] = "Mesa"
        hoja["B1"] = "Pedido"
        hoja["C1"] = "Precio"
        hoja["D1"] = "Fecha"

        for mesa in list_pedidos:
            for pedido in mesa.pedidos:
                hoja.append([mesa.numero, pedido["Comida"], pedido["Precio"], datetime.now().strftime("%d/%m/%Y")])

        wb.save("Pedidos.xlsx")
        print("Exportado con exito los pedidos a Excel")