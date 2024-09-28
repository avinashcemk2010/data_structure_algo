def move_zeroes(ls: list):
    
    j = 0
    for i in range(len(ls)):
        if(ls[i] != 0 and ls[j] == 0):
            temp = ls[i]
            ls[i] = ls[j]
            ls[j] = temp

        if(ls[j] != 0):
            j += 1

    print(ls)

ls = [5,7,0,0,1,0,4,6]
move_zeroes(ls) 