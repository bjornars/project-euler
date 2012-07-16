import functools
square = map(lambda x: map(int, x.split(',')), open("81.txt").readlines())

def get_diag(row, data):
    l = len(data)
    start = 0
    stop = l
    if row >= l:
        start = row - l + 1
    else:
        stop = row + 1 

    return [data[row-x][x] for x in range(start, stop)]

# turn the square into a diamond
diamond = []
for x in range(len(square) * 2 - 1):
    diamond.append(get_diag(x ,square))

diamond.reverse()

# and use a modified version of #67
while 1:
    l = len(diamond[1])
    if len(diamond[0]) > l: 
        for i in range(l):
            diamond[1][i] += min(diamond[0][i], diamond[0][i+1])
    else:
        diamond[1][0] += diamond[0][0]
        diamond[1][l-1] += diamond[0][l-2]
        for i in range(1,l-1):
            diamond[1][i] += min(diamond[0][i], diamond[0][i-1])

    if l == 1:
        print diamond[1][0]
        break

    del diamond[0]
