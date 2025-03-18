from machine import Pin
import time

# Definir pines para cada color
pin_rojo = Pin(4, Pin.OUT)
pin_verde = Pin(2, Pin.OUT)
pin_azul = Pin(17, Pin.OUT)

# Definir botón con resistencia pull-up interna
boton = Pin(12, Pin.IN, Pin.PULL_UP)

# Lista de colores en formato (rojo, verde, azul)
colores = [
    (1, 0, 0),  # Rojo
    (0, 1, 0),  # Verde
    (0, 0, 1),  # Azul
    (1, 1, 0),  # Amarillo
    (0, 1, 1),  # Cyan
    (1, 0, 1),  # Magenta
    (1, 1, 1)   # Blanco
]

indice_color = 0
leds_encendidos = False

def cambiar_color():
    global indice_color, leds_encendidos
    if leds_encendidos:
        pin_rojo.value(0)
        pin_verde.value(0)
        pin_azul.value(0)
        leds_encendidos = False
    else:
        r, g, b = colores[indice_color]
        pin_rojo.value(r)
        pin_verde.value(g)
        pin_azul.value(b)
        indice_color = (indice_color + 1) % len(colores)
        leds_encendidos = True

while True:
    if boton.value() == 0:  # Detecta si el botón es presionado
        time.sleep(0.2)  # Anti-rebote
        cambiar_color()
        
    time.sleep(0.1)  # Pequeño retardo para evitar sobrecarga del loop
