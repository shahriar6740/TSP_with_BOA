import numpy as np

class Utilities:
    '''
    Define utility functions for calculating distance between two cities and total distance of a route
    '''

    def __init__(self, cities: list) -> None:
        self.cities = cities
        # self.city1 = city1
        # self.city2 = city2


    def distance(self):
        '''
        calculates the linear distance between two cities using euclidian distance of both city co-ordinates.
        '''
        return np.sqrt((self.city1[0] - self.city2[0]) ** 2 + (self.city1[1] - self.city2[1]) ** 2)

    # Calculate total distance of a route
    def total_distance(self, route) -> int:
        '''
        iterate over each cities in the given route and sums the distance.
        Finally adds the distance from end city to starting city distance to complete the cycle.
        '''

        dist = 0

        for i in range(len(route) - 1):
            from_city = route[i]
            to_city = route[i+1]
            dist += self.cities[from_city][to_city]

        # Return to the starting city
        dist += self.cities[route[-1]][route[0]]
        return dist
