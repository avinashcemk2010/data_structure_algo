def pallindrome(st: str):
    i = 0
    j = len(st) - 1

    while(i <= j):
        if st[i] != st[j]:
            return 'not pallindrome'
        
        i += 1
        j -= 1

    return 'pallindrome'

st = 'madam'
result = pallindrome(st)
print(result)
    
