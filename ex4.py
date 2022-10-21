a = int(input("a="))
b = int(input("b="))

a = a ^ b
b = a ^ b
a = a ^ b

print("After Swapping a=" + str(a) + "  b=" + str(b))
