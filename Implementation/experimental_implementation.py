import numpy as np

# Define cities and their coordinates
cities = {
    "A": (0, 0),
    "B": (1, 3),
    "C": (2, 2),
    "D": (3, 1),
    "E": (4, 4)
}

# Calculate distance between two cities
def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate total distance of a route
def total_distance(route):
    dist = 0
    for i in range(len(route) - 1):
        dist += distance(cities[route[i]], cities[route[i + 1]])
    dist += distance(cities[route[-1]], cities[route[0]])  # Return to the starting city
    return dist

# Initialize population with random permutations of cities with city C as starting position
def initialize_population(population_size, cities):
    population = []
    for _ in range(population_size):
        route = list(cities.keys() - {'C'})
        np.random.shuffle(route)
        route.insert(0, 'C')
        population.append(route)
    return population

# Move butterflies by swapping cities between routes
def move_butterflies_tsp(population, best_solution):
    new_population = []
    for route in population:
        butterfly_route = route.copy()
        for i in range(len(route)):
            if np.random.rand() < 0.5:
                city1, city2 = np.random.choice(len(route), 2, replace=False)
                butterfly_route[city1], butterfly_route[city2] = butterfly_route[city2], butterfly_route[city1]
        new_population.append(butterfly_route)
    return new_population

# Butterfly Optimization Algorithm for TSP
def butterfly_optimization_tsp(population_size, cities, max_iterations):
    population = initialize_population(population_size, cities)
    best_solution = min(population, key=lambda x: total_distance(x))

    for _ in range(max_iterations):
        population = move_butterflies_tsp(population, best_solution)
        new_best_solution = min(population, key=lambda x: total_distance(x))
        if total_distance(new_best_solution) < total_distance(best_solution):
            best_solution = new_best_solution

    return best_solution, total_distance(best_solution)

# Example usage
population_size = 20
max_iterations = 100

best_route, best_distance = butterfly_optimization_tsp(population_size, cities, max_iterations)
print("Best route:", best_route)
print("Best distance:", best_distance)
