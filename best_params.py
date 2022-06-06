# SRD cost = 110
# SA
processing_time=22.49410581588745 temperature=0.9999999999999999 cooling_rate=0.8899999999999999 best_solution=BestSolution(position=[2, 12, 17, 9, 13, '*', 24, 15, 23, 7, '*', 30, 27, 28, 11, 6, '*', 25, 10, 21, 14, 31, 29, '*', 22, 20, 1, '*', 19, 16, 26, 0, 18, '*', 8, 5, 3, 4], cost=50.0) iterations=5000

# PSO
Params: iterations=200 swarm_size=30
 random_first_solution=False initialize_method='shuffle' reverse_subtraction=False multiplication_operator='regular' fill_velocity_randomly=False R_probability=Probability(distribution='bernoulli', R1=0.9, R2=0.1, R1_dampening=0.0, R2_dampening=0.0) local_search=LocalSearch(end_with_local_search=True, iterations=10), cost: 97.0


 Params: iterations=24 swarm_size=30 random_first_solution=True initialize_method='random' reverse_subtraction=True fill_velocity_randomly=False R_probability=Probability(distribution='bernoulli', R1=0.1, R2=0.1, R1_dampening=0.8, R2_dampening=0.8) local_search=LocalSearch(end_with_local_search=False, iterations=0), cost: 141.0
 Params: iterations=24 swarm_size=30 random_first_solution=True initialize_method='random' reverse_subtraction=True fill_velocity_randomly=False R_probability=Probability(distribution='bernoulli', R1=0.7000000000000001, R2=0.8, R1_dampening=0.2, R2_dampening=0.2) local_search=LocalSearch(end_with_local_search=False, iterations=0), cost: 137.0Reached limit time in iteration 21