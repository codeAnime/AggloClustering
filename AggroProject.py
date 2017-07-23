import math, sys
import time


def dist(a, b):
    s = 0
    for i in range(3):
        s += (a[i] - b[i]) ** 2
    return float("%.3f" % math.sqrt(s))


def get_max(data):
    max = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            d = dist(data[i], data[j])
            if max < d:
                max = d
    max = int(max + 1)
    # print("max", max)
    return max

# Printing the data from the clusters:
def vis_list(list1):
    a = 1
    for i in range(len(list1)):
        print('Cluster #', a, ' ', str(list1[i]).replace('[', '(').replace(']',')'))
        a += 1


def traverseList(list1, max1):
    a, b, c = None, None, max1
    for i in range(len(list1)-1):
        for n in range(len(list1[i])):
            for j in range(i+1, len(list1)):
                for m in range(len(list1[j])):
                    d = dist(list1[i][n], list1[j][m])
                    if c > d:
                        a, b, c = i, j, d
    return a, b


def merge(list1, a, b):
    for i in range(len(list1[b])):
        list1[a].append(list1[b][i])
    del list1[b]


def main():
    #data = [[1, 1, 1], [2, 2, 2], [4, 4, 4], [5, 5, 5], [7, 7, 7], [40, 0, 0], [45, 0, 0], [50, 0, 0], [0, 10, 0], [0, 11, 0], [0, 12, 0]]

    #data = [[1,2,3], [2,2,2], [33,3,3], [44,4,4], [55,5,5], [7,7,7], [0,10,8], [45, 0, 5]]
    data = []
    list1 = []
    max1 = get_max(data)

    with open("dataset1.csv", 'r') as f:
        for i in f:
            line = i.strip().split(",")
            for j in range(len(line)):
                line[j] = int(line[j])
            data.append(line)

    for i in range(len(data)):
        list1.append([data[i]])

    if len(sys.argv) > 1:
        k = int(sys.argv[1])
    else:

        k = int(input("How many clusters do you want:\n"))
        print("Please wait a minute or 2 for algorithm to finish.\n")
    if 0 >= k or k > len(data):
        raise Exception("K not in correct range. Pick number between 1 and ", len(data))
    else:
        start_time = time.time()
        while k < len(list1):
            a, b = traverseList(list1, 100)
            merge(list1, a, b)
    print("Time it took to run Agglomerative algorithm: ", time.time() - start_time)
    vis_list(list1)

    # Outlier program
    cont = input("Do you want outliers to be taken out? Answer with: 'Y' or 'N' for Yes/No")
    if cont.upper() == "Y":
        start_time = time.time()
        import outlier
        outlier.find_outliers(list1)
        print("Time it took to detect Outliers: ", time.time() - start_time)

    cont = input("Do you want find the silhouette coefficient for this data set? Answer with: 'Y' or 'N' for Yes/No")
    if cont.upper() == "Y":
        start_time = time.time()
        import SilhouetteCo as sc
        sc.calc_silhouette2(list1)
        print("Time it took to calculate Silhouette Coefficient: ", time.time() - start_time)


if __name__ == "__main__":
    main()