import displayio
import adafruit_imageload
import time
from adafruit_display_shapes.rect import Rect

from adafruit_hid.keycode import Keycode

# Listas de archivos de imagen
corner_images = [
    "/img/Selection_Windows.png",
    "/img/Selection_Mac.png"
]

platform_images = [
    "/img/Platform_Windows.png",
    "/img/Platform_Mac.png"
]

program_images = {
    "Office": "/img/prog/Office.png",
    "Illustrator": "/img/prog/Illustrator.png",
    "InDesign": "/img/prog/InDesign.png",
    "Photoshop": "/img/prog/Photoshop.png",
    "Premiere": "/img/prog/Premiere.png",
    "LigthRoom": "/img/prog/LigthRoom.png",
    "AfterEffects": "/img/prog/AfterEffects.png"
}


# Diccionario que mapea Keycodes a rutas de iconos
keycode_to_icon = {
    Keycode.SPACEBAR: "/img/prog/key/space.png",
    Keycode.O: "/img/prog/key/O.png",
    Keycode.I: "/img/prog/key/I.png",
}


def draw_icons(splash, key_actions_for_program, WIDTH, HEIGHT):
    """Dibuja iconos en dos filas en el centro de la pantalla según el Keycode correspondiente."""
    icon_group = displayio.Group()

    icon_size = 20
    spacing = 10

    num_icons_top = 5
    total_width_top = num_icons_top * icon_size + (num_icons_top - 1) * spacing
    x_start_top = (WIDTH - total_width_top) // 2
    y_position_top = HEIGHT // 2 - icon_size - spacing

    num_icons_bottom = 3
    total_width_bottom = num_icons_bottom * icon_size + (num_icons_bottom - 1) * spacing
    x_start_bottom = (WIDTH - total_width_bottom) // 2
    y_position_bottom = HEIGHT // 2 + spacing

    for index in range(num_icons_top):
        if index < len(key_actions_for_program):
            # Ajusta la descompresión para manejar hasta tres elementos
            action = key_actions_for_program[index]
            if len(action) == 3:
                modifier1, modifier2, key = action
            elif len(action) == 2:
                modifier1, key = action
                modifier2 = None
            else:
                key = action[0]
                modifier1 = modifier2 = None

            if key in keycode_to_icon:
                icon_path = keycode_to_icon[key]
                print(f"Intentando cargar la imagen para {key} desde {icon_path}")
                try:
                    image, palette = adafruit_imageload.load(icon_path, bitmap=displayio.Bitmap, palette=displayio.Palette)
                    icon_tilegrid = displayio.TileGrid(
                        image,
                        pixel_shader=palette,
                        x=x_start_top + index * (icon_size + spacing),
                        y=y_position_top
                    )
                    icon_group.append(icon_tilegrid)
                    print(f"Imagen cargada correctamente para {key}")
                except Exception as e:
                    print(f"Error al cargar {icon_path}: {e}")
                    placeholder = Rect(
                        x=x_start_top + index * (icon_size + spacing),
                        y=y_position_top,
                        width=icon_size,
                        height=icon_size,
                        fill=0x000000
                    )
                    icon_group.append(placeholder)

    for index in range(num_icons_bottom):
        if num_icons_top + index < len(key_actions_for_program):
            action = key_actions_for_program[num_icons_top + index]
            if len(action) == 3:
                modifier1, modifier2, key = action
            elif len(action) == 2:
                modifier1, key = action
                modifier2 = None
            else:
                key = action[0]
                modifier1 = modifier2 = None

            if key in keycode_to_icon:
                icon_path = keycode_to_icon[key]
                print(f"Intentando cargar la imagen para {key} desde {icon_path}")
                try:
                    image, palette = adafruit_imageload.load(icon_path, bitmap=displayio.Bitmap, palette=displayio.Palette)
                    icon_tilegrid = displayio.TileGrid(
                        image,
                        pixel_shader=palette,
                        x=x_start_bottom + index * (icon_size + spacing),
                        y=y_position_bottom
                    )
                    icon_group.append(icon_tilegrid)
                    print(f"Imagen cargada correctamente para {key}")
                except Exception as e:
                    print(f"Error al cargar {icon_path}: {e}")
                    placeholder = Rect(
                        x=x_start_bottom + index * (icon_size + spacing),
                        y=y_position_bottom,
                        width=icon_size,
                        height=icon_size,
                        fill=0x000000
                    )
                    icon_group.append(placeholder)

    if len(splash) > 1:
        splash.pop()
    splash.append(icon_group)


