import time

tempo = 1*60

while tempo >= 0:
    minutos = tempo // 60
    segundos = tempo % 60

    print(f"{minutos:02d}:{segundos:02d}")

    time.sleep(1)

    tempo -= 1

print("Contagem concluida")