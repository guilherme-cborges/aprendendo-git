import pyautogui
import time
import keyboard

print("Auto Clicker - Pressione 'ESC' para parar")
print("Iniciando em 3 segundos...")
time.sleep(3)

print("Clicando a cada 1 segundo. Pressione ESC para parar.")

try:
    while True:
        # Verifica se ESC foi pressionado
        if keyboard.is_pressed('esc'):
            print("\nParado pelo usuário.")
            break
        
        # Clica com o botão esquerdo do mouse
        pyautogui.click()
        
        # Aguarda 1 segundo
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\nO programa foi interrompido.")