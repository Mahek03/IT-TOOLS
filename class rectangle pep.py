class Rectangle:
    def CalculateArea(self):
        self.width=int(input("Enter Length:"))
        self.height=int(input("Enter breadth:"))
        area=self.width*self.height
        print(area)
        return (area)
    def CalculatePerimeter(self):
        perimeter=2*(self.width+self.height)
        print(perimeter)
        return (perimeter)
c=Rectangle()
x=c.CalculateArea()
y=c.CalculatePerimeter()
print("Area of rectangle is=%f"%(x))
print("Perimeter of rectangle is=%f"%(y))

