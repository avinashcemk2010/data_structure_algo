def find_min(ls: list):
    min = ls[0]
    for i in ls:
        if(i < min):
            min = i

    print(min)

find_min([1,2,3,4,4,5,32,9,-4,7])