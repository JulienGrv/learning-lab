"""Lesson 1."""

n = 5
p = [1 / float(n)] * n

print p

# Normalized Sense Function

# Modify the code below so that the function sense, which
# takes p and Z as inputs, will output the NON-normalized
# probability distribution, q, after multiplying the entries
# in p by pHit or pMiss according to the color in the
# corresponding cell in world.

p = [0, 1, 0, 0, 0]
world = ['green', 'red', 'red', 'green', 'green']
Z = 'green'
pHit = 0.6
pMiss = 0.2


def sense(p, Z):
    q = [a * pHit if b == Z else a * pMiss for a, b in zip(p, world)]
    sum_q = sum(q)
    q[:] = [a / sum_q for a in q]
    return q


print sense(p, Z)

# Move function


def move(p, U):
    U % len(p)
    q = p[-U:] + p[:-U]
    return q
