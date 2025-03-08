import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt

def run_frozenlake(is_slippery, episodes=100):
    env = gym.make("FrozenLake-v1", is_slippery=is_slippery)
    rewards = []
    
    for _ in range(episodes):
        obs, info = env.reset()
        done = False
        total_reward = 0
        
        while not done:
            action = env.action_space.sample()  # Selección aleatoria de acción
            obs, reward, done, truncated, info = env.step(action)
            total_reward += reward
        
        rewards.append(total_reward)  # Guardar recompensa total por episodio
    
    env.close()
    return rewards

# Correr simulaciones
episodes = 1000000
rewards_slippery = run_frozenlake(is_slippery=True, episodes=episodes)
rewards_non_slippery = run_frozenlake(is_slippery=False, episodes=episodes)

# Graficar resultados
plt.plot(np.cumsum(rewards_slippery), label="is_slippery=True", alpha=0.7)
plt.plot(np.cumsum(rewards_non_slippery), label="is_slippery=False", alpha=0.7)
plt.xlabel("Episodios")
plt.ylabel("Recompensa acumulada")
plt.title("Comparación de FrozenLake con y sin deslizamiento")
plt.legend()
plt.show()
