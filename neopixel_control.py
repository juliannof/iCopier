import board
import neopixel
from config import pin_neopixels, num_pixels


# Inicialización de los NeoPixels
def initialize_neopixels(pin_pixels, num_pixels, brightness=0.3):
    """
    Inicializa los NeoPixels en el pin especificado.
    
    :param pin: Pin al que están conectados los NeoPixels.
    :param num_pixels: Número de NeoPixels.
    :param brightness: Brillo inicial de los NeoPixels.
    :return: Objeto NeoPixel inicializado.
    """
    pixels = neopixel.NeoPixel(pin_pixels, num_pixels, brightness=brightness, auto_write=False)
    set_all_pixels_color(pixels, (0, 100, 0))  # Verde con brillo 100 de 255
    pixels.show()
    return pixels

def set_all_pixels_color(pixels, color):
    """
    Establece el color de todos los NeoPixels.
    
    :param pixels: Objeto NeoPixel.
    :param color: Tupla de color (R, G, B).
    """
    for i in range(len(pixels)):
        pixels[i] = color
    pixels.show()

def turn_off_pixels(pixels):
    """
    Apaga todos los NeoPixels.
    
    :param pixels: Objeto NeoPixel.
    """
    set_all_pixels_color(pixels, (0, 0, 0))

def set_pixel_color(pixels, index, color):
    """
    Establece el color de un NeoPixel específico.
    
    :param pixels: Objeto NeoPixel.
    :param index: Índice del NeoPixel a modificar.
    :param color: Tupla de color (R, G, B).
    """
    if 0 <= index < len(pixels):
        pixels[index] = color
        pixels.show()