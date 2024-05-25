import pyautogui
import json
import time

# Carregar eventos do arquivo JSON
with open('mouse_events.json', 'r') as f:
    mouse_events = json.load(f)

# Pausa antes de iniciar a reprodução
time.sleep(2)

# Reproduza os eventos do mouse
for event in mouse_events:
    event_type = event[0]
    if event_type == 'move':
        x, y = event[1], event[2]
        pyautogui.moveTo(x, y) # duration=0.0)  # Reduzindo a duração para 0.0 segundos
    elif event_type == 'click':
        x, y = event[1], event[2]
        pyautogui.click(x, y) #duration=0.0)  # Reduzindo a duração para 0.0 segundos

print("Reprodução dos eventos do mouse concluída.")
