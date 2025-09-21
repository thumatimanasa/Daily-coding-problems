#leetcode problem 1071
#Greatest common divisor of strings

import math
def gcd_of_strings(str1,str2):
    if str1+str2!=str2+str1:
        return ""
    else:
        gcd_len=math.gcd(len(str1),len(str2))
        return str1[:gcd_len]
print(gcd_of_strings("ababab","ab"))
