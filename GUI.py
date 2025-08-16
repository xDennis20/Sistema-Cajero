import customtkinter
import tkinter.messagebox as messagebox
from Cajero import Cajero
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.cajero = Cajero()
        
        self.title("App")
        self.geometry("400x400")
        self._set_appearance_mode("dark")
        self.grid_rowconfigure(1, weight=2) 
        self.grid_rowconfigure(2, weight=0) 
        
        #Texto
        self.Titulo = customtkinter.CTkLabel(self,text="Sistema Cajero",font=("Arial",18))
        self.Titulo.grid(row=0, column=0, pady=10)
        
        #Frame
        self.frame_botones = customtkinter.CTkFrame(self)
        self.frame_botones.grid(row=2, column=0, pady=10,padx= 75,sticky="s")
        
        #Botones
        self.boton_crear_mesa = customtkinter.CTkButton(self.frame_botones,text="Crear Mesa",font=("Arial",14),width=250, height=50,command=self.ventana_crear_mesa)
        self.boton_crear_mesa.grid(pady=10)
        self.boton_agregar_pedido = customtkinter.CTkButton(self.frame_botones,text="Agregar pedido en mesa",font=("Arial",14),width=250, height=50, command=self.ventana_registrar_pedido)
        self.boton_agregar_pedido.grid(pady=10)
        self.boton_cobrar_mesa = customtkinter.CTkButton(self.frame_botones,text="Cobrar mesa",font=("Arial",14),width=250, height=50, command=self.ventana_cobrar_mesa)
        self.boton_cobrar_mesa.grid(pady=10)
        self.boton_mostrar_resumen_pedidos = customtkinter.CTkButton(self.frame_botones,text="Resumen de pedidos del dia",font=("Arial",14),width=250, height=50)
        self.boton_mostrar_resumen_pedidos.grid(pady=10)
    
    def ventana_crear_mesa(self):
        ventana = customtkinter.CTkToplevel(self)
        ventana.title("Nueva Mesa")
        ventana.geometry("200x200")
        
        ventana.wait_visibility()
        ventana.grab_set()

        frame = customtkinter.CTkFrame(ventana)
        frame.grid(row=0, column=0, padx=25, pady=30, sticky="nsew")

        label = customtkinter.CTkLabel(frame, text="Ingrese número de mesa:")
        label.grid(row=0, column=0, pady=10)

        entrada_numero = customtkinter.CTkEntry(frame)
        entrada_numero.grid(row=1, column=0, pady=5)
        
        def confirmar():
            try:
                numero_mesa = int(entrada_numero.get())
                if type(numero_mesa) == int:
                    self.cajero.crear_mesa(numero_mesa)
                    print("Mesa creada")
                messagebox.showinfo("Exito", f"Su mesa {numero_mesa} fue creada")
            except ValueError:
                messagebox.showerror("Error","El valor que coloco no es un numero entero")
                print("No es un valor entero")
            ventana.destroy()
         
        boton_confirmar = customtkinter.CTkButton(frame, text="Crear", command=confirmar)
        boton_confirmar.grid(row=2, column=0, pady=10)
            
    def ventana_registrar_pedido(self):
        ventana = customtkinter.CTkToplevel(self)
        ventana.title("Nueva Mesa")
        ventana.geometry("358x350")
        
        ventana.wait_visibility()
        ventana.grab_set()

        frame = customtkinter.CTkFrame(ventana)
        frame.grid(row=0, column=0, padx=10, pady=30, sticky="nsew")
        #Labels
        label_mesa = customtkinter.CTkLabel(frame,text="Ingrese la mesa que en la que desea registrar los pedidos: ")
        label_mesa.grid(row=0, column=0, pady=10)
        label_pedido = customtkinter.CTkLabel(frame,text="Ingrese el pedido: ")
        label_pedido.grid(row=2,column=0, pady=10)
        label_precio = customtkinter.CTkLabel(frame,text="Ingrese el precio del pedido (En decimales):")
        label_precio.grid(row=4,column=0, pady=10)
        #Entradas
        entrada_mesa = customtkinter.CTkEntry(frame)
        entrada_mesa.grid(row=1,column=0,pady=5)
        entrada_pedido = customtkinter.CTkEntry(frame)
        entrada_pedido.grid(row=3,column=0,pady=5)
        entrada_precio = customtkinter.CTkEntry(frame)
        entrada_precio.grid(row=6,column=0,pady=5)
        messagebox.showwarning("Advertencia","No deje en blanco los espacios requeridos")
        def confirmar():
            try:
                numero_mesa = int(entrada_mesa.get())
                pedido = entrada_pedido.get()
                precio = float(entrada_precio.get())
                if type(numero_mesa) == int or type(precio) == float:
                    self.cajero.registrar_pedido_en_mesa(numero_mesa,pedido,precio)
                messagebox.showinfo("Exito",f"Se registro el pedido en la mesa {numero_mesa}")
            except ValueError:
                messagebox.showerror("Error","Error en tipos de datos")
            ventana.destroy()
        
        boton_confirmar = customtkinter.CTkButton(frame,text="Confirmar Pedido",command=confirmar)
        boton_confirmar.grid(row=7,column=0,pady=10)
    def ventana_cobrar_mesa(self):
        ventana = customtkinter.CTkToplevel(self)
        ventana.title("Cobrar Mesa")
        ventana.geometry("222x250")

        ventana.wait_visibility()
        ventana.grab_set()

        frame = customtkinter.CTkFrame(ventana)
        frame.grid(row=0, column=0, padx=10, pady=30, sticky="nsew")

        label_mesa = customtkinter.CTkLabel(frame,text="Ingrese el numero de mesa:")
        label_mesa.grid(row=0,column=0,pady=10)
        label_dinero = customtkinter.CTkLabel(frame,text="Ingrese el dinero que dio el cliente: ")
        label_dinero.grid(row=2,column=0,pady=10)

        entrada_mesa = customtkinter.CTkEntry(frame)
        entrada_mesa.grid(row=1,column=0,pady=5)
        entrada_dinero = customtkinter.CTkEntry(frame)
        entrada_dinero.grid(row=3,column=0,pady=5)

        def confirmar():
            try:
                numero_mesa = int(entrada_mesa.get())
                dinero_cliente = float(entrada_dinero.get())
                if type(numero_mesa) == int or type(dinero_cliente) == float:
                    messagebox.showinfo("Exitos",f"Vuelto a dar: {self.cajero.cobrar_mesa(numero_mesa,dinero_cliente)}")
            except ValueError:
                messagebox.showerror("Error","Error en los tipos de dato")

        boton_confirmar = customtkinter.CTkButton(frame,text="Confirmar",command=confirmar)
        boton_confirmar.grid(row=4,column=0,pady=5)

        
app = App()
app.mainloop()