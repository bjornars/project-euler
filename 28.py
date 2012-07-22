def spiral():
    step = 0
    gen = 1
    yield 1
    while 1:
        step += 2
        for x in range(4):
            gen += step
            yield gen

def gen(size):
    total = 0
    for each in spiral():
        if each > size*size: break
        total += each
    return total

print gen(1001)
