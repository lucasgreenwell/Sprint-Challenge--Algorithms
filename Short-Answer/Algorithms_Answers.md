#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)


b)


c)

## Exercise II

U
I need to find the highest floor where the egg doesn't break and can be thrown off. This value is called F for now
The challenge is to do it while throwing as few eggs as possible(as few ops as possible)
Makes a lot of sense to me, to do it in a binary, recursive fashion

P
function takes in three parameters, n (the top of the floor range), and b (the bottom of the floor range)
declare test_floor variable as half of n
if n and b are the same:
    return n
if f is lower than test_floor (if the egg breaks):
    recurse function passing test_floor - 1 as n
if f is higher than test_floor (if the egg makes it):
    recurse function passing test_floor as b

in python
f = secrethiddenfloornumber

def max_floor(n, b):
    test_floor = n // 2
    if n == b:
        return n
    elif test_floor > f:
        return max_floor(test_floor - 1, b)
    elif test_floor <= f:
        return max_floor(n, test_floor)
    


