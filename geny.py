import itertools
import math
import time
import random

#total: do tylu się sumuje, n: na tyle liczb ma się składać
def lista_mozliwych_genow( n, total):
    allPossibleGene = [x for x in range(0, int(total)+1)]
    tab=[x for x in itertools.product(allPossibleGene, repeat=n) if sum(x) == int(total)]
    b = [list(x) for x in tab]
    return b

# Generuje listę możliwych genów dla wszystkich zapotrzebowań
def generate_list_of_gens_for_all_demands( D, m_d, h_d):
    gens=[]
    for i in range(0, D):
        lista = lista_mozliwych_genow(m_d[i], h_d[i])
        gens.append(lista)
    return gens

# Generuje tablice która ustala indeksy genow jakie będą wczytane do chromosomów
def generate_possible_chromosoms(D, numberOfPossibleGens ):

    allPossibleQuanta = [x for x in range(0, int(max(numberOfPossibleGens)))]
    #a = [x for x in itertools.product(allPossibleQuanta, repeat=6) if x[5] <= int(3) ]

    chromosoms=[]
    for x in itertools.product(allPossibleQuanta, repeat=D):
        count = 0

        for i in range(D):
            if x[i] < numberOfPossibleGens[i]:
                count=count+1

        if count == len(numberOfPossibleGens):
            chromosoms.append(list(x))

    return chromosoms


# Generuje tablice która ustala indeksy genow jakie będą wczytane do chromosomów dla dużych zbiorów
def generate_possible_chromosoms_BIG(D, numberOfPossibleGens ):

    chromosoms=[]

    for i in range(1000):
        random_chromosom = []
        for j in range(D):
            random_chromosom.append(random.randint(0, numberOfPossibleGens[j]-1))

        chromosoms.append(random_chromosom)

    return chromosoms

# Generuje liste wszyskich możliwych genów (tablic routingu)
def generate_list_of_possible_chromosoms(D, numberOfPossibleGens, possibleGens):

    if D < 20:
        possibleChromosoms= generate_possible_chromosoms(D, numberOfPossibleGens)
    else:
        possibleChromosoms = generate_possible_chromosoms_BIG(D, numberOfPossibleGens)

    tableOfChromosom=[]

    for i in possibleChromosoms:
        a= []
        for j in range(D):
            a.append(possibleGens[j][i[j]])

        tableOfChromosom.append(a)

    theFile= open("tablice_routingu.txt", 'w')
    for item in tableOfChromosom:
        theFile.write("%s\n" % item)

    return tableOfChromosom

def minimize_function(E, tableOfChromosom,P, links,D ):

    f_x = []
    for chrom in tableOfChromosom:
        link_loads = []

        for item in range(1, E+1):
            ll = 0
            for i in P:
                ii = P.index(i)

                for j, x in enumerate(i):
                    if item in x:
                        #print(chromosom[ii][j])
                        ll = ll + chrom[ii][j]

            link_loads.append(ll)

        l_e_x = []
        for i in range(len(link_loads)):
            l_e_x.append(max(0, link_loads[i] - links[0][2]*links[0][4]))

        f_x.append(l_e_x)

    return f_x


def suma_elementow_listy(minimize_f_x):

    sum_minimize_f_x =[]
    for i in minimize_f_x:
        sum_minimize_f_x.append(sum(i))

    return sum_minimize_f_x
