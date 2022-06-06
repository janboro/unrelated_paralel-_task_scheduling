import pandas as pd
import numpy as np
from data_type.algorithm_test_results import AlgorithmTestResults
from scipy.stats import wilcoxon

# SRD = AlgorithmTestResults(
#     computing_times=[0.021542787551879883],
#     iterations=[1],
#     costs=[162.0, 162.0, 162.0, 162.0, 162.0],
#     best_cost=162.0,
#     worst_cost=162.0,
#     mean=162.0,
#     std=0.0,
# )

# # small_problem
# SA = AlgorithmTestResults(
#     computing_times=[12.77, 10.95, 12.33, 18.61, 14.80],
#     iterations=[5000, 5000, 5000, 5000, 5000],
#     costs=[68.0, 62.0, 61.0, 60.0, 68.0],
# )
# SA.mean = np.mean(SA.costs)
# SA.std = np.std(SA.costs)
# SA.best_cost = np.min(SA.costs)
# SA.worst_cost = np.max(SA.costs)

# PSO_LIT = AlgorithmTestResults(
#     computing_times=[180.38, 180.76, 180.59, 181.25, 180.83],
#     iterations=[131, 131, 140, 164, 165],
#     costs=[77.0, 77.0, 79.0, 72.0, 71.0],
# )
# PSO_LIT.mean = np.mean(PSO_LIT.costs)
# PSO_LIT.std = np.std(PSO_LIT.costs)
# PSO_LIT.best_cost = np.min(PSO_LIT.costs)
# PSO_LIT.worst_cost = np.max(PSO_LIT.costs)

# PSO_LIT_LS = AlgorithmTestResults(
#     computing_times=[181.77, 180.31, 183.48, 180.93, 180.91],
#     iterations=[54, 55, 53, 55, 49],
#     costs=[74.0, 82.0, 71.0, 74.0, 73.0],
# )
# PSO_LIT_LS.mean = np.mean(PSO_LIT_LS.costs)
# PSO_LIT_LS.std = np.std(PSO_LIT_LS.costs)
# PSO_LIT_LS.best_cost = np.min(PSO_LIT_LS.costs)
# PSO_LIT_LS.worst_cost = np.max(PSO_LIT_LS.costs)

# PSO_RAND = AlgorithmTestResults(
#     computing_times=[180.35, 180.55, 180.38, 180.29, 180.32],
#     iterations=[456, 472, 477, 450, 447],
#     costs=[88.0, 86.0, 86.0, 90.0, 94.0],
# )
# PSO_RAND.mean = np.mean(PSO_RAND.costs)
# PSO_RAND.std = np.std(PSO_RAND.costs)
# PSO_RAND.best_cost = np.min(PSO_RAND.costs)
# PSO_RAND.worst_cost = np.max(PSO_RAND.costs)

# PSO_BERN_RF = AlgorithmTestResults(
#     computing_times=[180.57, 180.39, 180.51, 180.26, 180.54],
#     iterations=[482, 465, 451, 456, 497],
#     costs=[83.0, 81.0, 82.0, 73.0, 83.0],
# )
# PSO_BERN_RF.mean = np.mean(PSO_BERN_RF.costs)
# PSO_BERN_RF.std = np.std(PSO_BERN_RF.costs)
# PSO_BERN_RF.best_cost = np.min(PSO_BERN_RF.costs)
# PSO_BERN_RF.worst_cost = np.max(PSO_BERN_RF.costs)

# PSO_BERN_SRDF = AlgorithmTestResults(
#     computing_times=[180.32, 180.50, 180.21, 180.49, 180.34],
#     iterations=[88, 86, 79, 83, 87],
#     costs=[75.0, 68.0, 66.0, 73.0, 65.0],
# )
# PSO_BERN_SRDF.mean = np.mean(PSO_BERN_SRDF.costs)
# PSO_BERN_SRDF.std = np.std(PSO_BERN_SRDF.costs)
# PSO_BERN_SRDF.best_cost = np.min(PSO_BERN_SRDF.costs)
# PSO_BERN_SRDF.worst_cost = np.max(PSO_BERN_SRDF.costs)

# PSO_BERN_SRDF_LS = AlgorithmTestResults(
#     computing_times=[180.50, 181.64, 180.93, 181.57, 181.52],
#     iterations=[88, 86, 79, 83, 87],
#     costs=[66.0, 65.0, 66.0, 66.0, 67.0],
# )
# PSO_BERN_SRDF_LS.mean = np.mean(PSO_BERN_SRDF_LS.costs)
# PSO_BERN_SRDF_LS.std = np.std(PSO_BERN_SRDF_LS.costs)
# PSO_BERN_SRDF_LS.best_cost = np.min(PSO_BERN_SRDF_LS.costs)
# PSO_BERN_SRDF_LS.worst_cost = np.max(PSO_BERN_SRDF_LS.costs)


# # Medium problems ========================
# SRD = AlgorithmTestResults(
#     computing_times=[0.085],
#     iterations=[1],
#     costs=[188.0, 188.0, 188.0, 188.0, 188.0],
#     mean=0.085,
#     std=0.0,
# )

