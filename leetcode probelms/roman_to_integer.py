#leetcode problem 13
#roman to integer

s=input('enter string')
values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
total = 0
for i in range(len(s)):
    #current value is smaller than the next value then subtract other add
    if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
        total -= values[s[i]]
    else:
        total += values[s[i]]
print(total)
