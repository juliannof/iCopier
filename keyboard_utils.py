# keyboard_utils.py
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard

def type_character(keyboard, character):
    if character.isalpha():
        if character.isupper():
            keyboard.press(Keycode.SHIFT, getattr(Keycode, character))
            keyboard.release_all()
        else:
            keyboard.press(getattr(Keycode, character.upper()))
            keyboard.release_all()
    elif character.isdigit():
        number_keycodes = {
            '0': Keycode.ZERO,
            '1': Keycode.ONE,
            '2': Keycode.TWO,
            '3': Keycode.THREE,
            '4': Keycode.FOUR,
            '5': Keycode.FIVE,
            '6': Keycode.SIX,
            '7': Keycode.SEVEN,
            '8': Keycode.EIGHT,
            '9': Keycode.NINE
        }
        keyboard.press(number_keycodes[character])
        keyboard.release_all()
    else:
        char_to_keycode = {
            ' ': Keycode.SPACE,
            '!': (Keycode.SHIFT, Keycode.ONE),
            '@': (Keycode.SHIFT, Keycode.TWO),
            '#': (Keycode.SHIFT, Keycode.THREE),
            '$': (Keycode.SHIFT, Keycode.FOUR),
            '%': (Keycode.SHIFT, Keycode.FIVE),
            '^': (Keycode.SHIFT, Keycode.SIX),
            '&': (Keycode.SHIFT, Keycode.SEVEN),
            '*': (Keycode.SHIFT, Keycode.EIGHT),
            '(': (Keycode.SHIFT, Keycode.NINE),
            ')': (Keycode.SHIFT, Keycode.ZERO),
            '-': Keycode.MINUS,
            '_': (Keycode.SHIFT, Keycode.MINUS),
            '=': Keycode.EQUALS,
            '+': (Keycode.SHIFT, Keycode.EQUALS),
            '[': Keycode.LEFT_BRACKET,
            '{': (Keycode.SHIFT, Keycode.LEFT_BRACKET),
            ']': Keycode.RIGHT_BRACKET,
            '}': (Keycode.SHIFT, Keycode.RIGHT_BRACKET),
            '\newline': Keycode.BACKSLASH,
            '|': (Keycode.SHIFT, Keycode.BACKSLASH),
            ';': Keycode.SEMICOLON,
            ':': (Keycode.SHIFT, Keycode.SEMICOLON),
            "'": Keycode.QUOTE,
            '"': (Keycode.SHIFT, Keycode.QUOTE),
            ',': Keycode.COMMA,
            '<': (Keycode.SHIFT, Keycode.COMMA),
            '.': Keycode.PERIOD,
            '>': (Keycode.SHIFT, Keycode.PERIOD),
            '/': Keycode.FORWARD_SLASH,
            '?': (Keycode.SHIFT, Keycode.FORWARD_SLASH)
        }
        if character in char_to_keycode:
            keycode = char_to_keycode[character]
            if isinstance(keycode, tuple):
                keyboard.press(*keycode)
            else:
                keyboard.press(keycode)
            keyboard.release_all()