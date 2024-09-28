def reverse_string_array(ls: list):
    i = 0
    j = len(ls)-1 
    while(i <= j):
        temp = ls[i]
        ls[i] = ls[j]
        ls[j] = temp
        i += 1
        j -= 1

    print(ls)


reverse_string_array(['s','t','r','i','n','g'])