import itertools

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

# Generuje liste wszyskich możliwych genów (tablic routingu)
def generate_list_of_possible_chromosoms(D, numberOfPossibleGens, possibleGens):
    possibleChromosoms= generate_possible_chromosoms(D, numberOfPossibleGens)
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
