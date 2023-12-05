a = int(input("Enter the value of first angle: "))
b = int(input("Enter the value of second angle: "))
c = int(input("Enter the value of third angle: "))
if(a<=90 and b<=90 and c<=90 and a + b + c ==180):
    if(a == b == c):
        print("Equilateral triangle")
    elif(a == b or b == c or c == a):
        print("Isoscekes triangle")
    else:
        print("Scalene triangle")
else:
    if(a + b + c ==180):
        print("Given triangle is an obtuse angled triangle.")
    else:
        print("It is not a valid triangle.")