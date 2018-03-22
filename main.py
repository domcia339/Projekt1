from random import randint
from geny import*

## usunięcie putych linijek z pliku
with open('dane.txt','r+') as file:
    with open('dane2.txt', 'w+') as file2:
        for line in file:
            if not line.isspace():
                file2.write(line)

## Otwieram plik
f = open('dane2.txt', 'r')

#Wczytuje liczbe krawedzi E
E = int(f.readline())
print(E)

links = []

# Wczutuj tablice kwawędzi do tablicy dwuwymiarowej
for i in range(E):
    # e = f.readline().split()v
    #ee = list(map(int, f.readline().split()))
    ee = [int(i) for i in f.readline().split()]
    links.append(ee)
print(links)

# Wczytuje liczbe zapotrzebowań
D=int(f.readline())
if(D<=0):
    D = int(f.readline())
print(D)

d=[0]*D
p=[0]*D
h_d=[0]*D
m_d=[0]*D
P={}  #Słownik
# Generuje słownik sciezek
for i in range(D):
    #d[i], p[i], h_d[i] = list(map(int,f.readline().strip().split(' ')))
    d[i], p[i], h_d[i] = [int(a) for a in f.readline().strip().split(' ')]
    m_d[i]=int(f.readline())
    for j in range(m_d[i]):
        #x=list(map(int,f.readline().strip().split(' ')))
        x = [int(a) for a in f.readline().strip().split(' ')]
        P['P('+str(i+1)+','+str(j+1)+')']=x[1:]
print(P)

#generacja chromosomów na podstawie funkcji z pliku geny.py
gens=[]
for i in range (0, 10):
    j = 0
    gen=[]
    #list = constrained_sum_sample_nonneg(15, 400)
    list = constrained_sum_sample_pos(m_d[0], h_d[0])
    for n in list:
        j = j+1
        gen.append(n)
        #worksheet.write(j, i, n)
        ##print(n)
    gens.append(gen)

print(gens)