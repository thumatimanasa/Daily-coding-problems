#temparature conversion
def convert_temparature(temp,unit):
    if unit=='c':
        return temp*9/5+32
    elif unit=='f':
        return (temp-32)*5/9
    else:
        return None
print(convert_temparature(25,'c'))
print(convert_temparature(77,'f'))
