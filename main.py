import customtkinter as ctk
import matplotlib.pyplot as plt


def graficar():
    try:
        m = float(entry_m.get())
        b = float(entry_b.get())
        
        lbl_msg.configure(text="") 
        
        x = [-10, 10]
        y = [m * x[0] + b, m * x[1] + b]       
        plt.figure("Gráfica")
        plt.plot(x, y, 'b--', label=f'f(x) = {m}x + {b}')
        plt.axhline(0, color='black') 
        plt.axvline(0, color='black') 
        plt.grid()
        plt.legend()
        plt.show()
        
    except ValueError:
        lbl_msg.configure(text="Error: Ingresa números válidos", text_color="red")


app = ctk.CTk()
app.geometry("300x250")
app.title("Generador Lineal")

# Elementos de la interfaz apilados verticalmente
ctk.CTkLabel(app, text="f(x) = mx + b", font=("Arial", 18, "bold")).pack(pady=15)

entry_m = ctk.CTkEntry(app, placeholder_text="Valor de la pendiente (m)")
entry_m.pack(pady=5)

entry_b = ctk.CTkEntry(app, placeholder_text="Término independiente (b)")
entry_b.pack(pady=5)

ctk.CTkButton(app, text="Graficar", command=graficar).pack(pady=15)

lbl_msg = ctk.CTkLabel(app, text="")
lbl_msg.pack()

app.mainloop()