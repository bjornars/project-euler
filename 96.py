import itertools

class Thing(object):
    def __init__(self, getter):
        self.c = [ [] for x in range(9) ]
        self.getter = getter

    def get(self, x, y):
        return self.c[self.getter(x,y)]

    def __len__(self):
        return sum(map(len, self.c))

    def dump(self):
        return sum([sum(x) for x in self.c])

def print_grid(grid):
    print '*' * 10
    for x in grid: print x

def solve(row, col, box, grid, x, y):
    if x == 9 and y == 8:
        #print_grid(grid)
        global total
        total += grid[0][0] * 100 + grid[0][1] * 10 + grid[0][2]
        return

    if x == 9:
        return solve(row, col, box, grid, 0, y+1)

    if grid[x][y] != 0:
        return solve(row, col, box, grid, x + 1, y)

    for g in range(1, 10):
        skip = False
        for e in box, col, row:
            if g in e.get(x,y):
                skip = True
        if skip:
            continue

        #print 'trying %s for %sx%s' % (g,  x, y)
        for e in box, col, row:
            e.get(x,y).append(g)

        grid[x][y] = g
        solve(row, col, box, grid, x + 1, y)
        grid[x][y] = 0
        for e in box, col, row:
            e.get(x,y).remove(g)

def start_solve(grid):
    print_grid(grid)
    boxs = Thing(lambda x,y: (y/3) + (x/3 * 3))
    rows = Thing(lambda x,y: y)
    cols = Thing(lambda x,y: x)
    for x,y in itertools.product(range(9), range(9)):
        if grid[x][y] > 0:
            for e in boxs, rows, cols:
                e.get(x, y).append(grid[x][y])
    solve(rows, cols, boxs, grid, 0, 0)

data = open("96.txt").readlines()
grids = [data[x+1:x+10] for x in range(0, len(data), 10)]

total = 0
for grid in grids[:5]:
    grid = [map(int, x.strip()) for x in grid]
    start_solve(grid)

print total
