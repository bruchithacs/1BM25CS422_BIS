import numpy as np

# Employees
employees = ["A", "B", "C", "D"]

# Number of employees
population_size = 10

# Number of generations
num_generations = 20

# Probability of mutation
mutation_rate = 0.1

# Probability of crossover
crossover_rate = 0.7


# Create a random schedule
def create_schedule():
    return np.random.permutation(4)


# Create initial population
def initialize_population():
    population = []

    for _ in range(population_size):
        population.append(create_schedule())

    return population


# Calculate fitness
def calculate_fitness(schedule):
    # Each different shift is considered a valid schedule
    # So a schedule with no duplicate shifts gets fitness 1
    if len(set(schedule)) == 4:
        return 1
    else:
        return 0


# Selection
def selection(population, fitness):
    probabilities = np.array(fitness) + 0.01
    probabilities = probabilities / probabilities.sum()

    indexes = np.random.choice(
        len(population),
        size=2,
        p=probabilities
    )

    return population[indexes[0]], population[indexes[1]]


# Crossover
def crossover(parent1, parent2):

    if np.random.rand() < crossover_rate:

        point = np.random.randint(1, 4)

        child = list(parent1[:point])

        for shift in parent2:
            if shift not in child:
                child.append(shift)

        return np.array(child)

    return parent1.copy()


# Mutation
def mutate(schedule):

    if np.random.rand() < mutation_rate:

        i, j = np.random.choice(4, 2, replace=False)

        schedule[i], schedule[j] = schedule[j], schedule[i]

    return schedule


# Genetic Algorithm
def genetic_algorithm():

    population = initialize_population()

    for generation in range(num_generations):

        fitness = [
            calculate_fitness(schedule)
            for schedule in population
        ]

        new_population = []

        for _ in range(population_size):

            parent1, parent2 = selection(population, fitness)

            child = crossover(parent1, parent2)

            child = mutate(child)

            new_population.append(child)

        population = new_population

    # Find best schedule
    fitness = [
        calculate_fitness(schedule)
        for schedule in population
    ]

    best_index = np.argmax(fitness)

    return population[best_index]


# Run the algorithm
best_schedule = genetic_algorithm()

# Display result
print("Best Employee Shift Schedule:")

shifts = ["Morning", "Afternoon", "Evening", "Night"]

for i in range(4):
    print(employees[i], "->", shifts[best_schedule[i]])
