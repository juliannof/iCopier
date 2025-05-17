import time
import board
import busio
import displayio
import neopixel
from digitalio import DigitalInOut, Direction, Pull
from adafruit_st7735r import ST7735R
from adafruit_display_text import label
import terminalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from pwmio import PWMOut
from utils import smooth_transition_to_10_percent
from fourwire import FourWire
from image_loader import *
from menu_management import *
from config import *
from hardware_setup import *
from keyboard_utils import type_character
from key_config import key_actions, NO_MODIFIER

# Mapeo de Keycode a nombres de teclas
keycode_to_name = {
    Keycode.A: "A",
    Keycode.B: "B",
    Keycode.C: "C",
    Keycode.D: "D",
    Keycode.E: "E",
    Keycode.F: "F",
    Keycode.G: "G",
    Keycode.H: "H",
    Keycode.I: "I",
    Keycode.J: "J",
    Keycode.K: "K",
    Keycode.L: "L",
    Keycode.M: "M",
    Keycode.N: "N",
    Keycode.O: "O",
    Keycode.P: "P",
    Keycode.Q: "Q",
    Keycode.R: "R",
    Keycode.S: "S",
    Keycode.T: "T",
    Keycode.U: "U",
    Keycode.V: "V",
    Keycode.W: "W",
    Keycode.X: "X",
    Keycode.Y: "Y",
    Keycode.Z: "Z",
    Keycode.SPACEBAR: "SPACE",
    # Agrega más mapeos según sea necesario
}

def keycode_to_string(keycode):
    return keycode_to_name.get(keycode, f"Unknown Keycode ({keycode})")

# Liberar displays previos
displayio.release_displays()

# Configuración de SPI para ST7735R
spi = busio.SPI(clock=board.GP18, MOSI=board.GP19)
tft_cs = board.GP22
tft_dc = board.GP21
tft_reset = board.GP20
tft_bl = board.GP17

# Configuración del bus de display
display_bus = FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=tft_reset
)

# Inicialización de la pantalla ST7735R
WIDTH = 160  # Ancho después de rotar
HEIGHT = 128  # Alto después de rotar
display = ST7735R(
    display_bus,
    width=WIDTH,
    height=HEIGHT,
    rotation=270,  # Rotación de 90 grados
    bgr=True,  # Ajustar si es necesario
    colstart=0,  # Offset de columna
    rowstart=0,  # Offset de fila
)

# Configuración de la retroiluminación
backlight = PWMOut(tft_bl, frequency=5000, duty_cycle=65535)

# Crear un grupo de display
splash = displayio.Group()

# Asigna el grupo `splash` al display usando `root_group`
display.root_group = splash

# Subgrupo para la imagen de esquina
corner_group = displayio.Group()
splash.append(corner_group)

# Subgrupo para el contenido principal
main_content_group = displayio.Group()
splash.append(main_content_group)

