from AggroProject import dist
from itertools import product
import sys


list = [[[1,1,1], [2,2,2], [4,4,4], [5,5,5], [7,7,7]], [[40,0,0], [45,0,0], [50,0,0]], [[0,10,0], [0,11,0], [0,12,0]]]
list2 = [[1,1,1], [2,2,2], [4,4,4], [5,5,5], [7,7,7]]
list3 = [[[0,0,0], [2,0,0], [4,0,0], [6,0,0]]]


def get_o():
    if len(sys.argv) > 2:
        o = float(sys.argv[2])
    else:
        o = float(input("At what distance should outliers lie away from other points:\n"))
    return o


def find_outliers(lst):
    # initialize values for needed variables
    o, outliers, i = get_o(), [], 0

    for y, a in enumerate(lst):
        print("list[a]: {}\n len(list[a]): {}".format(a, len(a)))
        i, origLenList = 0, len(a)
        outliers.append([])
        # if length of lst[a] is greater than 1 continue
        if len(a) > 1:
            # while i is less than length of lst[a] keep iterating this block
            while i < len(a):
                temp = a.pop(i)
                # print("new temp: ", temp)
                j, count = 0, 0
                # check if the list is equal to len of outlier list
                if (origLenList - 1) == len(outliers[y]):
                    outliers[y].append(temp)
                    break
                while j < len(a):
                    aj = a[j]
                    # print("j:", j, ' ', aj)
                    if j > len(a) - 1:
                        break
                    d = dist(temp, aj)
                    # print("temp: {}, list[j]: {}, dist: {}".format(temp, aj, d))
                    if d <= o:
                        # print("inserted temp back in.")
                        a.insert(i, temp)
                        break
                    else:
                        count += 1
                        # print("count: {}, len list: {}".format(count, len(a)))
                        if count == len(a):
                            outliers[y].append(temp)
                            # print("outlier added:", temp)
                            j, i = 0, i - 1
                            break
                    j += 1
                i += 1
    print("Outliers: ", outliers)
    for index, cluster in enumerate(lst):
        print("new cluster: ",index+1, ": ", cluster)


def find_outliers2(list):
    a, count, o = 0, 0, get_o()
    outlier = []
    for x, y in product(range(len(list)), repeat=2):
        if len(list[x]) == 1:
            continue
        if a != x - 1:
            t = list[x].pop(y)
            print("new t popped: ", t)
            #for i, j in product(range(len(list[x])), repeat=2):
            for  i, p in enumerate(list):
                for j, q in enumerate(p):
                    try:
                        print("a: {}, x: {}, y: {}, i: {}, j: {}, t:{}, list[i][j]: {}".format(a, x, y, i, j, t, p[j]))
                        if dist(t, p[j]) < o:
                            list[x].insert(0, t)
                            print("insert point", t," back in ", list[x])
                            break
                        else:
                            count += 1
                            if count == len(list[x]):
                                count = 0
                                print("outlier detected:", t)
                                outlier.append(t)
                    except IndexError:
                        print("IndexError!  i: {}, j: {}, temp: {}, list[i][j]: {}".format(i, j, t, list[i][j]))
        else:
            print('a is equal to x-1. x=',x,'\n')
            a = x


def find_outliers3(lst):
    c, count, o = 0, 0, get_o()
    outlier = []
    for x, y in product(range(len(list)), repeat=2):
        for i, j in enumerate(list):
            c = list[x].pop(y)
            print("c:", c)
            for a, b in enumerate(j):
                print("x: {}, y: {}, j: {} \t j[a]: {}".format(x, y, j, b))






def main():
    print(list)
    find_outliers(list)

if __name__ == "__main__":
    main()




