# key_config.py

from adafruit_hid.keycode import Keycode

# Definimos un modificador ficticio para indicar que no se usa modificador
NO_MODIFIER = None

# Acciones de teclas para cada programa
key_actions = {
    "Office": [
        ("CONTROL", Keycode.C),  # Copiar
        ("CONTROL", Keycode.V),  # Pegar
        ("CONTROL", Keycode.X),  # Cortar
        ("CONTROL", Keycode.Z),  # Deshacer
        ("CONTROL", Keycode.S),  # Guardar
        ("CONTROL", Keycode.A),  # Seleccionar todo
        ("CONTROL", Keycode.F),  # Buscar
        ("CONTROL", Keycode.G),  # Agrupar
        ("CONTROL", Keycode.P),  # Imprimir
        ("CONTROL", Keycode.W),  # Cerrar
    ],
    "Illustrator": [
        ("CONTROL", Keycode.N),  # Nuevo
        ("CONTROL", Keycode.O),  # Abrir
        ("CONTROL", Keycode.P),  # Imprimir
        ("CONTROL", Keycode.W),  # Cerrar
        ("CONTROL", Keycode.A),  # Seleccionar todo
        ("CONTROL", Keycode.D),  # Duplicar
        ("CONTROL", Keycode.F),  # Buscar
        ("CONTROL", Keycode.G),  # Agrupar
        ("CONTROL", Keycode.S),  # Guardar
        ("CONTROL", Keycode.L),  # Bloquear
    ],
    "InDesign": [
        ("CONTROL", Keycode.A),  # Seleccionar todo
        ("CONTROL", Keycode.D),  # Duplicar
        ("CONTROL", Keycode.F),  # Buscar
        ("CONTROL", Keycode.G),  # Agrupar
        ("CONTROL", Keycode.S),  # Guardar
        ("CONTROL", Keycode.L),  # Bloquear
        ("CONTROL", Keycode.T),  # Transformar
        ("CONTROL", Keycode.U),  # Saturación
        ("CONTROL", Keycode.B),  # Balance de color
        ("CONTROL", Keycode.E),  # Fusionar capas
    ],
    "Photoshop": [
        ("CONTROL", Keycode.T),  # Transformar
        ("CONTROL", Keycode.U),  # Saturación
        ("CONTROL", Keycode.B),  # Balance de color
        ("CONTROL", Keycode.E),  # Fusionar capas
        ("CONTROL", Keycode.S),  # Guardar
        ("CONTROL", Keycode.L),  # Bloquear
        ("CONTROL", Keycode.R),  # Revelar
        ("CONTROL", Keycode.K),  # Cortar
        ("CONTROL", Keycode.M),  # Marcar
        ("CONTROL", Keycode.I),  # Importar
    ],
    "Premiere": [
        (NO_MODIFIER, Keycode.SPACEBAR ),  # Importar
        ("CONTROL", Keycode.E),  # Exportar
        ("CONTROL", Keycode.M),  # Marcar
        ("CONTROL", Keycode.K),  # Cortar
        ("CONTROL", Keycode.S),  # Guardar
        ("CONTROL", Keycode.L),  # Bloquear
        ("CONTROL", Keycode.R),  # Revelar
        ("CONTROL", Keycode.T),  # Transformar
        (NO_MODIFIER, Keycode.SPACEBAR),  # Espacio
        ("CONTROL", Keycode.B),  # Balance de color
    ],
    "LigthRoom": [
        ("CONTROL", Keycode.R),  # Revelar
        ("CONTROL", Keycode.L),  # Biblioteca
        ("CONTROL", Keycode.Y),  # Sincronizar
        ("CONTROL", Keycode.J),  # Información
        ("CONTROL", Keycode.S),  # Guardar
        ("CONTROL", Keycode.A),  # Seleccionar todo
        ("CONTROL", Keycode.D),  # Duplicar
        ("CONTROL", Keycode.F),  # Buscar
        ("CONTROL", Keycode.G),  # Agrupar
        ("CONTROL", Keycode.P),  # Imprimir
    ],
    "AfterEffects": [
        ("CONTROL", Keycode.N),  # Nuevo proyecto
        ("CONTROL", Keycode.K),  # Composición
        ("CONTROL", Keycode.R),  # Renderizar
        ("CONTROL", Keycode.M),  # Agregar a cola de render
        ("CONTROL", Keycode.S),  # Guardar
        ("CONTROL", Keycode.L),  # Bloquear
        ("CONTROL", Keycode.T),  # Transformar
        ("CONTROL", Keycode.U),  # Saturación
        ("CONTROL", Keycode.B),  # Balance de color
        ("CONTROL", Keycode.E),  # Fusionar capas
    ],
}