from math import floor, sqrt
import operator

def factor(num):
    factors = []
    num_prime = num
    max = int(floor(sqrt(num)))
    for x in range(2, max):
        while 1:
            if num % x == 0:
                factors.append(x)
                num /= x
            else:
                break

    assert reduce(operator.mul, factors, 1) == num_prime
    return factors

a = 600851475143L
print "The factors of %d are %s"  % (a ,", ".join([str(x) for x in factor(a)]))
