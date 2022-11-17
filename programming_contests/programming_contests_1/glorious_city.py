# city = [[int(i) for i in list(input())] for row in range(int(input()))]
city = [[1, 1, 1, 2], [1, 0, 0, 1], [1, 1, 0, 1], [0, 1, 1, 1]]

print(city)


start_position = (0, 0)
city_len = len(city)


unvisited_points = [(i, j) for i in range(city_len) for j in range(city_len) if city[i][j] != 0]
# paths = dict(zip(unvisited_points, (100 for _ in range(len(unvisited_points)))))
# paths = dict.fromkeys(unvisited_points)
paths = {(0, 0): 0}
print(unvisited_points)


current_pos = start_position

change_done = True
while change_done:
    change_done = False
    new_paths = {}
    for i, p in enumerate(paths):
        for j in range(i, len(unvisited_points)):
            if unvisited_points[j][0] - p[0] + unvisited_points[j][1] - p[1] == 1:
                change_done = True
                new_paths[unvisited_points[j]] = paths[p] + city[unvisited_points[j][0]][unvisited_points[j][1]]
                print(new_paths)
            # print(new_paths)
    paths = new_paths.copy()
print(paths)
print(paths.get((city_len, city_len), 'Impossible'))
