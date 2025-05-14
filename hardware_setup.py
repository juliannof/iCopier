# hardware_setup.py
from digitalio import DigitalInOut, Direction, Pull
import displayio
from adafruit_st7735r import ST7735R
from pwmio import PWMOut

def setup_hardware(button_pins, led_pins):
    buttons = []
    leds = []

    for pin in button_pins:
        button = DigitalInOut(pin)
        button.direction = Direction.INPUT
        button.pull = Pull.UP
        buttons.append(button)

    for pin in led_pins:
        led = DigitalInOut(pin)
        led.direction = Direction.OUTPUT
        leds.append(led)

    return buttons, leds

def setup_display(spi, tft_cs, tft_dc, tft_reset, tft_bl):
    backlight = PWMOut(tft_bl, frequency=5000, duty_cycle=65535)
    display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_reset)
    display = ST7735R(display_bus, width=160, height=128, rotation=270, bgr=True, colstart=0, rowstart=0)
    return display, backlight