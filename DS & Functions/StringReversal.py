def Reverse(str):
    if len(str) == 0:
        return str
    return str[len(str)-1] + Reverse(str[0:len(str)-1])

str = "hello world"
print(Reverse(str))
print(Reverse(Reverse(str)))