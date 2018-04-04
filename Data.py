
# Klada która jest odpowiedzialna tylko za wczytywanie danych z pliku
class Data:

    def __init__(self):

        ## usunięcie putych linijek z pliku
        with open('dane_duze.txt', 'r+') as file:
            with open('dane2.txt', 'w+') as file2:
                for line in file:
                    if not line.isspace():
                        file2.write(line)

        ## Otwieram plik
        f = open('dane2.txt', 'r')

        #Wczytuje liczbe krawedzi E
        self.E = int(f.readline())
        #print(E)

        self.links = []
        # Wczutuj tablice kwawędzi do tablicy dwuwymiarowej
        for i in range(self.E):
            ee = [int(i) for i in f.readline().split()]
            self.links.append(ee)

        # Wczytuje liczbe zapotrzebowań
        self.D = int(f.readline())
        if self.D <= 0:
            self.D = int(f.readline())

        #Generuje puste tablice o odpowiedniej długości
        self.d = [0]*self.D
        self.p = [0]*self.D
        self. h_d = [0]*self.D
        self.m_d = [0]*self.D
        self.P = []
        # Generuje słownik sciezek
        for i in range(self.D):
            self.d[i], self.p[i], self.h_d[i] = [int(a) for a in f.readline().strip().split(' ')]
            self.m_d[i] = int(f.readline())
            a=[]
            for j in range(self.m_d[i]):
                x = [int(a) for a in f.readline().strip().split(' ')]
                ##P['P('+str(i+1)+','+str(j+1)+')'] = x[1:]
                a.append(x[1:])
            self.P.append(a)