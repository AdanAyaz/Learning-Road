#python selection sorting algorithm simplified with a bug for numbers with difference of first unit being in different unit places
import math
def swap(list, xx, yy):
    list[xx], list[yy] = list[yy], list[xx]
    return list

print("Numbers to arrange: ")
xa = input()
xc = xa.split()
print(xc)
m = len(xc)
m = int(m)
aaa = 0
while (aaa == (m*m)-1) == False:
    aaa += 1
    for i in range(0, m-1):
        i = int(i)
        if (i == m-1) == False:
            if (xc[i] > xc[i+1]) == True:
                swap(xc, i, (i+1))
            elif (xc[i] <= xc[i+1]) == True:
                continue

print(xc)
print("Code is complete.")