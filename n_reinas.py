# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 17:46:34 2025

@author: Edison
"""

import random
import numpy as np
import matplotlib.pyplot as plt

# Función de aptitud: cuenta conflictos diagonales
def fitness(individual):
    conflicts = 0
    n = len(individual)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(i - j) == abs(individual[i] - individual[j]):
                conflicts += 1
    return conflicts

# Generar un individuo aleatorio
def create_individual(n):
    return random.sample(range(n), n)  # Permutación válida

# Generar población inicial
def create_population(size, n):
    return [create_individual(n) for _ in range(size)]

#Selección por ruleta para mejorar la diversidad genética.
def roulette_wheel_selection(population):
    fitness_values = np.array([1 / (1 + fitness(ind)) for ind in population])
    probabilities = fitness_values / fitness_values.sum()
    return population[np.random.choice(len(population), p=probabilities)]

#Cruce de orden (OX) para mantener permutaciones válidas.
def ordered_crossover(parent1, parent2):
    n = len(parent1)
    start, end = sorted(random.sample(range(n), 2))
    child = [-1] * n
    child[start:end] = parent1[start:end]
    pos = end
    for gene in parent2:
        if gene not in child:
            while child[pos % n] != -1:
                pos += 1
            child[pos % n] = gene
    return child

#Mutación adaptativa, donde la tasa de mutación disminuye con el tiempo.
def mutate(individual, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(individual)), 2)
        individual[i], individual[j] = individual[j], individual[i]  # Swap mutation
    return individual

def evolutionary_algorithm(n, population_size, mutation_rate, max_generations=1000):
    population = create_population(population_size, n)
    generation = 0
    
    while generation < max_generations:
        best = min(population, key=fitness)
        if fitness(best) == 0:
            return best, generation
        
        new_population = []
        for _ in range(population_size // 2):
            parent1 = roulette_wheel_selection(population)
            parent2 = roulette_wheel_selection(population)
            child1 = ordered_crossover(parent1, parent2)
            child2 = ordered_crossover(parent2, parent1)
            
            mutation_rate = max(0.01, mutation_rate * 0.99)  # Disminuye con el tiempo
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            
            new_population.extend([child1, child2])
        
        population = new_population
        generation += 1
    
    return min(population, key=fitness), generation

# Prueba
n = 8
population_size = 1000
mutation_rate = 0.1
solution, generations = evolutionary_algorithm(n, population_size, mutation_rate)
print(f"Solución para N={n}: {solution}")
print(f"Generaciones: {generations}")
print(f"Conflictos: {fitness(solution)}")

def plot_board(solution):
    n = len(solution)
    fig, ax = plt.subplots()
    # Dibujar el tablero
    for row in range(n):
        for col in range(n):
            color = 'white' if (row + col) % 2 == 0 else 'gray'
            rect = plt.Rectangle((col, n - row - 1), 1, 1, facecolor=color)
            ax.add_patch(rect)
    
    # Dibujar las reinas
    for col, row in enumerate(solution):
        ax.text(col + 0.5, n - row - 1 + 0.5, '♛', ha='center', va='center', fontsize=20, color='red')

    # Ajustes del gráfico
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')
    plt.title(f"Tablero de {n} Reinas")
    plt.show()
    
plot_board(solution)
