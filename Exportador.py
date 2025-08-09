from openpyxl import Workbook
from Cajero import Cajero

class Exportador:
    @staticmethod
    def exportar_pedidos_excel():
        wb = Workbook()
        hoja = wb.active
        lista = Cajero().ventas_dia
        hoja["A1"] = "Mesa"
        hoja["B1"] = "Pedido"
        hoja["C1"] = "Precio"

        fila = 2
        for pedido in lista:
            hoja.cell(row= fila,column=1,value=pedido.get("Mesa"))
            hoja.cell(row= fila,column=2,value=pedido.get("Pedido"))
            hoja.cell(row= fila,column=3,value=pedido.get("Precio"))
            fila+=1

        wb.save("Pedidos.xlsx")