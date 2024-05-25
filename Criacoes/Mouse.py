from pynput import mouse, keyboard
import json

mouse_events = []
is_running = True

def on_move(x, y):
    if is_running:
        mouse_events.append(('move', x, y))

def on_click(x, y, button, pressed):
    if is_running and pressed:
        mouse_events.append(('click', x, y, button.name))

def on_press(key):
    global is_running
    try:
        if key == keyboard.Key.esc:
            is_running = False
            # Parar os listeners
            return False
    except AttributeError:
        pass

# Inicia os listeners de mouse e teclado
with mouse.Listener(on_move=on_move, on_click=on_click) as mouse_listener, \
     keyboard.Listener(on_press=on_press) as keyboard_listener:
    print("Movimente e clique com o mouse. Pressione 'Esc' para parar.")
    keyboard_listener.join()
    mouse_listener.stop()  # Certifica que o listener de mouse para também

# Salve os eventos em um arquivo JSON
with open('mouse_events.json', 'w') as f:
    json.dump(mouse_events, f)

print("Eventos do mouse gravados e salvos em 'mouse_events.json'.")
