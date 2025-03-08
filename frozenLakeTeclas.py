import gymnasium as gym
import pygame
from gymnasium.envs.toy_text.frozen_lake import LEFT, DOWN, RIGHT, UP

# Inicializar FrozenLake
env = gym.make("FrozenLake-v1", render_mode="human", is_slippery=False)
env.reset()

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((250, 250))
pygame.display.set_caption("FrozenLake con Pygame")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                action = LEFT
            elif event.key == pygame.K_RIGHT:
                action = RIGHT
            elif event.key == pygame.K_UP:
                action = UP
            elif event.key == pygame.K_DOWN:
                action = DOWN
            else:
                continue  # Ignora otras teclas

            # Realizar la acción en el entorno
            state, reward, done, _, _ = env.step(action)
            
            # Mostrar si el juego terminó
            if done:
                print("¡Juego terminado! Recompensa:", reward)
                env.reset()  # Reiniciar juego

env.close()
pygame.quit()
