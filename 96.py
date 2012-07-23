import itertools

class Thing(object):
    def __init__(self, getter):
        self.c = [[False]*10 for x in range(9) ]
        self.getter = getter

    def get(self, x, y):
        return self.c[self.getter(x,y)]

def print_grid(grid):
    print '*' * 10
    for x in grid: print x

class AbortException():
    pass

def solve(row, col, box, grid, nr):
    while nr != 81:
        x = nr % 9
        y = nr / 9
        if grid[x][y] == 0:
            break
        nr += 1

    if nr == 81:
        # print_grid(grid)
        global total
        total += grid[0][0] * 100 + grid[0][1] * 10 + grid[0][2]
        raise AbortException()

    for g in range(1, 10):
        if row.get(x,y)[g] or box.get(x,y)[g] or col.get(x,y)[g]:
            continue

        box.get(x,y)[g] = True
        col.get(x,y)[g] = True
        row.get(x,y)[g] = True

        grid[x][y] = g
        solve(row, col, box, grid, nr + 1)
        grid[x][y] = 0

        box.get(x,y)[g] = False
        row.get(x,y)[g] = False
        col.get(x,y)[g] = False

def start_solve(grid):
    print_grid(grid)
    boxs = Thing(lambda x,y: (y/3) + (x/3 * 3))
    rows = Thing(lambda x,y: y)
    cols = Thing(lambda x,y: x)
    for x,y in itertools.product(range(9), range(9)):
        if grid[x][y] > 0:
            for e in boxs, rows, cols:
                e.get(x, y)[grid[x][y]] = True
    solve(rows, cols, boxs, grid, 0)

data = open("96.txt").readlines()
grids = [data[x+1:x+10] for x in range(0, len(data), 10)]

total = 0
for grid in grids:
    grid = [map(int, x.strip()) for x in grid]
    try:
        start_solve(grid)
    except AbortException:
        pass

print total
