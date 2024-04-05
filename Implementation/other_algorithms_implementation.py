import time

# Calculate total distance of a route
def total_distance(route, cities):
    return sum(cities[route[i - 1]][route[i]] for i in range(len(route)))

# Nearest Neighbor Heuristic for TSP
def nearest_neighbor_tsp(distances):
    current_city = 0
    route = [current_city]
    unvisited_cities = set(range(1, len(distances)))

    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda city: distances[current_city][city])
        unvisited_cities.remove(next_city)
        route.append(next_city)
        current_city = next_city

    return route

# Nearest Insertion Algorithm for TSP
def nearest_insertion_tsp(distances):
    current_city = 0
    route = [current_city]
    unvisited_cities = set(range(1, len(distances)))

    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda city: min(distances[city][i] for i in route))
        unvisited_cities.remove(next_city)

        insertion_index = min(route, key=lambda i: distances[i][next_city])
        route.insert(route.index(insertion_index) + 1, next_city)

    return route

# Cheapest Insertion Algorithm for TSP
def cheapest_insertion_tsp(distances):
    current_city = 0
    route = [current_city]
    unvisited_cities = set(range(1, len(distances)))

    while unvisited_cities:
        next_city, insertion_index = min(
            ((city, i) for city in unvisited_cities for i in range(len(route))),
            key=lambda x: distances[route[x[1]-1]][x[0]] + distances[x[0]][route[(x[1]+1)%len(route)]] - distances[route[x[1]-1]][route[(x[1]+1)%len(route)]]
        )
        unvisited_cities.remove(next_city)
        route.insert(insertion_index, next_city)

    return route

def run_algorithm(algorithm, algorithm_name, cities, city_dict):
    start_time = time.time()
    route = algorithm(cities)
    execution_time = time.time() - start_time

    best_route = [city_dict[city_key] for city_key in route]
    best_distance = total_distance(route, cities)

    print(f"{algorithm_name} - Best route:", best_route)
    print(f"{algorithm_name} - Best distance:", best_distance)
    print(f"{algorithm_name} - Execution time:", execution_time, "seconds")

def main():
#    ----- For 5 cities from report --------
    cities = [
        [0, 12, 10, 19, 8],
        [12, 0, 3, 7, 2],
        [10, 3, 0, 6, 20],
        [19, 7, 6, 0, 4],
        [8, 3, 20, 2, 0]
    ]
    city_keys = list(range(len(cities)))
    city_values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'BB', 'CC', 'DD']
    city_dict = dict(zip(city_keys,city_values))

    run_algorithm(nearest_neighbor_tsp, "Nearest Neighbor Heuristic", cities, city_dict)
    run_algorithm(nearest_insertion_tsp, "Nearest Insertion Algorithm", cities, city_dict)
    run_algorithm(cheapest_insertion_tsp, "Cheapest Insertion Algorithm", cities, city_dict)

if __name__ == "__main__":
    main()