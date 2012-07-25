import operator, math

class memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

@memoize
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

def get_primes(limit):
    numbers = [True] * limit
    numbers[0] = False
    numbers[1] = False

    for sieve in range(2, limit):
        if not numbers[sieve]:
            # find next prime
            continue

        yield sieve

        for x in range(sieve+sieve, limit, sieve):
            numbers[x] = False

_primes = set()
_non_primes = set()
_prime_limit = 1000000
def is_prime(x):
    if len(_primes) == 0:
        _primes.update(get_primes(_prime_limit))
    if x in _primes:
        return True
    if x in _non_primes or x < _prime_limit:
        return False

    if x % 3 == 0 or x % 2 == 0:
        _non_primes.add(x)
        return False

    for d in range(6, int(math.sqrt(x)), 6):
        if x % (d+1) == 0 or x % (d-1) == 0:
            _non_primes.add(x)
            return False

    _primes.add(x)
    return True

def gcd(a, b):
    if a > b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def lcd(a, b):
    return a * b / gcd(a, b)
