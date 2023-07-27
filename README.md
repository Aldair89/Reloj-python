# Reloj-python
Este código es un programa en Python que crea una interfaz gráfica de usuario (GUI) utilizando el módulo tkinter para mostrar un reloj digital y permite al usuario ajustar la hora mostrada a través de una ventana de configuración.
Define la función get_current_time() que obtiene la hora actual del sistema utilizando datetime.now().strftime('%H:%M:%S') y actualiza la etiqueta time_label con la hora cada segundo. Esto permite que la etiqueta muestre la hora actualizada en tiempo real.

Define la función open_settings() que abre una ventana de ajustes cuando el usuario hace clic en el botón "Ajustes".

La ventana principal se crea utilizando tk.Tk() y se establece su título como "Reloj".

Crea una etiqueta llamada time_label para mostrar la hora actual en formato de texto grande (fuente Arial con tamaño 48).

Crea un botón llamado settings_button con el texto "Ajustes" que, cuando se hace clic, ejecuta la función open_settings().

Invoca la función get_current_time() para comenzar a mostrar la hora actualizada en la etiqueta time_label.

Inicia el bucle de eventos principal con window.mainloop(), lo que permite que la interfaz gráfica del programa responda a las interacciones del usuario y actualice la hora mostrada en la etiqueta.
