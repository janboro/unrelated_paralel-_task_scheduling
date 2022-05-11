import matplotlib.pyplot as plt
from task_generator.task_scheduling_generator import UnrelatedParallelMachineSchedulingGenerator
from algorithms.particle_swarm_optimization import PSO
from data_type.PSO_params import PSOParams




def main():
    pso_params = PSOParams(iterations=300, swarm_size=50, R1_probability=0.5, R2_probability=0.5)
    scheduling_problem = UnrelatedParallelMachineSchedulingGenerator()

    pso = PSO(scheduling_problem=scheduling_problem, pso_params=pso_params)
    best_solution = pso.run()
    print(f"Best solution: {best_solution}")
    plt.plot(pso.best_costs)
    plt.show()
    plt.semilogy(pso.best_costs)
    plt.show()


if __name__ == "__main__":
    main()

# Cost1:254
# Cost2:174
