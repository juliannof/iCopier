import displayio
import adafruit_imageload
import time
from adafruit_display_shapes.rect import Rect



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

import displayio
from adafruit_display_shapes.rect import Rect

def draw_squares(splash, width, height):
    """Dibuja un fondo negro y luego cuadrados blancos en el centro de la pantalla."""
    square_size_top = 25
    square_size_bottom = 30
    separation = 2
    total_width_top = 5 * square_size_top + 4 * separation
    total_width_bottom = 3 * square_size_bottom + 2 * separation

    # Calcular la posición inicial para centrar los cuadrados superiores
    start_x_top = (width - total_width_top) // 2
    start_y_top = (height - square_size_top) // 2 - 20  # Subir 20 píxeles

    # Calcular la posición inicial para centrar los cuadrados inferiores
    start_x_bottom = (width - total_width_bottom) // 2
    start_y_bottom = start_y_top + square_size_top + separation + 5
      # Debajo de los cuadrados superiores

    # Crear un grupo para los cuadrados
    squares_group = displayio.Group()

    # Dibujar un fondo negro que cubra el área de los cuadrados blancos
    background_width = max(total_width_top, total_width_bottom)
    background_height = (square_size_top + separation) + (square_size_bottom + separation + 5)  # Altura total
    background_x = (width - background_width) // 2
    background_y = start_y_top

    background_rect = Rect(
        x=background_x, 
        y=background_y, 
        width=background_width, 
        height=background_height, 
        fill=0x000000  # Color negro
    )
    squares_group.append(background_rect)

    # Dibujar 5 cuadrados superiores
    for i in range(5):
        x = start_x_top + i * (square_size_top + separation)
        square = Rect(x=x, y=start_y_top, width=square_size_top, height=square_size_top, fill=0xa1a0a1)
        squares_group.append(square)

    # Dibujar 3 cuadrados inferiores
    for i in range(3):
        x = start_x_bottom + i * (square_size_bottom + separation)
        square = Rect(x=x, y=start_y_bottom, width=square_size_bottom, height=square_size_bottom, fill=0xFFFFFF)
        squares_group.append(square)

    # Añadir el grupo de cuadrados al grupo principal splash
    splash.append(squares_group)





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