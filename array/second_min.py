import sys
def second_max(ls: list):
    max = -sys.maxsize-1
    second_max = -sys.maxsize-1

    for i in ls:
        if(i > max):
            second_max = max
            max = i
        elif(i > second_max and i != max):
            second_max = i

    return max, second_max


ls = [1,3,4,4,56,56,78,4]
max, second_max = second_max(ls)
print(f'max:{max}, second_max:{second_max}')