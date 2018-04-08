import time
import  random
from DAP_problem import*
from Data import *
import copy

class Evolution:

    def __init__(self):
        self.P_mutacji = 0.1
        self.P_crossing_over = 0.4
        self.Evolution_time = 120
        self.seed = 20
        self.best_solution_cost = []
        self.best_solution_chromosom = []
        self.data = Data()
        self.dap = DAP()
        self.sum_minimize_f_x_initial_population = []
        self.count = 0
        self.sum_f_x = []

    def initial_population(self, sum_minimize_f_x, tableOfChromosoms):
        tableOfChromosomsMutation = []
        table_of_cost = []
        indeks= []
        self.sum_minimize_f_x_initial_population = []
        self.sum_minimize_f_x_initial_population.extend(sum_minimize_f_x)
        #self.sum_f_x = []
        #self.sum_f_x.extend(sum_minimize_f_x)
        #print("##########################333")
        #print("suma",sum_minimize_f_x)
        #print(self.dap.suma_elementow_listy(self.dap.minimize_function(tableOfChromosoms)))
        for i in range(100):

            low = min(self.sum_minimize_f_x_initial_population)
            #table_of_cost.append(low)
            indeks.append(self.sum_minimize_f_x_initial_population.index(low))
            tableOfChromosomsMutation.append(tableOfChromosoms[self.sum_minimize_f_x_initial_population.index(low)])
            self.sum_minimize_f_x_initial_population[self.sum_minimize_f_x_initial_population.index(low)] = 10000

        #print(indeks)
        #print("table of low",table_of_cost)
        #print("suma2",self.dap.suma_elementow_listy(self.dap.minimize_function(tableOfChromosomsMutation)))
        #print("##################333##")

        return tableOfChromosomsMutation


    def mutation(self, tableOfChromosomsMutation):

        #cost_function = minimize_function(self.data.E, tableOfChromosomsMutation, self.data.P, self.data.links, self.data.D)

        newTableOfChromosom = []
        #Krzyżowanie
        for a in range(0,100,2):
            #p = random.seed(self.seed + self.count)
            #for i in range(0, int(1000), 2):
            #p = random.seed(x)
            #s1 = random.randint(0, len(tableOfChromosomsMutation)/2-1)
            #s2 = random.randint(len(tableOfChromosomsMutation)/2, len(tableOfChromosomsMutation)-1)
            s1 = a
            s2 = a+1
            osobnik1 = tableOfChromosomsMutation[s1]
            osobnik2 = tableOfChromosomsMutation[s2]

            newTableOfChromosom.append(osobnik1)
            newTableOfChromosom.append(osobnik2)

            probabilityOfCrossingOver = random.uniform(0, 1)
            if probabilityOfCrossingOver <= self.P_crossing_over:

                crossing_over = random.randint(0, self.data.D)

                merged_list = osobnik1[:crossing_over] + osobnik2[crossing_over:]
                merged_list2 = osobnik2[:crossing_over] + osobnik1[crossing_over:]

                newTableOfChromosom.append(merged_list)
                newTableOfChromosom.append(merged_list2)

            count = self.count +1
            ###################

        #new_minimize_f_x = minimize_function(self.data.E, newTableOfChromosom, self.data.P, self.data.links, self.data.D)
        #new_sum_minimize_f_x = suma_elementow_listy(new_minimize_f_x)


        mutation = []
        newMutatedChromosom = newTableOfChromosom.copy()
        print("sum1", self.dap.suma_elementow_listy(self.dap.minimize_function(newTableOfChromosom)))


        for item in newMutatedChromosom:
           # p = random.seed(self.seed + self.count)
            #p = random.seed(x)
            #newMutatedChromosom.append(item)
            mutation_possibility = random.uniform(0, 1)
            if mutation_possibility <= self.P_mutacji:
            #for i in range(1):
                x = random.randint(0, len(item)-1)

                minindex = item[x].index(min(item[x]))
                maxindex = item[x].index(max(item[x]))

                item[x][minindex] = min(item[x]) + 1
                item[x][maxindex] = max(item[x])-1

                mutation.append(item)

                item[x][minindex] = min(item[x]) - 1
                item[x][maxindex] = max(item[x]) + 1

            count = self.count + 1


        merged_mutation = newTableOfChromosom + mutation

        print("sum2", self.dap.suma_elementow_listy(self.dap.minimize_function(merged_mutation)))
        #print("mutation", self.dap.suma_elementow_listy(self.dap.minimize_function(mutation)))
        new_minimize_f_x2 = self.dap.minimize_function(merged_mutation)
        new_sum_minimize_f_x2 = self.dap.suma_elementow_listy(new_minimize_f_x2)

        #best_solutution = min(new_sum_minimize_f_x)
        #print(best_solutution)
       # self.best_solution_cost.append(best_solutution)
        #self.best_solution_chromosom.append(newTableOfChromosom[new_sum_minimize_f_x.index(best_solutution)])

            #if end - start > self.Evolution_time:
             #   print("przekroczono czas")
              #  break

       # return self.best_solution_cost, self.best_solution_chromosom
        count= self.count+1
        return new_sum_minimize_f_x2, merged_mutation

