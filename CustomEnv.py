from gymnasium import Env, spaces
import numpy as np

class CustomEnv(Env):
    def __init__(self):
        super().__init__()
        self.observation_space = spaces.Discrete(20)  # 20 estados en lugar de 10
        self.action_space = spaces.Discrete(2)
        self.state = 0

    def reset(self, seed=None, options=None):
        self.state = 0
        return self.state, {}

    def step(self, action):
        self.state = min(self.state + action, 19)  # Último estado es 19 en lugar de 9
        reward = 1  # Recompensa base por cada paso
        if self.state == 19:
            reward += 10  # Bono adicional al llegar al último estado
        done = self.state == 19
        return self.state, reward, done, False, {}

    def render(self):
        print(f"Estado actual: {self.state}")

env = CustomEnv()

for _ in range(20):
     obs, info = env.reset()
     done = False
     pasos = 0
     recompensa = 0
     while not done:
          action = env.action_space.sample()
          obs, reward, done, truncated, info = env.step(action)
          # env.render()
          pasos += 1
          recompensa += reward
     print(f"Simulación {_ + 1}:")
     print(f"\tTotal de pasos: {pasos}, recompensa total: {recompensa}")

print("Espacio de observación:", env.observation_space)
print("Espacio de acción:", env.action_space)

env.close()
