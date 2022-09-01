pi = 3.1415926 #The value of pi

#r will be provided by the user, r is radius

r = int(input("Enter the radius of circle: "))

#area = pi*(r^2)
area = pi*(r*r)

#following line will round to 2
area = round(area,2)

#Printing the area of circle
print("The area of the circle is: ",area)