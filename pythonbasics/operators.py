def arithematic(a,b):
    print("arithmetic:")
    print(a+b)
    if(a>b):
        print(a-b)
    else:
        print(b-a)
    print(a*b)
    print(a**b)
    print(a/b)
    print(a%b)

def logical(a,b):
    print("logical:")
    print(a or b)
    print(a and b)
    print(not a)

def comparison(a,b):
    print("comparison:")
    if(a>b):
        print("a is greater")
    if(a<b):
        print("b is greater")
    if(a==b):
        print("both are equal")

def bitwise(a,b):
    print("bitwise:")
    print(a & b) #and
    print(a | b) #or
    print(a ^ b) #xor
    print(~a) #not
    print(a<<1) #left shift
    print(a>>1) #right shift

arithematic(2,4)
logical(1,0)
comparison(3,2)
comparison(2,3)
comparison(2,2)
bitwise(6,3)#6-->110,3-->011