'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
#https://www.geeksforgeeks.org/count-occurrences-of-a-substring-recursively/
def count_th(word):
    if len(word) < 2:
        #base case when you've chopped up the input too much
        return 0
    if word[0:2] == 'th':
        #adds one to the count and reccurses is it found a match
        return count_th(word[1:]) + 1
    else:
        #recurses without a count increase because there were no matches
        return count_th(word[1:])

