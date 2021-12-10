lines = list(map(str.strip, open("2021/day9/input.txt").readlines()))

heights = [[int(x) for x in lines[i]] for i in range(len(lines))]

row_limit = len(heights)
column_limit = len(heights[0])
 
def get_adjacent_indices(i, j, m, n):
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i-1,j))
    if i+1 < m:
        adjacent_indices.append((i+1,j))
    if j > 0:
        adjacent_indices.append((i,j-1))
    if j+1 < n:
        adjacent_indices.append((i,j+1))
    return adjacent_indices

low_points = []
low_points_coords = []
for x in range(len(heights[0])):
    for y in range(len(heights)):
        el = heights[y][x]
        neighbours = get_adjacent_indices(x,y,column_limit,row_limit)
        neighbour_heights = [heights[n[1]][n[0]] for n in neighbours]
        if el < min(neighbour_heights):
            low_points.append(el)
            low_points_coords.append((x,y))

risk_levels = list(map(lambda x: x + 1, low_points))
part_i = sum(risk_levels)
print(f"Part I: {part_i}")

def basin(point, visited):
    global basin_size
    basin_size += 1
    x,y = point
    el = heights[y][x]
    neighbours = get_adjacent_indices(x,y,column_limit,row_limit)
    neighbours = list(set(neighbours) - set(visited))
    flowing_neigbours= list(filter(lambda x: heights[x[1]][x[0]] > el and heights[x[1]][x[0]] < 9, neighbours))
    visited.extend(flowing_neigbours)
    for x in flowing_neigbours:
        basin(x,visited)
        

basins = []
basin_size=0
for x in low_points_coords:
    basin(x,[])
    basins.append(basin_size)
    basin_size = 0
basins.sort(reverse=True)

top_three = basins[0:3]
total = 1
for x in top_three:
    total *= x 
print(f"Part 2: {total}")

