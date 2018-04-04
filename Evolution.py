import time
import  random
from DAP_problem import*
from Data import *

class Evolution:

    def __init__(self):
        self.P_mutacji = 0.1
        self.P_crossing_over = 0.4
        self.Evolution_time = 100
        self.seed = 534207523132
        self.best_solution_cost = []
        self.best_solution_chromosom = []
        self.data = Data()


    def initial_population(self, sum_minimize_f_x, tableOfChromosoms):
        tableOfChromosomsMutation = []

        for i in range(int(self.P_mutacji*3000)):
            #chromosom_index = random.randint(0, 1000-1)
            low = max(sum_minimize_f_x)
            for j in sum_minimize_f_x:
                if (j <= low ):
                    low = j

            tableOfChromosomsMutation.append(tableOfChromosoms[sum_minimize_f_x.index(low)])
            sum_minimize_f_x.remove(low)

        return tableOfChromosomsMutation


    def mutation(self, tableOfChromosomsMutation):

        start = time.time()
        for a in range(0, int(self.P_mutacji*3000*self.P_crossing_over)):
            newTableOfChromosom = []
            x = 534207523132 + time.time()
            for i in range(0, int(self.P_mutacji*3000), 2):
                p = random.seed(x)
                s1 = random.randint(0, len(tableOfChromosomsMutation)/2-1)
                s2 = random.randint(len(tableOfChromosomsMutation)/2, len(tableOfChromosomsMutation)-1)
                osobnik1 = tableOfChromosomsMutation[s1]
                osobnik2 = tableOfChromosomsMutation[s2]

                crossing_over = random.randint(0, self.data.D)

                merged_list = osobnik1[:crossing_over] + osobnik2[crossing_over:]
                newTableOfChromosom.append(merged_list)
                x = x + time.time()

            new_minimize_f_x = minimize_function(self.data.E, newTableOfChromosom, self.data.P, self.data.links, self.data.D)
            new_sum_minimize_f_x = suma_elementow_listy(new_minimize_f_x)

            best_solutution = min(new_sum_minimize_f_x)
            self.best_solution_cost.append(best_solutution)
            self.best_solution_chromosom.append(newTableOfChromosom[new_sum_minimize_f_x.index(best_solutution)])

            end = time.time()
            if end - start > self.Evolution_time:
                #print("przekroczono czas")
                break

        return self.best_solution_cost, self.best_solution_chromosom

