from random import randint
from geny import*
import math

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
minimize_f_x = minimize_function(E, tableOfChromosoms, P, links)
print(minimize_f_x)

#Mutacja

#Wybieram 10 najmniejszych tablic
tableOfChromosomsMutatioan = []
for i in range(10):
    min_chromosom = min(minimize_f_x)
    tableOfChromosomsMutatioan.append(tableOfChromosoms[minimize_f_x.index(min_chromosom)])

#for i in range(0,10, 2):


