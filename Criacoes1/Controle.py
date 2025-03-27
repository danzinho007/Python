import pyautogui
import time

# Captura o tempo de início
start_time = time.time()

# Espera inicial
time.sleep(5)
# Execução dos comandos
pyautogui.press('z')
time.sleep(0.05)
pyautogui.press('z')
time.sleep(0.05)
pyautogui.press('x')
time.sleep(0.5)
pyautogui.press('q')
time.sleep(0.05)
pyautogui.press('z')

# Captura o tempo de término
end_time = time.time()

# Calcula e imprime o tempo total
total_time = end_time - start_time
print(f"Tempo total de execução: {total_time:.4f} segundos")

# zzxqz 6.2438 
# zzxqz 6.2582
# zxqz 6.0137
# zxqz 6.1879
