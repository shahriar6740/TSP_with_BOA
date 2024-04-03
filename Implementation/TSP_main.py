import numpy as np
from utilities import Utilities
from constants import Constants
from butterfly import Butterfly

cities = Constants.FIVE_CITIES
source = Constants.SOURCE
search_agent = Constants.POPULATION_SIZE
iterations = Constants.MAX_ITERATION

BOA = Butterfly()
util = Utilities(cities)

def TSP_with_BOA(population_size, cities, max_iterations):
    population = BOA.initialize_population(population_size, cities, source=source)
    best_solution = min(population, key=lambda x: util.total_distance(x))

    for _ in range(max_iterations):
        population = BOA.move_butterflies_global_tsp(population)
        new_best_solution = min(population, key=lambda x: util.total_distance(x))

        if util.total_distance(new_best_solution) < util.total_distance(best_solution):
            best_solution = new_best_solution


    return best_solution, util.total_distance(best_solution)


if __name__ == "__main__":

    best_route, best_distance = TSP_with_BOA(population_size=search_agent, cities=cities, max_iterations=iterations)

    #append the source node at the end for showing circular tsp path.
    best_path = list(best_route)
    best_path.append(source)

    print(f"Best Path index:{best_path}")
    print("Best distance:", best_distance)

