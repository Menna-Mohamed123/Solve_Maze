import heapq

def solve_maze(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])

    distances = {}
    for r in range(rows):
        for c in range(cols):
            distances[(r, c)] = float('inf')

    distances[start] = 0
    priority_queue = [(0, start)]

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while priority_queue:
        current_dist, (r, c) = heapq.heappop(priority_queue)

        if (r, c) == end:
            print(f"Goal {current_dist}")
            return current_dist

        for dr, dc in directions:
            new_r = r + dr
            new_c = c + dc

            if 0 <= new_r < rows and 0 <= new_c < cols and maze[new_r][new_c] == 0:
                new_dist = current_dist + 1

                if new_dist < distances[(new_r, new_c)]:
                    distances[(new_r, new_c)] = new_dist
                    heapq.heappush(priority_queue, (new_dist, (new_r, new_c)))

    print("No Way to end !")
    return -1

my_maze = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start_point = (0, 0)
end_point = (3, 3)

solve_maze(my_maze, start_point, end_point)