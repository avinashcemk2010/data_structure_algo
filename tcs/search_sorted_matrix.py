#                       j
# i-->10    20    30    40                     
#     15    25    35    45
#     27    29    37    48
#     32    33    39    51

def search(matrix, n, x):
    i = 0
    j = n-1

    while(j >= 0 and i < n):
        if matrix[i][j] == x:
            print(f' found {x} at i={i} and j={j}')
            return 

        if matrix[i][j] > x:
            j -= 1
        else:
            i += 1

    print('not found') 


matrix = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 48],
    [32, 33, 39, 51]
]

search(matrix, 4, 32)




