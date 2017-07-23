from AggroProject import dist
import itertools as it

list = [[[0,1,0],[0,2,0],[0,5,0],[0,3,0]],
        [[10, 1, 0],[13, 1, 0],[15, 2, 0]],
        [[20, 20, 0], [25, 30, 1]]]
orig_list, other_list, sil_list = [], [], []
list2 = [[[5,16,0],[8,13,0],[8,10,0],[5,9,0]],
         [[14,16,0],[18,17,0]],
         [[10,3,0],[12,5,0],[16,7,0],[16,11,0]]]


def calc_silhouette(list):
    sum, count = 0, 0
    for w in range(len(list)-1):
        other_list.append([])

    for i in range(len(list)):
        list.insert(0, list.pop(i))
        for j in range(len(list[0])):
            t = list[0].pop(j)
            for index, m in enumerate(list):
                for n in range(len(m)):
                    sum += dist(t, m[n])
                    count += 1
                d = sum / len(m)
                if index == 0:  orig_list.append(d)
                else:           other_list[index-1].append(d)
                sum = 0
            list[0].insert(0, t)

    while len(orig_list) > 0:
        fill_silhouette(orig_list, other_list, sil_list)

    print("silhouette list:", sil_list)
    sum = 0
    for sil in sil_list:
        sum += sil
    print("Silhouette Coefficient is: ", sum / len(sil_list))


def fill_silhouette(orig_list, other_list, sil_list):
    print("original_list:\t", orig_list, " other_list:\t", other_list)
    print("original_list[0]:\t", orig_list[0], " other_list[0]:\t", other_list[0])
    print("sil:", sil_list)
    a1, b1 = orig_list.pop(0), other_list[0][0]
    for i, j in it.product(range(len(other_list)-1), repeat=2):
        b1 = min(b1, other_list[j].pop(0))
    sil_list.append((b1 - a1) / max(a1, b1))


# ***************All methods below are for calc_silhouette2:***************************

def getLocalSilValue(point, lst):
    sum = 0
    for i in range(len(lst)):
        sum += dist(point, lst[i])
    return float("%.3f" % (sum/len(lst)))


def getMinSilValue(point, lst):
        sil_values = []
        for i in range(len(lst)-1):
            sil_values.append([])

        for i in range(1, len(lst)):
            summ = 0
            for j in range(len(lst[i])):
                d = dist(point, lst[i][j])
                # print("comparing pt: {} and pt. lst[i][j]: {} -- dist: {}".format(point, lst[i][j], d))
                summ += d
            sil_values[i-1] = (summ / len(lst[i]))
            print("sil_values:", sil_values)

        m = sil_values[0]
        for i in range(1, len(sil_values)):
            m = min(m, sil_values[i])

        return float("%.3f" % m)


def swap_cluster(a, i, lst):
    print("swapping 0th position with a=", a, " : ", lst[a])
    lst.insert(0, lst.pop(a))
    print(lst)



def calc_silhouette2(lst):
    local_list, other_list, sil_list = [], [], []
    i, a = 0, 0
    # Gathering silhouette coefs. for each point phase:
    # for each point in list1[0] get silhouette coef. for its own cluster
    while i < len(lst[0]):
        print(i, " ", lst[0][i])
        t = lst[0].pop(i)

        # getting the silhouette coef. for the point inside its own cluster
        if len(lst[0]) == 0:
            local_list.append(0)
        else:
            local_list.append(getLocalSilValue(t, lst[0]))

        # for each cluster other than its own store min. sil. coef. cluster ONLY.
        min = getMinSilValue(t, lst)
        print("min: ", min)
        other_list.append(min)

        # insert the point back in
        lst[0].insert(i, t)

        # When cluster 0 (list[0]) is finished swap with next cluster
        if i == (len(lst[0])-1) and a < len(lst)-1:
            a += 1
            print("attempting: ", a)
            swap_cluster(a, i, lst)
            i = 0

            print("lst:", lst, " a:", a, " i:", i)
            continue
        i += 1

    # calculate silhouette coef. for every point and store in sil_list.
    # this is the first task not having to do with gathering silhouettes.
    summ = 0
    print("local_list:",local_list,'\n', "other_list:", other_list)
    for i in zip(local_list, other_list):
        summ += (i[1] - i[0]) / max(i)

    # take avg of sil_list and you're done!
    print("Silhouette Coefficient: ", round(summ / len(local_list), 3))


if __name__ == "__main__":
    calc_silhouette2(list2)