class Circle:
#constructor with argument radius.
    def __init__(self,radius):
#radius of the circle.
        self.radius = radius
#function that calculates perimeter and returns it.
    def perimeter(self):
        return 2 * 3.14 * self.radius
#function that calculates area and returns it.
    def area(self):
        return 3.14 * self.radius * self.radius
#function that returns the string that contains the radius,perimeter and area of the called circle object
    def __str__(self):
        return "Circle with radius : {:.2f} , Perimeter : {:.2f} , Area : {:.2f}".format(self.radius,self.perimeter(),self.area())
#create two circles.
circle_one = Circle(10)
circle_two = Circle(20)
#print the two objects
print(circle_one)
print(circle_two)