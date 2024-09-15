phi = 3.142
radius = int(input("Enter radius of the circle: "))
if radius >= 1:
    area = phi * pow(radius, 2)
    Circumference = 2 * phi * radius
    print("Area of the circle is", area)
    print("Circumference of circle is", Circumference)  
else:
    print("Invalid value for Radius of the circle")
