# utils.py
import time

def smooth_transition_to_10_percent(backlight):
    current_duty_cycle = backlight.duty_cycle
    target_duty_cycle = 2000  # 10% de 65535
    step = 1000  # Tamaño del paso para ajustar el brillo

    if current_duty_cycle > target_duty_cycle:
        # Decrementar gradualmente hasta el 10%
        while current_duty_cycle > target_duty_cycle:
            current_duty_cycle -= step
            if current_duty_cycle < target_duty_cycle:
                current_duty_cycle = target_duty_cycle
            backlight.duty_cycle = current_duty_cycle
            time.sleep(0.005)  # Retardo para suavizar la transición
    else:
        # Incrementar gradualmente hasta el 10%
        while current_duty_cycle < target_duty_cycle:
            current_duty_cycle += step
            if current_duty_cycle > target_duty_cycle:
                current_duty_cycle = target_duty_cycle
            backlight.duty_cycle = current_duty_cycle
            #time.sleep(0.01)  # Retardo para suavizar la transición



# menu_management.py

def is_long_press(button, threshold=0.3):
    start_time = time.monotonic()
    while not button.value:
        if time.monotonic() - start_time > threshold:
            return True
    return False