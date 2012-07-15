import functools
triangle = map(lambda x: map(int, x.split()), open("67.txt").readlines())
triangle.reverse()

while 1:
    for i in range(len(triangle[1])):
        triangle[1][i] += max(triangle[0][i], triangle[0][i+1])

    if len(triangle[1]) == 1:
        print triangle[1][0]
        break

    del triangle[0]
