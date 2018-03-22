import random
##import xlwt #Excel library

##total: do tylu się sumuje, n: na tyle liczb ma się składać
def constrained_sum_sample_pos(n, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""
    dividers = sorted(random.sample(range(0, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]

def constrained_sum_sample_nonneg(n, total):
    """Return a randomly chosen list of n nonnegative integers summing to total.
    Each such list is equally likely to occur."""
    return [x - 1 for x in constrained_sum_sample_pos(n, total + n)]

##workbook = xlwt.Workbook(encoding="utf-8")
##worksheet = workbook.add_sheet("generated-data")

"""
gens=[]

for i in range (0, 8):
    j = 0
    gen=[]
    #list = constrained_sum_sample_nonneg(15, 400)
    list = constrained_sum_sample_pos(3, 8)
    for n in list:
        j = j+1
        gen.append(n)
        #worksheet.write(j, i, n)
        ##print(n)
    gens.append(gen)

print(gens)
#workbook.save("FileName.csv")

"""