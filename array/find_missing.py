'''
n(n+1)/2 gives sum of n natural numbers
'''

def find_missing(ls: list):
    n = len(ls) + 1
    sum = int((n * (n+1))/2)
    for i in ls:
        sum -= i

    print(sum)

ls = [2,4,1,8,6,3,7]
find_missing(ls)
