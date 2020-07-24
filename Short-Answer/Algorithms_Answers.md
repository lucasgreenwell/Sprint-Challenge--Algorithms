#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
linear complexity because 2/3 of the cubed time in the loop conditions is cancelled out by the quadratic being added inside of the loop body
In the worst case scenario, this algo runs O(n) times

b)
linear complexity overall, but a little bit worse. the for loop has linear time on its own and the nested while loop has logarithmic time(you can tell because the loops condition is being met exponentially quickly)
in the worst case scenario this algo runs O(n * log(n)) times

c)
linear complexity again! bunnies decreases by 1 until it reaches 0
in the worst case scenario this algo runs O(bunnies) times

## Exercise II

U
I need to find the highest floor where the egg doesn't break and can be thrown off. This value is called F for now
The challenge is to do it while throwing as few eggs as possible(as few ops as possible)
Makes a lot of sense to me, to do it in a binary, recursive fashion, removing half of the floors each time

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
This function performs in logarithmic time and space complexity. It's very much replicating a binary search approach. 
    


