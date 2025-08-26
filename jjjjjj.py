import random
import time
import os

# Configuración
ANCHO = 40
ALTO = 20
NUM_ESTRELLAS = 50
VELOCIDAD = 0.1

# Inicializa las estrellas en posiciones aleatorias
estrellas = [[random.randint(0, ANCHO - 1), random.randint(0, ALTO - 1)] for _ in range(NUM_ESTRELLAS)]

def dibujar(estrellas):
    pantalla = [[' ' for _ in range(ANCHO)] for _ in range(ALTO)]
    for x, y in estrellas:
        if 0 <= y < ALTO:
            pantalla[y][x] = '*'
    os.system('cls' if os.name == 'nt' else 'clear')
    for fila in pantalla:
        print(''.join(fila))

def actualizar(estrellas):
    for estrella in estrellas:
        estrella[1] += 1
        if estrella[1] >= ALTO:
            estrella[0] = random.randint(0, ANCHO - 1)
            estrella[1] = 0

# Bucle principal
try:
    while True:
        dibujar(estrellas)
        actualizar(estrellas)
        time.sleep(VELOCIDAD)
except KeyboardInterrupt:
    print("\nAnimación detenida.")
