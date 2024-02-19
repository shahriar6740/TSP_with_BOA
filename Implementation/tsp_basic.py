# problem using naive approach.

from sys import maxsize 
from itertools import permutations

max_nodes = 5

# implementation of traveling Salesman Problem 
def travelling_salesman_problem(graph, s):
	'''
	Problem Domain:
	----------------
	Given a list of cities and the distances between each pair of cities, what is the
    shortest possible route that visits each city exactly once and returns to the origin city


	Implementation Strategy:
	------------------------
	1. Consider city 1 as the starting and ending point. Since the route is cyclic, we can consider any point as a starting point.
    2. Generate all (n-1)! permutations of cities.
    3. Calculate the cost of every permutation and keep track of the minimum cost permutation.
    4. Return the permutation with minimum cost.
	'''

	# store all vertex apart from source vertex 
	vertex = []
	
	for node in range(max_nodes): 
		if node != s: 
			vertex.append(node)
			
	# print(f"vertex list: {vertex}")

	# store minimum weight Hamiltonian Cycle 
	min_path = maxsize 
	next_permutation=permutations(vertex)


	for i in next_permutation:
		
		print(f"current permutation: {i}")

		# store current Path weight(cost) 
		current_pathweight = 0

		# compute current path weight 
		k = s

		
        # now we are iterating over the tuple of each permutation.
		for j in i: 
			current_pathweight += graph[k][j] 
			k = j
			
		current_pathweight += graph[k][s]
		
		print(current_pathweight)

		# update minimum 
		min_path = min(min_path, current_pathweight)
		
		
	return min_path 


# Driver Code 
if __name__ == "__main__": 

	# matrix representation of graph 
    graph = [
		        [0, 12, 10, 19, 8],
		        [12, 0, 3, 7, 2],
		        [10, 3, 0, 6, 20],
		        [19, 7, 6, 0, 4],
		        [8, 3, 20, 2, 0]
			]
	
    SOURCE = 0
	
    print(travelling_salesman_problem(graph, SOURCE))
	
