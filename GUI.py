import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

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
        self.boton_crear_mesa = customtkinter.CTkButton(self.frame_botones,text="Crear Mesa",font=("Arial",14),width=250, height=50,command=self.crear_mesa)
        self.boton_crear_mesa.grid(pady=10)
        self.boton_agregar_pedido = customtkinter.CTkButton(self.frame_botones,text="Agregar pedido en mesa",font=("Arial",14),width=250, height=50)
        self.boton_agregar_pedido.grid(pady=10)
        self.boton_cobrar_mesa = customtkinter.CTkButton(self.frame_botones,text="Cobrar mesa",font=("Arial",14),width=250, height=50)
        self.boton_cobrar_mesa.grid(pady=10)
        self.boton_mostrar_resumen_pedidos = customtkinter.CTkButton(self.frame_botones,text="Resumen de pedidos del dia",font=("Arial",14),width=250, height=50)
        self.boton_mostrar_resumen_pedidos.grid(pady=10)
        
    def crear_mesa(self):
        print("Creando mesa")
            
        
        
app = App()
app.mainloop()