def update_icon_feedback(splash, button_index, WIDTH, HEIGHT, duration=0.2):
    """Proporciona feedback visual al presionar un botón dibujando un borde alrededor del icono."""
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

    # Determinar la posición del icono basado en el índice del botón
    if button_index < num_icons_top:
        x = x_start_top + button_index * (icon_size + spacing)
        y = y_position_top
    else:
        x = x_start_bottom + (button_index - num_icons_top) * (icon_size + spacing)
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
    time.sleep(duration)

    # Eliminar el rectángulo después de mostrar el feedback
    splash.remove(border_rect)

def display_program_icon(splash, program_name, width):
    """Carga y muestra una imagen pequeña del programa en la esquina superior izquierda."""
    try:
        # Construir la ruta del archivo de imagen pequeña
        filename = f"/img/prog/{program_name}_25.png"
        
        # Cargar la imagen y su paleta
        image, palette = adafruit_imageload.load(filename, bitmap=displayio.Bitmap, palette=displayio.Palette)
        
        # Configurar la posición de la imagen en la esquina superior izquierda
        x = 5
        y = 0
        tile_grid = displayio.TileGrid(image, pixel_shader=palette, x=x, y=y)
        
        # Añadir la imagen al grupo splash
        splash.append(tile_grid)
        print(f"Icono del programa {filename} cargado en posición ({x}, {y})")
    except Exception as e:
        print(f"Error al cargar el icono del programa {filename}: {e}")

def display_program_images(splash, filename):
    """Carga y muestra una imagen de programa en la pantalla."""
    try:
        # Remover la imagen previa si existe
        if len(splash) > 1:
            splash.pop(1)

        # Cargar la imagen y su paleta
        image, palette = adafruit_imageload.load(filename, bitmap=displayio.Bitmap, palette=displayio.Palette)
        
        # Configurar la posición de la imagen
        x = 60
        y = 30
        tile_grid = displayio.TileGrid(image, pixel_shader=palette, x=x, y=y)
        
        # Añadir la imagen al grupo splash
        splash.append(tile_grid)
        print(f"Imagen {filename} cargada en posición ({x}, {y})")
    except Exception as e:
        print(f"Error al cargar la imagen {filename}: {e}")

def load_and_display_image(splash, filename, width, height, center=True):
    """Carga y muestra una imagen centrada en la pantalla."""
    try:
        # Cargar la imagen y su paleta
        image, palette = adafruit_imageload.load(filename, bitmap=displayio.Bitmap, palette=displayio.Palette)
        
        # Calcular la posición para centrar la imagen
        x = (width - image.width) // 2 if center else 0
        y = (height - image.height) // 2 if center else 0
        tile_grid = displayio.TileGrid(image, pixel_shader=palette, x=x, y=y)
        
        # Añadir la imagen al grupo splash
        splash.append(tile_grid)
    except Exception as e:
        print(f"Error al cargar la imagen {filename}: {e}")

def display_corner_image(splash, filename, height):
    """Carga y muestra una imagen en la esquina inferior de la pantalla."""
    try:
        # Remover la imagen previa si existe
        if len(splash) > 2:
            splash.pop(-1)

        # Cargar la imagen y su paleta
        image, palette = adafruit_imageload.load(filename, bitmap=displayio.Bitmap, palette=displayio.Palette)
        
        # Configurar la posición de la imagen en la esquina inferior
        x = 5
        y = height - image.height
        tile_grid = displayio.TileGrid(image, pixel_shader=palette, x=x, y=y)
        
        # Añadir la imagen al grupo splash
        splash.append(tile_grid)
        print(f"Imagen de esquina {filename} cargada en posición ({x}, {y})")
    except Exception as e:
        print(f"Error al cargar la imagen {filename}: {e}")

def update_platform_display(splash, text_area, current_option, menu_options, height):
    """Actualiza la pantalla para mostrar la plataforma seleccionada."""
    # Limpiar el grupo splash
    while len(splash) > 0:
        splash.pop()
    
    # Cargar y mostrar la imagen de la plataforma
    load_and_display_image(splash, platform_images[current_option], 160, height)
    
    # Cargar y mostrar la imagen de la esquina
    #display_corner_image(splash, corner_images[current_option], height)
    
    # Actualizar el texto
    text_area.text = f"{menu_options[current_option]} Seleccionado"
    splash.append(text_area)
    time.sleep(0.5)
    

def update_application_display(splash, text_area, current_app, program_names):
    """Actualiza la pantalla para mostrar el programa seleccionado."""
    # Limpiar el grupo splash
    while len(splash) > 0:
        splash.pop()
    
    # Obtener el nombre del programa
    program_name = program_names[current_app]
    
    # Obtener el archivo de imagen correspondiente
    image_filename = program_images.get(program_name, None)
    
    if image_filename:
        # Cargar y mostrar la imagen del programa
        display_program_images(splash, image_filename)
    
    # Actualizar el texto para mostrar el nombre del programa
    text_area.text = f"{program_name}"
    splash.append(text_area)
    time.sleep(0.5)