import pygame
import gymnasium as gym
from gymnasium import spaces

# Configuración de pantalla
RADIUS_STEP = 10  # Radio de cada anillo
MAX_RADIUS = RADIUS_STEP * 20  # Radio del anillo más externo
CENTER = (MAX_RADIUS, MAX_RADIUS)

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

class CustomEnv(gym.Env):
    def __init__(self):
        super().__init__()
        self.observation_space = spaces.Discrete(20)  # 20 estados (anillos)
        self.action_space = spaces.Discrete(2)  # Avanzar o quedarse
        self.state = 0

    def reset(self, seed=None, options=None):
        self.state = 0
        return self.state, {}

    def step(self, action):
        self.state = min(self.state + action, 19)  # Avanza hasta el estado 19
        reward = 1 if self.state < 19 else 11  # Bono si llega al último anillo
        done = self.state == 19
        return self.state, reward, done, False, {}

    def render(self):
        pass  # No imprime texto porque usamos Pygame


def draw_donuts(screen, agent_pos):
    screen.fill(WHITE)
    for i in range(19, 0, -1):
        outer_radius = (i + 1) * RADIUS_STEP
        color = BLUE
        if i == agent_pos:
            if i == 19:
                color = GREEN
            else:
                color = RED
        pygame.draw.circle(screen, color, CENTER, outer_radius)
        pygame.draw.circle(screen, BLACK, CENTER, outer_radius, 1)
    pygame.draw.circle(screen, WHITE, CENTER, RADIUS_STEP)  # Agujero central
    pygame.display.flip()


# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((MAX_RADIUS * 2, MAX_RADIUS * 2))
pygame.display.set_caption("CustomEnv con Donas")
clock = pygame.time.Clock()

# Crear entorno
env = CustomEnv()
state, _ = env.reset()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Acción aleatoria (puedes cambiar esto por control del usuario)
    action = env.action_space.sample()
    state, reward, done, _, _ = env.step(action)
    
    # Dibujar el entorno
    draw_donuts(screen, state)
    
    if done:
        pygame.time.wait(2000)  # Espera al llegar al último anillo
        state, _ = env.reset()  # Reinicia el juego

    clock.tick(2)  # Control de velocidad (2 FPS)

pygame.quit()
