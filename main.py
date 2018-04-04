from DAP_problem import*
from Evolution import *
from Data import *

data = Data()

#Generacja możliwych genów na podstawie funkcji z pliku DAP_problem.py
possibleGens = generate_list_of_gens_for_all_demands(data.D, data.m_d, data.h_d)

numberOfPossibleGens = []
for i in range(data.D):
    numberOfPossibleGens.append(len(possibleGens[i]))

#generacja możliwości ułożenia genów w chromosomie
tableOfChromosoms= generate_list_of_possible_chromosoms(data.D, numberOfPossibleGens, possibleGens)

#liczenie wartości funkcji f(x)
minimize_f_x = minimize_function(data.E, tableOfChromosoms, data.P, data.links, data.D)

#sumuje wartości, żeby znależć najlepsze rozwiązanie
sum_minimize_f_x =suma_elementow_listy(minimize_f_x)
najmniejsze_rozwiązanie_z_populacji = min(sum_minimize_f_x)
print(najmniejsze_rozwiązanie_z_populacji)

if najmniejsze_rozwiązanie_z_populacji == 0:
    print("Znaleziono rozwiąznie optymalne, dla zbioru małego z wykorzystaniem metody Brute Force:")
    print(tableOfChromosoms[sum_minimize_f_x.index(min(sum_minimize_f_x))])
else:
    nowe_najmniejsze_rozwiązanie = 1000

    while najmniejsze_rozwiązanie_z_populacji < nowe_najmniejsze_rozwiązanie:
        #Mutacja
        x = []
        evolution = Evolution()

        #Populacja początkowa (sum_minimize_f_x)
        tableOfChromosomsMutation = evolution.initial_population(sum_minimize_f_x, tableOfChromosoms)
        #print(tableOfChromosomsMutation)

        best_solution_cost, best_solution_chromosom = evolution.mutation(tableOfChromosomsMutation)

        #print(best_solution_cost)
        nowe_najmniejsze_rozwiązanie = min(best_solution_cost)
        #print(nowe_najmniejsze_rozwiązanie)
        #print(best_solution_chromosom)

        end = time.time()


    index_of_best_solution = best_solution_cost.index(nowe_najmniejsze_rozwiązanie)
    best_solution = best_solution_chromosom[index_of_best_solution]
    x.append(best_solution)

    print("Znaleziono rozwiązanie najbardziej optymalne dla dużego zbioru.")
    print("Rozwiązanie (chromosom): ", best_solution)
    print("Koszt rozwiązania: ",minimize_function(data.E, x, data.P, data.links, data.D))
    print("Suma kosztów rozwiązania: ", nowe_najmniejsze_rozwiązanie)

    theFile= open("optymalny_wynik.txt", 'w')
    theFile.write("Rozwiazanie (chromosom): " )
    theFile.write("%s\n" % str(best_solution))
    theFile.write("Koszt rozwiazania: " )
    theFile.write("%s\n" % str(minimize_function(data.E, x, data.P, data.links, data.D)))
    theFile.write("Suma kosztow rozwiazania: " )
    theFile.write("%s\n" % str(nowe_najmniejsze_rozwiązanie))

