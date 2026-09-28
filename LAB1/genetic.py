import numpy as np

def objective_function(x):
    return x**2


population_size = 31
num_generations = 50
mutation_rate = 0.1
crossover_rate = 0.7
value_range = (-10, 10)


def initialize_population(size, value_range):
    return np.random.uniform(value_range[0], value_range[1], size)


def evaluate_fitness(population):
    return np.array([objective_function(x) for x in population])


def selection(population, fitness):
    probabilities = fitness / fitness.sum()
    return population[
        np.random.choice(len(population), size=2, p=probabilities)
    ]


def crossover(parent1, parent2):
    if np.random.rand() < crossover_rate:
        return (parent1 + parent2) / 2
    return parent1 if np.random.rand() < 0.5 else parent2


def mutate(individual, mutation_rate, value_range):
    if np.random.rand() < mutation_rate:
        return np.random.uniform(value_range[0], value_range[1])
    return individual


def genetic_algorithm():
    population = initialize_population(population_size, value_range)

    best_solution = None
    best_fitness = -np.inf

    for generation in range(num_generations):
        fitness = evaluate_fitness(population)

        current_best_index = np.argmax(fitness)

        if fitness[current_best_index] > best_fitness:
            best_fitness = fitness[current_best_index]
            best_solution = population[current_best_index]

        new_population = []

        for _ in range(population_size):
            parent1, parent2 = selection(population, fitness)

            offspring = crossover(parent1, parent2)

            offspring = mutate(
                offspring,
                mutation_rate,
                value_range
            )

            new_population.append(offspring)

        population = np.array(new_population)

    return best_solution, best_fitness


best_solution, best_fitness = genetic_algorithm()

print(f"Best solution found: x = {best_solution:.2f}")
print(f"Maximum value of f(x) = x^2: f(x) = {best_fitness:.2f}")
