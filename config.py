import board
from digitalio import DigitalInOut, Direction, Pull

# Número de NeoPixels.
num_pixels = 9

# Pin para los NeoPixels
pin_neopixels = board.GP16

# Configuración de pantalla
DISPLAY_WIDTH = 160
DISPLAY_HEIGHT = 128


# Pines para los botones (incluyendo los nuevos en GP11, GP12 y GP13)
button_pins = [
    board.GP5,  # Botón 1
    board.GP6,  # Botón 2
    board.GP7,  # Botón 3
    board.GP8,  # Botón 4
    board.GP9,  # Botón 5
    board.GP10, # Botón 6
    board.GP11, # Botón 7
    board.GP12, # Botón 8
    board.GP13  # Botón 9
]

# Configuración de botones
buttons = [DigitalInOut(pin) for pin in button_pins]

for button in buttons:
    button.direction = Direction.INPUT
    button.pull = Pull.UP

# Pines para los LEDs
led_pins = [
    board.GP0,  # LED 1
    board.GP1,  # LED 2
    board.GP2,  # LED 3
    board.GP3,  # LED 4
    board.GP4,  # LED 5
    board.LED   # LED 6 (integrado)
]