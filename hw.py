def possible(maze, x, y, visited):
    n = len(maze)
    return (0 <= x < n and 0 <= y < n and
            maze[x][y] == 1 and not visited[x][y])

def solvemaze(maze, x, y, visited):
    n = len(maze)
    
    if x == n - 1 and y == n - 1:
        return True

    visited[x][y] = True

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if possible(maze, nx, ny, visited):
            if solvemaze(maze, nx, ny, visited):
                return True

    visited[x][y] = False
    return False


maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

n = len(maze)
visited = [[False] * n for _ in range(n)]

if maze[0][0] == 1 and solvemaze(maze, 0, 0, visited):
    print("Possible to move out of the maze")
else:
    print("Not possible to move out of the maze")