# SA = AlgorithmTestResults(
#     computing_times=[34.09, 33.27, 32.87, 31.72, 31.52],
#     iterations=[5000, 5000, 5000, 5000, 5000],
#     costs=[87.0, 83.0, 76.0, 75.0, 90.0],
# )
# SA.mean = np.mean(SA.costs)
# SA.std = np.std(SA.costs)
# SA.best_cost = np.min(SA.costs)
# SA.worst_cost = np.max(SA.costs)

# PSO_LIT = AlgorithmTestResults(
#     computing_times=[180.85, 182.71, 180.61, 184.38, 182.04],
#     iterations=[47, 47, 45, 43, 43],
#     costs=[173.0, 181.0, 170.0, 175.0, 171.0],
# )
# PSO_LIT.mean = np.mean(PSO_LIT.costs)
# PSO_LIT.std = np.std(PSO_LIT.costs)
# PSO_LIT.best_cost = np.min(PSO_LIT.costs)
# PSO_LIT.worst_cost = np.max(PSO_LIT.costs)

# PSO_LIT_LS = AlgorithmTestResults(
#     computing_times=[190.73, 185.85, 186.49, 193.80, 183.12],
#     iterations=[16, 16, 16, 16, 15],
#     costs=[162.0, 160.0, 159.0, 152.0, 151.0],
# )
# PSO_LIT_LS.mean = np.mean(PSO_LIT_LS.costs)
# PSO_LIT_LS.std = np.std(PSO_LIT_LS.costs)
# PSO_LIT_LS.best_cost = np.min(PSO_LIT_LS.costs)
# PSO_LIT_LS.worst_cost = np.max(PSO_LIT_LS.costs)

# PSO_RAND = AlgorithmTestResults(
#     computing_times=[181.35, 181.43, 180.74, 180.73, 181.12],
#     iterations=[163, 159, 164, 172, 165],
#     costs=[190.0, 190.0, 203.0, 202.0, 203.0],
# )
# PSO_RAND.mean = np.mean(PSO_RAND.costs)
# PSO_RAND.std = np.std(PSO_RAND.costs)
# PSO_RAND.best_cost = np.min(PSO_RAND.costs)
# PSO_RAND.worst_cost = np.max(PSO_RAND.costs)

# PSO_BERN_RF = AlgorithmTestResults(
#     computing_times=[180.94, 180.71, 181.17, 180.84, 180.93],
#     iterations=[162, 155, 156, 179, 197],
#     costs=[206.0, 196.0, 200.0, 205.0, 186.0],
# )
# PSO_BERN_RF.mean = np.mean(PSO_BERN_RF.costs)
# PSO_BERN_RF.std = np.std(PSO_BERN_RF.costs)
# PSO_BERN_RF.best_cost = np.min(PSO_BERN_RF.costs)
# PSO_BERN_RF.worst_cost = np.max(PSO_BERN_RF.costs)

# PSO_BERN_SRDF = AlgorithmTestResults(
#     computing_times=[181.08, 180.62, 181.04, 181.18, 180.88],
#     iterations=[197, 196, 196, 196, 195],
#     costs=[173.0, 186.0, 173.0, 176.0, 175.0],
# )
# PSO_BERN_SRDF.mean = np.mean(PSO_BERN_SRDF.costs)
# PSO_BERN_SRDF.std = np.std(PSO_BERN_SRDF.costs)
# PSO_BERN_SRDF.best_cost = np.min(PSO_BERN_SRDF.costs)
# PSO_BERN_SRDF.worst_cost = np.max(PSO_BERN_SRDF.costs)

# PSO_BERN_SRDF_LS = AlgorithmTestResults(
#     computing_times=[182.74, 183.39, 182.28, 182.21, 184.73],
#     iterations=[39, 39, 39, 38, 37],
#     costs=[149.0, 146.0, 141.0, 146.0, 126.0],
# )
# PSO_BERN_SRDF_LS.mean = np.mean(PSO_BERN_SRDF_LS.costs)
# PSO_BERN_SRDF_LS.std = np.std(PSO_BERN_SRDF_LS.costs)
# PSO_BERN_SRDF_LS.best_cost = np.min(PSO_BERN_SRDF_LS.costs)
# PSO_BERN_SRDF_LS.worst_cost = np.max(PSO_BERN_SRDF_LS.costs)


# Big problems ========================
SRD = AlgorithmTestResults(
    computing_times=[0.164],
    iterations=[1],
    costs=[190.0, 190.0, 190.0, 190.0, 190.0],
    mean=190.0,
    std=0.0,
)

SA = AlgorithmTestResults(
    computing_times=[59.91, 60.27, 60.40, 60.29, 59.97],
    iterations=[5000, 5000, 5000, 5000, 5000],
    costs=[130.0, 136.0, 151.0, 142.0, 141.0],
)
SA.mean = np.mean(SA.costs)
SA.std = np.std(SA.costs)
SA.best_cost = np.min(SA.costs)
SA.worst_cost = np.max(SA.costs)

