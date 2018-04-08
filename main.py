from DAP_problem import*
from Evolution import *
from Data import *


class MainClass:
    def __init__(self):
        self.sum_minimize_f_x = []

        # Odwołanie do klasy Data
        data = Data()
        dap = DAP()

        #Generacja możliwych genów na podstawie funkcji z pliku DAP_problem.py
        possibleGens = dap.generate_list_of_gens_for_all_demands(data.D, data.m_d, data.h_d)

        numberOfPossibleGens = []
        for i in range(data.D):
            numberOfPossibleGens.append(len(possibleGens[i]))

        #generacja możliwości ułożenia genów w chromosomie
        tableOfChromosoms= dap.generate_list_of_possible_chromosoms(data.D, numberOfPossibleGens, possibleGens)

        #liczenie wartości funkcji f(x)
        minimize_f_x = dap.minimize_function(tableOfChromosoms)

        #sumuje wartości, żeby znależć najlepsze rozwiązanie
        self.sum_minimize_f_x =dap.suma_elementow_listy(minimize_f_x)

        najmniejsze_rozwiazanie_z_populacji = min(self.sum_minimize_f_x)
        print("najmniejsze rozwiązanie populacji:", najmniejsze_rozwiazanie_z_populacji)

        #print(najmniejsze_rozwiązanie_z_populacji)

        theFile= open("optymalny_wynik.txt", 'w')

        #Szukanie najlepszego rozwiązania algorytm ewolucyjny
        if najmniejsze_rozwiazanie_z_populacji == 0:
            print("Znaleziono rozwiąznie optymalne, dla zbioru małego z wykorzystaniem metody Brute Force:")
            theFile.write("Znaleziono rozwiąznie optymalne, dla zbioru małego z wykorzystaniem metody Brute Force:")
            print(tableOfChromosoms[self.sum_minimize_f_x.index(min(self.sum_minimize_f_x))])
            theFile.write(str(tableOfChromosoms[self.sum_minimize_f_x.index(min(self.sum_minimize_f_x))]))
        else:

            nowe_najmniejsze_rozwiazanie = 1000
            count = 0
            evolution = Evolution()
            start= time.time()
            #Populacja początkowa (sum_minimize_f_x)
            rozwiazaniaWKolejnychGeneracjach = []
            best_solution_chromosom = []
            best_solution_cost = []
            x = []

            tableOfChromosomsMutation = evolution.initial_population(self.sum_minimize_f_x, tableOfChromosoms)

            while 0 < nowe_najmniejsze_rozwiazanie:
                #Mutacja
                if count == 0:
                    best_solution_cost, best_solution_chromosom = evolution.mutation(tableOfChromosomsMutation)

                if count > 0:
                    tableOfChromosomsMutation = evolution.initial_population(best_solution_cost, best_solution_chromosom)
                    #print(dap.suma_elementow_listy(dap.minimize_function(tableOfChromosomsMutation)))
                    #print("1: ", best_solution_cost)
                    best_solution_cost, best_solution_chromosom = evolution.mutation(tableOfChromosomsMutation)
                    #print("2: ", best_solution_cost)


                #print(best_solution_cost)

                nowe_najmniejsze_rozwiazanie = min(best_solution_cost)
                rozwiazaniaWKolejnychGeneracjach.append(nowe_najmniejsze_rozwiazanie)
                #print(nowe_najmniejsze_rozwiązanie)
                #print(best_solution_chromosom)
                count = count +1
                #print(count)

            index_of_best_solution = best_solution_cost.index(nowe_najmniejsze_rozwiazanie)
            best_solution = best_solution_chromosom[index_of_best_solution]
            x.append(best_solution)
            end = time.time()
            print("Znaleziono rozwiązanie najbardziej optymalne dla dużego zbioru.")
            print("Rozwiązanie (chromosom): ", best_solution)
            print("Koszt rozwiązania: ",dap.minimize_function( x))
            print("Suma kosztów rozwiązania: ", nowe_najmniejsze_rozwiazanie)
            print("Sekwencja wartości najlepszych rozwiązań: ", rozwiazaniaWKolejnychGeneracjach)
            print("Ilość iteracji: ",count)
            print("Czas:", end - start)


            theFile.write("Rozwiazanie (chromosom): " )
            theFile.write("%s\n" % str(best_solution))
            theFile.write("Koszt rozwiazania: " )
            theFile.write("%s\n" % str(dap.minimize_function( x)))
            theFile.write("Suma kosztow rozwiazania: " )
            theFile.write("%s\n" % str(nowe_najmniejsze_rozwiazanie))
            theFile.write("Liczba wykonanych iteracji algorytmu:")
            theFile.write("%s\n" % str(count))


main = MainClass()
