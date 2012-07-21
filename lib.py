import operator, math

def factorial(n):
    return reduce(operator.mul, range(2,n+1), 1)

def triangular(p):
    return (p * (p+1)) / 2

def num_divisors(p):
    num = 0
    square_root = int(math.ceil(math.sqrt(p))) 
    for x in xrange(1, square_root):
        if p % x == 0:
            num += 2
    if square_root * square_root == p:
        num += 1
    return num    

def divisors(p):
    div = set()
    square_root = int(math.ceil(math.sqrt(p))) 
    for x in xrange(1, square_root+1):
        if p % x == 0:
            div.add(p/x)
            div.add(x)
    if p > 1: div.remove(p)
    return div

def word_score(word):
    return sum( (ord(x) - ord('A')+1) for x in word)

