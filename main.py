from random import randint
from geny import*
from Evolution import *
import heapq

import itertools

## usunięcie putych linijek z pliku
with open('dane_duze.txt', 'r+') as file:
    with open('dane2.txt', 'w+') as file2:
        for line in file:
            if not line.isspace():
                file2.write(line)

## Otwieram plik
f = open('dane2.txt', 'r')

#Wczytuje liczbe krawedzi E
E = int(f.readline())
#print(E)

links = []
# Wczutuj tablice kwawędzi do tablicy dwuwymiarowej
for i in range(E):
    ee = [int(i) for i in f.readline().split()]
    links.append(ee)

# Wczytuje liczbe zapotrzebowań
D = int(f.readline())
if D <= 0:
    D = int(f.readline())

#Generuje puste tablice o odpowiedniej długości
d = [0]*D
p = [0]*D
h_d = [0]*D
m_d = [0]*D
P = []
# Generuje słownik sciezek
for i in range(D):
    d[i], p[i], h_d[i] = [int(a) for a in f.readline().strip().split(' ')]
    m_d[i] = int(f.readline())
    a=[]
    for j in range(m_d[i]):
        x = [int(a) for a in f.readline().strip().split(' ')]
        ##P['P('+str(i+1)+','+str(j+1)+')'] = x[1:]
        a.append(x[1:])
    P.append(a)


#Generacja możliwych genów na podstawie funkcji z pliku geny.py
possibleGens = generate_list_of_gens_for_all_demands(D, m_d, h_d)

numberOfPossibleGens=[]
for i in range(D):
    numberOfPossibleGens.append(len(possibleGens[i]))

#generacja możliwości ułożenia genów w chromosomie

tableOfChromosoms= generate_list_of_possible_chromosoms(D, numberOfPossibleGens, possibleGens)

#liczenie wartości funkcji f(x)
minimize_f_x = minimize_function(E, tableOfChromosoms, P, links, D)

#sumuje wartości, żeby znależć najlepsze rozwiązanie
sum_minimize_f_x =suma_elementow_listy(minimize_f_x)
print(sum_minimize_f_x)
print(min(sum_minimize_f_x))
'''
if min(sum_minimize_f_x) == 0:
    print("Znaleziono rozwiąznie optymalne:")
    print(tableOfChromosoms[sum_minimize_f_x.index(min(sum_minimize_f_x))])
'''

#Mutacja

P_mutacji = 0.1
evolution = Evolution()

#Populacja początkowa (sum_minimize_f_x)
tableOfChromosomsMutation = evolution.initial_population(sum_minimize_f_x, tableOfChromosoms)

print(tableOfChromosomsMutation)

best_solution_cost, best_solution_chromosom = evolution.mutation(tableOfChromosomsMutation, D, E, P, links)

print(best_solution_cost)
print(best_solution_chromosom)