PSO_LIT = AlgorithmTestResults(
    computing_times=[184.32, 185.24, 186.63, 184.44, 184.26],
    iterations=[29, 29, 29, 29, 29],
    costs=[190.0, 190.0, 190.0, 190.0, 186.0],
)
PSO_LIT.mean = np.mean(PSO_LIT.costs)
PSO_LIT.std = np.std(PSO_LIT.costs)
PSO_LIT.best_cost = np.min(PSO_LIT.costs)
PSO_LIT.worst_cost = np.max(PSO_LIT.costs)

PSO_LIT_LS = AlgorithmTestResults(
    computing_times=[199.14, 199.91, 200.66, 181.98, 184.55],
    iterations=[11, 11, 11, 10, 10],
    costs=[187.0, 186.0, 189.0, 190.0, 185.0],
)
PSO_LIT_LS.mean = np.mean(PSO_LIT_LS.costs)
PSO_LIT_LS.std = np.std(PSO_LIT_LS.costs)
PSO_LIT_LS.best_cost = np.min(PSO_LIT_LS.costs)
PSO_LIT_LS.worst_cost = np.max(PSO_LIT_LS.costs)

PSO_RAND = AlgorithmTestResults(
    computing_times=[181.38, 182.42, 182.59, 180.83, 181.25],
    iterations=[98, 98, 99, 96, 87],
    costs=[222.0, 215.0, 239.0, 237.0, 249.0],
)
PSO_RAND.mean = np.mean(PSO_RAND.costs)
PSO_RAND.std = np.std(PSO_RAND.costs)
PSO_RAND.best_cost = np.min(PSO_RAND.costs)
PSO_RAND.worst_cost = np.max(PSO_RAND.costs)

PSO_BERN_RF = AlgorithmTestResults(
    computing_times=[181.58, 183.39, 182.52, 182.40, 181.50],
    iterations=[87, 75, 81, 79, 79],
    costs=[232.0, 238.0, 234.0, 232.0, 236.0],
)
PSO_BERN_RF.mean = np.mean(PSO_BERN_RF.costs)
PSO_BERN_RF.std = np.std(PSO_BERN_RF.costs)
PSO_BERN_RF.best_cost = np.min(PSO_BERN_RF.costs)
PSO_BERN_RF.worst_cost = np.max(PSO_BERN_RF.costs)

PSO_BERN_SRDF = AlgorithmTestResults(
    computing_times=[183.12, 182.21, 181.20, 181.00, 181.55],
    iterations=[81, 85, 87, 89, 79],
    costs=[190.0, 185.0, 185.0, 185.0, 190.0],
)
PSO_BERN_SRDF.mean = np.mean(PSO_BERN_SRDF.costs)
PSO_BERN_SRDF.std = np.std(PSO_BERN_SRDF.costs)
PSO_BERN_SRDF.best_cost = np.min(PSO_BERN_SRDF.costs)
PSO_BERN_SRDF.worst_cost = np.max(PSO_BERN_SRDF.costs)

PSO_BERN_SRDF_LS = AlgorithmTestResults(
    computing_times=[184.97, 185.93, 190.78, 183.45, 184.81],
    iterations=[16, 19, 20, 17, 17],
    costs=[178.0, 175.0, 171.0, 182.0, 167.0],
)
PSO_BERN_SRDF_LS.mean = np.mean(PSO_BERN_SRDF_LS.costs)
PSO_BERN_SRDF_LS.std = np.std(PSO_BERN_SRDF_LS.costs)
PSO_BERN_SRDF_LS.best_cost = np.min(PSO_BERN_SRDF_LS.costs)
PSO_BERN_SRDF_LS.worst_cost = np.max(PSO_BERN_SRDF_LS.costs)
print("Big problem: 15 machines 100 jobs")
data = []
for alg in [SRD, SA, PSO_LIT, PSO_LIT_LS, PSO_RAND, PSO_BERN_RF, PSO_BERN_SRDF, PSO_BERN_SRDF_LS]:
    algo = {
        "computing_times": round(np.mean(alg.computing_times), 2),
        "iterations": np.mean(alg.iterations),
        "worst_cost": alg.worst_cost,
        "best_cost": alg.best_cost,
        "mean": alg.mean,
        "std": alg.std,
    }
    data.append(algo)

parsed_data = pd.DataFrame(data)
parsed_data.index = [
    "SRD",
    "SA",
    "PSO_LIT",
    "PSO_LIT_LS",
    "PSO_RAND",
    "PSO_BERN_RF",
    "PSO_BERN_SRDF",
    "PSO_BERN_SRDF_LS",
]
print(parsed_data)


# for alg in [SRD, SA, PSO_LIT, PSO_LIT_LS, PSO_RAND, PSO_BERN_RF, PSO_BERN_SRDF, PSO_BERN_SRDF_LS]:
#     for alg2 in [SRD, SA, PSO_LIT, PSO_LIT_LS, PSO_RAND, PSO_BERN_RF, PSO_BERN_SRDF, PSO_BERN_SRDF_LS]:
