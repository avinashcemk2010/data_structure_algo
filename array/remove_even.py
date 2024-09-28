def remove_even(ls: list):
    i = 0
    while(i < len(ls)):
        if ls[i] % 2 == 0:
            #pop value at index i
            ls.pop(i) 
        else:
            i += 1
        
    print(ls) 

remove_even([1,2,6,4,4,4,4,4,4,4,5,6,7,45,43])