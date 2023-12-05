'''class circle:
    def cir(self):
        c=2*3.14*self.r
        print(c)

c1=circle()
c1.r=12
c1.cir()'''




class circle():
    def circumference(self):
        a=2*3.14*self.r
        print(a)
r1=circle()
r2=int(input("enter 1st radius of a circle: "))
r1.r = r = r2
print("circumference is",r1.circumference())
r3=circle()
r4=int(input("enter 1st radius of a circle: "))
r3.r = r = r4
print("circumference is",r3.circumference())