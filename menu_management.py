import time
from utils import is_long_press
from image_loader import *

threshold=0.2

def update_background_color(background, is_pc):
    """Actualiza el color de fondo según el tipo de dispositivo."""
    background.pixel_shader[0] = 0x0000FF if is_pc else 0x800080

def get_neopixel_index(button_index, num_pixels):
    """Calcula el índice del NeoPixel basado en el índice del botón."""
    return num_pixels - 1 - button_index

def handle_user_interaction(buttons, leds, pixels, pixel_timers, current_time, num_pixels, pixel_colors):
    """Gestiona la interacción del usuario con botones, LEDs y NeoPixels."""
    interaction = False
    for i, button in enumerate(buttons):
        if not button.value:
            interaction = True
            if i < len(leds):
                leds[i].value = True
            neopixel_index = get_neopixel_index(i, num_pixels)
            if neopixel_index < len(pixels):
                pixels[neopixel_index] = (0, 255, 0)
                pixel_timers[neopixel_index] = current_time + 1
        else:
            if i < len(leds):
                leds[i].value = False
            neopixel_index = get_neopixel_index(i, num_pixels)
            if neopixel_index < len(pixels) and current_time >= pixel_timers[neopixel_index]:
                pixels[neopixel_index] = pixel_colors[neopixel_index]
    return interaction

def manage_menu(buttons, current_option, menu_options, selection_made, text_area, corner_text, corner_text1):
    """Gestiona el menú de opciones, permitiendo seleccionar y cambiar opciones."""
    if not selection_made:
        if not buttons[5].value:
            if is_long_press(buttons[5]):
                selection_made = True
                text_area.text = "Seleccionado"
                corner_text.text = menu_options[current_option]
                corner_text1.text = "C | P | CO | DES | G"
            else:
                current_option = (current_option + 1) % len(menu_options)
                text_area.text = menu_options[current_option]
        time.sleep(0.3)  # Reducir el tiempo de espera para mejorar la respuesta
    return current_option, selection_made

def select_platform(splash, text_area, button, menu_options, current_option, height):
    """Permite seleccionar una plataforma mediante pulsaciones cortas y largas."""
    print(f"Plataforma seleccionada ahora: {menu_options[current_option]}")
    update_platform_display(splash, text_area, current_option, menu_options, height)
    platform_selected = False
    while not platform_selected:
        if not button.value:
            if is_long_press(button, threshold):  # Asegúrate de usar el argumento correcto
                platform_selected = True
                print(f"Teclado para {menu_options[current_option]}")
            else:
                current_option = (current_option + 1) % len(menu_options)
                update_platform_display(splash, text_area, current_option, menu_options, height)
                print(f"Cambiada a: {menu_options[current_option]}")
            while not button.value:
                time.sleep(0.1)
    return current_option

def select_program(splash, text_area, button, program_names, current_app):
    """Permite seleccionar un programa mediante pulsaciones cortas y largas."""
    program_selected = False
    update_application_display(splash, text_area, current_app, program_names)
    
    while not program_selected:
        if not button.value:  # Si el botón está presionado
            if is_long_press(button, threshold):  # Pulsación larga para seleccionar
                program_selected = True
                print(f"Programa seleccionado: {program_names[current_app]}")
            else:  # Pulsación corta para cambiar de programa
                current_app = (current_app + 1) % len(program_names)
                update_application_display(splash, text_area, current_app, program_names)
                print(f"Programa cambiado a: {program_names[current_app]}")
            
            # Esperar a que el botón sea liberado
            while not button.value:
                time.sleep(0.1)
    
    return current_app