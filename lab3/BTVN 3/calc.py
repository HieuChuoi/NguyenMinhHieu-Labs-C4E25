# input
# process
# output

# x = int(input("x = "))
# y = int(input("y = "))
# pheptinh = input("pheptinh: ")

def eval(x, y, pheptinh):
    result = 0

    if pheptinh == "+":
        result = x + y
    elif pheptinh == "-":
        result = x - y
    elif pheptinh == "*":
        result = x * y
    elif pheptinh == "/":
        result = x /y
    
    return(result)

# a = int(input("a = "))
# b = int(input("b = "))
# op = input("op = ")

# r = eval(a, b, op)
# print(r)

# print(result)



# FUNCTION

# def sayHi(n):
#     print("Hi")
#     print("Hi", n)
#     print("Bye Bye")

# sayHi("Quan")
# sayHi("Linh")



# def add(x, y):
#     r = x + y
#     return r    

# s = add(3, 4)
# print(s)

# t = add(6, 7)
# print(t)
