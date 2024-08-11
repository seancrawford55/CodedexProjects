#calculating area of different objects
import math

print ("Which shape are we using?")
print ("1\) Triangle")
print ("2\) Rectangle")
print ("3\) Square")
print ("4\) Circle")
print ("5\) Quit")

#User input the number for shape
num = int(input('Choose a shape based on number: '))

match num:
    case 1:
        #Input dimensions and calculate the area of triangle
        h = int(input('What is the height? '))
        w = int(input('what is the width? '))
        area = (h * w)/2
    
    case 2:
        #Input dimensions and calculate the area of rectangle
        h = int(input('What is the height? '))
        w = int(input('what is the width? '))
        area = (h * w)
    
    case 3:
        #Input dimensions and calculate the area of square
        h = int(input('What is the height? '))
        w = int(input('what is the width? '))
        area = (h * w)

    case 4:
        #Input the radius and calculate area of circle
        r = int(input('What is the radius of the circle? '))
        area = math.pi*(r**2)
    
    case 5:
        print ('Goodbye')
        exit

a = str(area)
print ('The area of the shape is ' + a)