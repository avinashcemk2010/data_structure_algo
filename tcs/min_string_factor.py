'''
Malvika is very found of strings, so whenever she gets time she keeps herself engaged in strings.
One day she was given string x and y and asked to form x from y. the rules for forming the string are given below
The string x should be formed with the concatenations of substring of y. she can also select substring from y in reverse order.
Length of substring selected from y should be greater than 0
Aim is to minimise number of substrings that are selected from y and concatenate to form x
A term string factor is defined which is calculated as (number of substring selected from y)*s + (number of substring selected from reverse y)*r where s and r are given input
You also have to minimise the string factor while maintaining minimum number of substrings 
Given two integers s and r and two strings x and y, find the minimum string factor of the string x following above rules
'''

def min_string_factor(x, y, s, r):
    n = len(x)
    m = len(y)
    
    # dp[i] will store the minimum string factor to form x[0:i]
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # No cost to form the empty string

    for i in range(1, n + 1):
        for j in range(m):
            for k in range(j + 1, m + 1):
                # Get normal and reversed substrings from y
                normal_sub = y[j:k]
                reversed_sub = normal_sub[::-1]
                
                # Check if x[i-(k-j):i] matches normal_sub or reversed_sub
                if i - (k - j) >= 0 and x[i-(k-j):i] == normal_sub:
                    dp[i] = min(dp[i], dp[i - (k - j)] + s)
                if i - (k - j) >= 0 and x[i-(k-j):i] == reversed_sub:
                    dp[i] = min(dp[i], dp[i - (k - j)] + r)

    # The minimum string factor for the full string x
    return dp[n]



x = input()
y = input()
s, r = map(int, input().split())

print(min_string_factor(x, y, s, r))
#print(min_string_factor('niveditha', 'lavekdahnita', 3, 5))
#print(min_string_factor('abcdef', 'pafedexycbc', 4, 2))
