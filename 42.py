import lib
data = map(lambda x:x[1:-1], open("42.txt").read().split(','))
triangles = [lib.triangular(each) for each in range(50)]

def is_triangular(word):
    return lib.word_score(word) in triangles

print len(filter(is_triangular, data))
