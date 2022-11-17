def get_distance(data1, data2):
    data1 = [int(i) for i in '1 3 5 6 10 21 22'.split()]
    data2 = [c for c in 'r g b w w r g'.split()]

    data = list(zip(data1, data2))
    dist = 0
    i = 0
    j = len(data) - 1

    while dist < data[j][0] - data[i][0]:
        for x in range(i, j):
            if data[x][1] == data[j][1]:
                temp_res = data[j][0] - data[x][0]

                if temp_res > dist:
                    dist = temp_res
        j -= 1

    return dist



