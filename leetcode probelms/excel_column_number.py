#leetcode problem 168
#Excel Sheet Column Title

def convertToTitle(columnNumber):
    result = ""
    while columnNumber > 0:
        columnNumber -= 1  
        result = chr(columnNumber % 26 + ord('A')) + result
        columnNumber //= 26
    return result


# Example usage
print(convertToTitle(1))    # A
print(convertToTitle(28))   # AB