# Crear el área de texto principal
text_area = label.Label(
    terminalio.FONT,
    text="",
    color=0xFFFFFF,
    scale=1,
    anchor_point=(0.5, 0.5),
    anchored_position=(WIDTH // 2, 120),
)
main_content_group.append(text_area)

pixels = neopixel.NeoPixel(pin_neopixels, num_pixels, brightness=0.3)

# Configuración del teclado
keyboard = Keyboard(usb_hid.devices)

def update_icon_feedback(splash, key, key_actions, WIDTH, HEIGHT):
    """Proporciona feedback visual al presionar un botón dibujando un borde alrededor del icono."""
    # Tamaño y posición de los iconos
    icon_size = 25
    spacing = 10

    # Configuración para la fila superior (4 iconos)
    num_icons_top = 4
    total_width_top = num_icons_top * icon_size + (num_icons_top - 1) * spacing
    x_start_top = (WIDTH - total_width_top) // 2
    y_position_top = HEIGHT // 2 - icon_size - spacing

    # Configuración para la fila inferior (3 iconos)
    num_icons_bottom = 3
    total_width_bottom = num_icons_bottom * icon_size + (num_icons_bottom - 1) * spacing
    x_start_bottom = (WIDTH - total_width_bottom) // 2
    y_position_bottom = HEIGHT // 2 + spacing

    # Encontrar el índice del key en key_actions
    index = None
    for idx, (modifier, k) in enumerate(key_actions):
        if k == key:
            index = idx
            break

    if index is not None:
        # Determinar la posición del icono
        if index < num_icons_top:
            x = x_start_top + index * (icon_size + spacing)
            y = y_position_top
        else:
            x = x_start_bottom + (index - num_icons_top) * (icon_size + spacing)
            y = y_position_bottom

        # Crear un rectángulo con borde blanco alrededor del icono
        border_rect = Rect(
            x=x - 2,  # Un poco más grande que el icono
            y=y - 2,
            width=icon_size + 4,
            height=icon_size + 4,
            outline=0xFFFFFF  # Blanco
        )

        # Añadir el rectángulo al grupo splash
        splash.append(border_rect)

        # Mantener el borde visible por un corto período
        time.sleep(0.2)

        # Eliminar el rectángulo después de mostrar el feedback
        splash.remove(border_rect)

def main():
    menu_options = ["PC", "Mac"]
    current_option = 0
    program_names = list(program_images.keys())
    current_app = 0

    while True:
        print("Iniciando selección de plataforma...")
        text_area.text = "Iniciando selección de plataforma..."
        current_option = select_platform(
            main_content_group,
            text_area,
            buttons[5],
            menu_options,
            current_option,
            HEIGHT
        )
        print(f"Plataforma seleccionada: {menu_options[current_option]}")

        time.sleep(1)

        print("Iniciando selección de programa...")
        text_area.text = "Iniciando selección de programa..."

        # Mostrar una imagen en la esquina
        display_corner_image(corner_group, corner_images[current_option], HEIGHT)

        current_app = select_program(
            main_content_group,
            text_area,
            buttons[5],
            program_names,
            current_app
        )
        program_name = program_names[current_app]
        print(f"Programa seleccionado: {program_name}")

        # Mostrar el icono pequeño del programa seleccionado
        display_program_icon(corner_group, program_names[current_app], WIDTH)

        time.sleep(1)

        print(f"Has seleccionado: {program_name}")

        # Dibujar iconos en el centro de la pantalla
        draw_icons(splash, key_actions[program_name], WIDTH, HEIGHT)

        # Determinar la contraseña según la plataforma seleccionada
        if menu_options[current_option] == "PC":
            password = "!Ds8902201"
            platform_modifier = Keycode.CONTROL
        else:
            password = "9821"
            platform_modifier = Keycode.GUI

        # Bucle para verificar el funcionamiento de los botones
        while True:
            for index, button in enumerate(buttons):
                if not button.value:  # Si el botón está presionado (normalmente alto, bajo cuando se presiona)
                    print(f"Botón {index} presionado")

                    # Proporcionar feedback visual basado en la posición del botón
                    #update_icon_feedback(splash, index, WIDTH, HEIGHT)

                    if index == 5:
                        # Escribir la contraseña
                        for char in password:
                            type_character(keyboard, char)
                        
                        # Enviar Enter inmediatamente después de la contraseña
                        keyboard.press(Keycode.ENTER)
                        keyboard.release_all()
                        
                        print(f"Contraseña '{password}' enviada con Enter.")
                        break  # Salir del bucle después de enviar la contraseña
                    else:
                        # Enviar la acción de tecla correspondiente al botón
                        if program_name in key_actions:
                            actions = key_actions[program_name]
                            if index < len(actions):
                                action = actions[index]
                                # Procesar la acción de tecla
                                if len(action) == 3:
                                    modifier1, modifier2, key = action
                                    if modifier1:
                                        keyboard.press(modifier1)
                                    if modifier2:
                                        keyboard.press(modifier2)
                                    keyboard.press(key)
                                elif len(action) == 2:
                                    modifier, key = action
                                    if modifier:
                                        keyboard.press(modifier)
                                    keyboard.press(key)
                                elif len(action) == 1:
                                    key = action[0]
                                    keyboard.press(key)

                                keyboard.release_all()

                                # Imprimir una descripción más clara
                                key_name = keycode_to_string(key)
                                print(f"Acción de tecla {key_name} enviada para el programa {program_name}.")

                    time.sleep(0.05)  # Pequeña pausa para evitar múltiples lecturas rápidas

            time.sleep(0.02)  # Esperar un poco antes de verificar de nuevo

# Ejecutar la función principal
main()