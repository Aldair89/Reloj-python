import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def get_current_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    time_label.config(text=current_time)
    time_label.after(1000, get_current_time)

def open_settings():
    def apply_settings():
        try:
            new_hour = int(hour_entry.get())
            new_minute = int(minute_entry.get())
            new_second = int(second_entry.get())

            if 0 <= new_hour < 24 and 0 <= new_minute < 60 and 0 <= new_second < 60:
                new_time = f"{new_hour:02d}:{new_minute:02d}:{new_second:02d}"
                time_label.config(text=new_time)
                messagebox.showinfo("Ajustes", "La hora se ha actualizado correctamente.")
                settings_window.destroy()
            else:
                messagebox.showerror("Error", "Formato de hora inválido.")
        except ValueError:
            messagebox.showerror("Error", "Formato de hora inválido.")

    settings_window = tk.Toplevel(window)
    settings_window.title("Ajustes")

    hour_label = tk.Label(settings_window, text="Hora:")
    hour_label.grid(row=0, column=0, padx=10, pady=10)
    hour_entry = tk.Entry(settings_window)
    hour_entry.grid(row=0, column=1, padx=10, pady=10)

    minute_label = tk.Label(settings_window, text="Minutos:")
    minute_label.grid(row=1, column=0, padx=10, pady=10)
    minute_entry = tk.Entry(settings_window)
    minute_entry.grid(row=1, column=1, padx=10, pady=10)

    second_label = tk.Label(settings_window, text="Segundos:")
    second_label.grid(row=2, column=0, padx=10, pady=10)
    second_entry = tk.Entry(settings_window)
    second_entry.grid(row=2, column=1, padx=10, pady=10)

    apply_button = tk.Button(settings_window, text="Aplicar", command=apply_settings)
    apply_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Crear ventana principal
window = tk.Tk()
window.title("Reloj")

# Etiqueta para mostrar la hora actual
time_label = tk.Label(window, text="", font=("Arial", 48))
time_label.pack(pady=20)

# Botón para abrir la ventana de ajustes
settings_button = tk.Button(window, text="Ajustes", command=open_settings)
settings_button.pack(pady=10)

# Obtener y mostrar la hora actual
get_current_time()

# Iniciar el bucle de eventos
window.mainloop()
