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
        self.boton_agregar_pedido = customtkinter.CTkButton(self.frame_botones,text="Agregar pedido en mesa",font=("Arial",14),width=250, height=50)
        self.boton_agregar_pedido.grid(pady=10)
        self.boton_cobrar_mesa = customtkinter.CTkButton(self.frame_botones,text="Cobrar mesa",font=("Arial",14),width=250, height=50)
        self.boton_cobrar_mesa.grid(pady=10)
        self.boton_mostrar_resumen_pedidos = customtkinter.CTkButton(self.frame_botones,text="Resumen de pedidos del dia",font=("Arial",14),width=250, height=50)
        self.boton_mostrar_resumen_pedidos.grid(pady=10)
    
    def ventana_crear_mesa(self):
        ventana = customtkinter.CTkToplevel(self)
        ventana.title("Nueva Mesa")
        ventana.geometry("200x200")
        
        # Forzar a que sea modal
        ventana.wait_visibility()
        ventana.grab_set()

        frame = customtkinter.CTkFrame(ventana)
        frame.grid(row=0, column=0, padx=25, pady=30, sticky="nsew")

        label = customtkinter.CTkLabel(frame, text="Ingrese número de mesa:")
        label.grid(row=0, column=0, pady=10)

        entry_numero = customtkinter.CTkEntry(frame)
        entry_numero.grid(row=1, column=0, pady=5)
        
        def confirmar():
            try:
                numero_mesa = int(entry_numero.get())
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
            
        
        
app = App()
app.mainloop()