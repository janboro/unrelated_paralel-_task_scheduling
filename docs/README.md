# Prerequisites
Before you are able to run this program you first need to install `Bazel` (tested on version 5.0.0.)

# Choosing an algorithm
You have the choice to choose between:
    - Simulated annealing (SA)
    - Particle Swarm Optimization (PSO) (With or without Local Search)
    - Shortest Release Date (SRD)

To use one of those algorithm you need to run them by the: `bazel run //runners:run_[pso/sa/srd]`
You can also compare the given results of every algorithm by using: `bazel run //runners:run_all`

To configure specific parameters for those algorithms head to their appropriate files in the `runners` directory.

# Definining your problem
In order to solve your specific problem, define the:
    - Number of machines
    - Job release dates
    - Jobs processing times
in the `task_generatro/task_scheduling_generator.py` file.

IF you DON'T specify any problem, the program will generate a random problem based on the parameters found in the `config/parameters.yaml` file.
