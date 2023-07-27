# Reloj-python
Este código es un programa en Python que crea una interfaz gráfica de usuario (GUI) utilizando el módulo tkinter para mostrar un reloj digital y permite al usuario ajustar la hora mostrada a través de una ventana de configuración.
Define la función get_current_time() que obtiene la hora actual del sistema utilizando datetime.now().strftime('%H:%M:%S') y actualiza la etiqueta time_label con la hora cada segundo. Esto permite que la etiqueta muestre la hora actualizada en tiempo real.

Define la función open_settings() que abre una ventana de ajustes cuando el usuario hace clic en el botón "Ajustes".

La ventana principal se crea utilizando tk.Tk() y se establece su título como "Reloj".

Crea una etiqueta llamada time_label para mostrar la hora actual en formato de texto grande (fuente Arial con tamaño 48).

Crea un botón llamado settings_button con el texto "Ajustes" que, cuando se hace clic, ejecuta la función open_settings().

Invoca la función get_current_time() para comenzar a mostrar la hora actualizada en la etiqueta time_label.

Inicia el bucle de eventos principal con window.mainloop(), lo que permite que la interfaz gráfica del programa responda a las interacciones del usuario y actualice la hora mostrada en la etiqueta.

Cuando el programa se ejecuta, muestra una ventana con la hora actual y un botón "Ajustes". Si el usuario hace clic en el botón "Ajustes", se abrirá una nueva ventana donde podrá ingresar una hora, minutos y segundos, y al hacer clic en el botón "Aplicar", la hora mostrada en la etiqueta se actualizará con el valor ingresado. Si el usuario ingresa una hora inválida, se mostrará un mensaje de error. El reloj seguirá actualizando la hora cada segundo en la ventana principal mientras esté abierta.
