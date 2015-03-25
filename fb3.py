from collections import deque

def preprocess(grid):
    R = len(grid)
    C = len(grid[0])
    obstacles = set([])
    dangers = set([])
    for i in range(R):
        for j in range(C):
            cell = grid[i][j]
            if cell == '#':
                obstacles.add((i, j))
            if cell == 'S':
                start = (i, j)
            if cell == 'G':
                goal = (i, j)
            if cell in "<^>v":
                obstacles.add((i, j))
                # to the left
                for b in range(j - 1, -1, -1):
                    if grid[i][b] in "#<^>v":
                        break
                    dangers.add((i, b, "<v>^".find(cell)))
                # to the right
                for b in range(j + 1, C, +1):
                    if grid[i][b] in "#<^>v":
                        break
                    dangers.add((i, b, ">^<v".find(cell)))
                # to the top
                for a in range(i - 1, -1, -1):
                    if grid[a][j] in "#<^>v":
                        break
                    dangers.add((a, j, "^<v>".find(cell)))
                # to the bottom
                for a in range(i + 1, R, +1):
                    if grid[a][j] in "#<^>v":
                        break
                    dangers.add((a, j, "v>^<".find(cell)))
    return (R, C, start, goal, obstacles, dangers)

def bfs(R, C, start, goal, obstacles, dangers):
    done = {(start[0], start[1], 0): 0}
    frontier = deque([(start[0], start[1], 0)])
    while frontier:
        i, j, stepmod4 = frontier.popleft()
        if (i, j) == goal:
            return done[(i, j, stepmod4)]
        for (di, dj) in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
            new_i = i + di
            new_j = j + dj
            new_stepmod4 = (stepmod4 + 1) % 4
            if (new_i, new_j, new_stepmod4) in done:
                continue
            if new_i < 0 or new_i >= R or new_j < 0 or new_j >= C:
                continue
            if (new_i, new_j) in obstacles:
                continue
            if (new_i, new_j, new_stepmod4) in dangers:
                continue
            done[(new_i, new_j, new_stepmod4)] = done[(i, j, stepmod4)] + 1
            frontier.append((new_i, new_j, new_stepmod4))
    return None

def do_case(case_num, grid):
    (R, C, start, goal, obstacles, dangers) = preprocess(grid)
    result = bfs(R, C, start, goal, obstacles, dangers)
    if result:
        print "Case #%d: %d" % (case_num, result)
    else:
        print "Case #%d: impossible" % case_num

def main():
    T = int(raw_input())
    for case_num in range(1, T + 1):
        R, C = map(int, raw_input().split())
        grid = []
        for i in range(R):
            grid.append(raw_input().strip())
        do_case(case_num, grid)

if __name__ == "__main__":
    main()