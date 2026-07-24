import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import tkinter.font as tkFont

class CifradorCesar:
    """Clase para implementar el Cifrado César con Módulo 27 (incluyendo Ñ)"""
    
    # Alfabeto extendido con la letra Ñ (27 caracteres)
    ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZÑ"
    
    def __init__(self):
        self.longitud_alfabeto = len(self.ALFABETO)  # 27
    
    def cifrar(self, texto, desplazamiento):
        """
        Cifra el texto usando el Cifrado César con Módulo 27
        """
        texto = texto.upper()
        resultado = ""
        
        for char in texto:
            if char in self.ALFABETO:
                # Obtener la posición del carácter en el alfabeto
                posicion = self.ALFABETO.index(char)
                # Aplicar el desplazamiento con módulo 27
                nueva_posicion = (posicion + desplazamiento) % 27
                resultado += self.ALFABETO[nueva_posicion]
            else:
                # Mantener caracteres que no estén en el alfabeto
                resultado += char
        
        return resultado
    
    def descifrar(self, texto, desplazamiento):
        """
        Descifra el texto usando el Cifrado César con Módulo 27
        """
        # Desplazamiento inverso
        desplazamiento_inverso = -desplazamiento
        return self.cifrar(texto, desplazamiento_inverso)


class AplicacionCifradorCesar:
    """Interfaz gráfica para el Cifrado César"""
    
    def __init__(self, ventana_principal):
        self.ventana = ventana_principal
        self.ventana.title("Cifrador César - Módulo 27")
        self.ventana.geometry("700x600")
        self.ventana.resizable(False, False)
        
        # Configurar colores
        self.color_fondo = "#1e1e2e"
        self.color_primario = "#2a9d8f"  # Verde militar/azul
        self.color_titulo = "#06d6a0"    # Verde brillante
        self.color_boton = "#e76f51"     # Naranja
        self.color_texto = "#ffffff"
        
        self.ventana.configure(bg=self.color_fondo)
        
        # Crear instancia del cifrador
        self.cifrador = CifradorCesar()
        
        # Crear interfaz
        self.crear_interfaz()
    
    def crear_interfaz(self):
        """Crea todos los elementos de la interfaz gráfica"""
        
        # Fuentes personalizadas
        fuente_titulo = tkFont.Font(family="Helvetica", size=18, weight="bold")
        fuente_subtitulo = tkFont.Font(family="Helvetica", size=12, weight="bold")
        fuente_normal = tkFont.Font(family="Helvetica", size=10)
        
        # ==================== ENCABEZADO ====================
        frame_encabezado = tk.Frame(self.ventana, bg=self.color_primario, height=80)
        frame_encabezado.pack(fill=tk.X, padx=0, pady=0)
        frame_encabezado.pack_propagate(False)
        
        # Título principal
        titulo = tk.Label(
            frame_encabezado,
            text="🔐 CIFRADOR CÉSAR 🔐",
            font=fuente_titulo,
            bg=self.color_primario,
            fg=self.color_titulo
        )
        titulo.pack(pady=10)
        
        # Subtítulo
        subtitulo = tk.Label(
            frame_encabezado,
            text="Módulo 27 - Incluyendo la letra Ñ",
            font=("Helvetica", 10),
            bg=self.color_primario,
            fg=self.color_texto
        )
        subtitulo.pack()
        
        # ==================== CONTENIDO PRINCIPAL ====================
        frame_principal = tk.Frame(self.ventana, bg=self.color_fondo)
        frame_principal.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)
        
        # --- Sección de Desplazamiento ---
        frame_desplazamiento = tk.LabelFrame(
            frame_principal,
            text="Desplazamiento",
            font=fuente_subtitulo,
            bg=self.color_fondo,
            fg=self.color_titulo,
            padx=10,
            pady=10,
            relief=tk.RAISED,
            borderwidth=2
        )
        frame_desplazamiento.pack(fill=tk.X, pady=(0, 15))
        
        frame_desplazamiento.grid_columnconfigure(1, weight=1)
        
        tk.Label(
            frame_desplazamiento,
            text="Número de desplazamiento (0-26):",
            font=fuente_normal,
            bg=self.color_fondo,
            fg=self.color_texto
        ).grid(row=0, column=0, sticky=tk.W, padx=5)
        
        self.entrada_desplazamiento = ttk.Spinbox(
            frame_desplazamiento,
            from_=0,
            to=26,
            width=10,
            font=fuente_normal,
            justify=tk.CENTER
        )
        self.entrada_desplazamiento.set(3)
        self.entrada_desplazamiento.grid(row=0, column=1, sticky=tk.W, padx=5)
        
        # --- Sección de Texto de Entrada ---
        tk.Label(
            frame_principal,
            text="📝 Texto a procesar:",
            font=fuente_subtitulo,
            bg=self.color_fondo,
            fg=self.color_titulo
        ).pack(anchor=tk.W, pady=(10, 5))
        
        frame_entrada = tk.Frame(frame_principal, bg=self.color_fondo)
        frame_entrada.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        # Scrollbar para texto de entrada
        scrollbar_entrada = ttk.Scrollbar(frame_entrada)
        scrollbar_entrada.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.texto_entrada = scrolledtext.ScrolledText(
            frame_entrada,
            height=6,
            font=fuente_normal,
            bg="#2a2a3a",
            fg=self.color_texto,
            insertbackground=self.color_titulo,
            relief=tk.SUNKEN,
            borderwidth=2,
            yscrollcommand=scrollbar_entrada.set
        )
        self.texto_entrada.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_entrada.config(command=self.texto_entrada.yview)
        
        # --- Botones de Acción ---
        frame_botones = tk.Frame(frame_principal, bg=self.color_fondo)
        frame_botones.pack(fill=tk.X, pady=15)
        
        btn_cifrar = tk.Button(
            frame_botones,
            text="🔒 CIFRAR",
            command=self.cifrar_texto,
            font=fuente_subtitulo,
            bg=self.color_primario,
            fg=self.color_texto,
            relief=tk.RAISED,
            padx=15,
            pady=10,
            cursor="hand2"
        )
        btn_cifrar.pack(side=tk.LEFT, padx=5)
        
        btn_descifrar = tk.Button(
            frame_botones,
            text="🔓 DESCIFRAR",
            command=self.descifrar_texto,
            font=fuente_subtitulo,
            bg=self.color_boton,
            fg=self.color_texto,
            relief=tk.RAISED,
            padx=15,
            pady=10,
            cursor="hand2"
        )
        btn_descifrar.pack(side=tk.LEFT, padx=5)
        
        btn_limpiar = tk.Button(
            frame_botones,
            text="🗑️  LIMPIAR",
            command=self.limpiar,
            font=fuente_subtitulo,
            bg="#7a7a8a",
            fg=self.color_texto,
            relief=tk.RAISED,
            padx=15,
            pady=10,
            cursor="hand2"
        )
        btn_limpiar.pack(side=tk.LEFT, padx=5)
        
        btn_salir = tk.Button(
            frame_botones,
            text="❌ SALIR",
            command=self.salir,
            font=fuente_subtitulo,
            bg="#e74c3c",
            fg=self.color_texto,
            relief=tk.RAISED,
            padx=15,
            pady=10,
            cursor="hand2"
        )
        btn_salir.pack(side=tk.LEFT, padx=5)
        
        # --- Sección de Resultado ---
        tk.Label(
            frame_principal,
            text="✅ Resultado:",
            font=fuente_subtitulo,
            bg=self.color_fondo,
            fg=self.color_titulo
        ).pack(anchor=tk.W, pady=(10, 5))
        
        frame_resultado = tk.Frame(frame_principal, bg=self.color_fondo)
        frame_resultado.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar para resultado
        scrollbar_resultado = ttk.Scrollbar(frame_resultado)
        scrollbar_resultado.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.texto_resultado = scrolledtext.ScrolledText(
            frame_resultado,
            height=6,
            font=fuente_normal,
            bg="#2a2a3a",
            fg="#06d6a0",
            relief=tk.SUNKEN,
            borderwidth=2,
            state=tk.DISABLED,
            yscrollcommand=scrollbar_resultado.set
        )
        self.texto_resultado.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_resultado.config(command=self.texto_resultado.yview)
    
    def cifrar_texto(self):
        """Realiza el cifrado del texto ingresado"""
        try:
            texto = self.texto_entrada.get("1.0", tk.END).strip()
            
            if not texto:
                messagebox.showwarning("Advertencia", "Por favor, ingresa un texto para cifrar.")
                return
            
            desplazamiento = int(self.entrada_desplazamiento.get())
            
            if desplazamiento < 0 or desplazamiento > 26:
                messagebox.showerror("Error", "El desplazamiento debe estar entre 0 y 26.")
                return
            
            resultado = self.cifrador.cifrar(texto, desplazamiento)
            self.mostrar_resultado(resultado)
            
        except ValueError:
            messagebox.showerror("Error", "El desplazamiento debe ser un número entero.")
    
    def descifrar_texto(self):
        """Realiza el descifrado del texto ingresado"""
        try:
            texto = self.texto_entrada.get("1.0", tk.END).strip()
            
            if not texto:
                messagebox.showwarning("Advertencia", "Por favor, ingresa un texto para descifrar.")
                return
            
            desplazamiento = int(self.entrada_desplazamiento.get())
            
            if desplazamiento < 0 or desplazamiento > 26:
                messagebox.showerror("Error", "El desplazamiento debe estar entre 0 y 26.")
                return
            
            resultado = self.cifrador.descifrar(texto, desplazamiento)
            self.mostrar_resultado(resultado)
            
        except ValueError:
            messagebox.showerror("Error", "El desplazamiento debe ser un número entero.")
    
    def mostrar_resultado(self, resultado):
        """Muestra el resultado en el área de texto del resultado"""
        self.texto_resultado.config(state=tk.NORMAL)
        self.texto_resultado.delete("1.0", tk.END)
        self.texto_resultado.insert(tk.END, resultado)
        self.texto_resultado.config(state=tk.DISABLED)
    
    def limpiar(self):
        """Limpia los campos de entrada y resultado"""
        self.texto_entrada.delete("1.0", tk.END)
        self.texto_resultado.config(state=tk.NORMAL)
        self.texto_resultado.delete("1.0", tk.END)
        self.texto_resultado.config(state=tk.DISABLED)
        self.entrada_desplazamiento.set(3)
    
    def salir(self):
        """Cierra la aplicación"""
        if messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?"):
            self.ventana.quit()


def main():
    """Función principal para iniciar la aplicación"""
    ventana = tk.Tk()
    app = AplicacionCifradorCesar(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
