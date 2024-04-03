import numpy as np
class Butterfly:

    def initialize_population(self, population_size, cities, source):
        population = []
        for _ in range(population_size):
            city_list = list(range(len(cities)))

            city_list.remove(source)
            route = city_list

            np.random.shuffle(route)
            # print(route)
            route.insert(0, source)
            population.append(tuple(route))

        print(f"Number of Population permutation list: {len(population)}")

        print(f"Number of Unique Population permutation:{len({s for s in population})}")

        print(f"Unique Population permutations:{list({s for s in population})}")

        return list({s for s in population})
    

    def move_butterflies_global_tsp(self, population):
        new_population = []
        for route in population:

            butterfly_route = list(route).copy()
            for i in range(len(route)):
                if np.random.rand() < 0.5:
                    city1, city2 = np.random.choice(len(route), 2, replace=False)
                    
                    butterfly_route[city1], butterfly_route[city2] = butterfly_route[city2], butterfly_route[city1]
            new_population.append(butterfly_route)

        return new_population
