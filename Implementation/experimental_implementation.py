import numpy as np

# Define cities and their coordinates


# ----- For 5 cities from report --------
cities = [
    [0, 12, 10, 19, 8],
    [12, 0, 3, 7, 2],
    [10, 3, 0, 6, 20],
    [19, 7, 6, 0, 4],
    [8, 3, 20, 2, 0]
]

# ----- For 4 cities --------
# cities = [
#     [0, 12, 10, 19],
#     [12, 0, 3, 7],
#     [10, 3, 0, 6],
#     [19, 7, 6, 0]
# ]


# ------ for 6 cities example from report ---------
# cities = [
#     [0, 12, 29, 22, 13, 24],
#     [12, 0, 19, 3, 25, 6],
#     [29, 19, 0, 21, 23, 28],
#     [22, 3, 21, 0, 4, 5],
#     [13, 25, 23, 4, 0, 16],
#     [24, 6, 28, 5, 16, 0]
# ]


SOURCE = 0


# Calculate distance between two cities
def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


# Calculate total distance of a route
def total_distance(route):
    dist = 0

    for i in range(len(route) - 1):
        from_city = route[i]
        to_city = route[i+1]
        dist += cities[from_city][to_city]

    # Return to the starting city
    dist += cities[route[-1]][route[0]]  
    return dist

# Initialize population with random permutations of cities with city C as starting position
def initialize_population(population_size, cities):
    population = []
    for _ in range(population_size):
        city_list = list(range(len(cities)))

        city_list.remove(SOURCE)
        route = city_list

        np.random.shuffle(route)
        # print(route)
        route.insert(0, SOURCE)
        population.append(tuple(route))

    print(f"Population permutation list: {len(population)}")

    print(f"Population permutation set:{len({s for s in population})}")

    return list({s for s in population})

# Move butterflies by swapping cities between routes
def move_butterflies_tsp(population, best_solution):
    new_population = []
    for route in population:

        butterfly_route = list(route).copy()
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

    print(f"Best Path index:{best_solution}")

    return best_solution, total_distance(best_solution)



city_keys = list(range(len(cities)))
city_values = ['A','B', 'C', 'D', 'E', 'F']
city_dict = dict(zip(city_keys,city_values))
print(city_dict)

# Example usage
population_size = 20
max_iterations = 100
# print(f"check: {cities[0][4]+cities[4][3]+ cities[3][1] + cities[1][2] + cities[2][0]}")


# print(f"check: {distance(cities['C'],cities['A']) + distance(cities['A'],cities['B']) + distance(cities['B'],cities['C']) }")
best_route, best_distance = butterfly_optimization_tsp(population_size, cities, max_iterations)
print("Best route:", [city_dict[city_key] for city_key in best_route])
print("Best distance:", best_distance)
