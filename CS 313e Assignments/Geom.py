#  File: Geom.py

#  Description: Applying object oriented programming to shapes, completing tests
#				on these shapes 

#  Student Name: Dorian Bizgan

#  Student UT EID: dab4567

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 2/1/18

#  Date Last Modified: 1/31/18

import math


class Point(object):
    # constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get distance
    def dist(self, other):
        return round(math.hypot(self.x - other.x, self.y - other.y),2)

    # get a string representation of a Point object
    def __str__(self):
        return '(' + str(self.x) + ", " + str(self.y) + ")"

    # test for equality
    def __eq__(self, other):
        tol = 1.0e-16
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

    def __lt__(self, other):
    	return(self.x < other.x and self.y < other.y)


class Circle(object):
    # constructor
    def __init__(self, radius=1, x=0, y=0):
        self.radius = radius
        self.center = Point(x, y)

    # compute cirumference
    def circumference(self):
        return 2.0 * math.pi * self.radius

    # compute area
    def area(self):
        return round(math.pi * self.radius * self.radius,2)

    # determine if point is strictly inside circle
    def point_inside(self, p):
        return (self.center.dist(p) < self.radius)

    # determine if a circle is strictly inside this circle
    def circle_inside(self, c):
        distance = self.center.dist(c.center)
        return (distance + c.radius) < self.radius



    # determine if a circle c intersects this circle (non-zero area of overlap)
    def does_intersect(self, c):
        distance = self.center.dist(c.center)
        return(distance < (c.radius + self.radius))

    # string representation of a circle
    def __str__(self):
        template = "Center:" + str(self.center) + ": %.2f" % self.radius
        return(template)


    def circumference(self):
        template = "%.2f" % (2 * math.pi * self.radius)
        return(template)

    def area_circ(self):
    	return round((math.pi * (self.radius ** 2)),2)

    

    # test for equality of radius
    def __eq__(self, other):
        tol = 1.0e-16
        return((abs(self.radius - other.radius) < tol))

    # determine the smallest circle that circumscribes a rectangle
    # the circle goes through all the vertices of the rectangle
    def circle_circumscribes(self, r):
        self.center.x = (r.ul.x + r.lr.x) / 2
        self.center.y = (r.ul.y + r.lr.y) / 2
        self.radius = math.hypot(abs((r.length()/2)), (abs(r.width())/2))
        return self

    


class Rectangle(object):
    # constructor
    def __init__(self, ul_x=0, ul_y=1, lr_x=1, lr_y=0):
        if ((ul_x < lr_x) and (ul_y > lr_y)):
            self.ul = Point(ul_x, ul_y)
            self.lr = Point(lr_x, lr_y)
        else:
            self.ul = Point(0, 1)
            self.lr = Point(1, 0)

    # determine length of Rectangle (distance along the x axis)
    def length(self):
        return(abs(self.lr.x - self.ul.x))

    # determine width of Rectangle (distance along the y axis)
    def width(self):
        return(abs(self.ul.y - self.lr.y))
    # determine the perimeter
    def perimeter(self):
        return(self.width() * 2 + self.length() * 2)
    # determine the area
    def area(self):
        return(self.width() * self.length())
    # determine if a point is strictly inside the Rectangle
    def point_inside(self, p):
        return((p.x < self.lr.x and p.x > self.ul.x) and (p.y > self.lr.y and p.y < self.ul.y))

    def __lt__(self, other):
        return(self.ul < other.ul and self.lr < other.lr)

    # determine if another Rectangle is strictly inside this Rectangle
    def rectangle_inside(self, other):

        return other.ul == self.ul and self.lr == other.lr or\
        self.point_inside(other.ul) or self.point_inside(other.lr) or other.point_inside(self.ul) or other.point_inside(self.lr) or\
        other.ul.x < self.ul.x < other.lr.x and self.ul.y > other.ul.y > self.lr.y or\
        self.ul.x < other.ul.x < self.lr.x and other.ul.y > self.ul.y > other.lr.y

    # determine if two Rectangles overlap (non-zero area of overlap)
    def does_intersect(self, other):
        if self.ul.x < other.lr.x or other.lr.y > self.lr.y:
            return (True)
        else:
        	return (False)

    # determine the smallest rectangle that circumscribes a circle
    # sides of the rectangle are tangents to circle c
    def rect_circumscribe(self, c):
        self.ul.x = c.center.x - c.radius
        self.ul.y = c.center.y + c.radius
        self.lr.x = c.center.x + c.radius
        self.lr.y = c.center.y - c.radius
        return(self)

    # give string representation of a rectangle
    def __str__(self):
        template = 'UL: {0.ul} : {0.lr}'
        return template.format(self)
    def square_center(self):
        return(((self.ul.x + self.lr.x) / 2),((self.ul.y + self.lr.y) / 2))

    # determine if two rectangles have the same length and width
    def __eq__(self, other):
        tol = 1.0e-16
        return((self.length - other.length < tol) and (self.width - other.width < tol ))

def main():

# open the file geom.txt
    shapes = open("geom.txt", "r")

# create Point objects P and Q
    p = shapes.readline()
    p = p.split(" ")
    p = Point(float(p[0]),float(p[1]))

    q = shapes.readline()
    q = q.split(" ")
    q = Point(float(q[0]),float(q[1]))


#print the Coordinates of P and Q
    print()
    print("Coordinates of P:", p)
    print("Coordinates of Q:", q)


# find the distance between the points P and Q
    print("Distance between P and Q:",p.dist(q))

# create two Circle objects C and D
    c = shapes.readline()
    c = c.split(" ")
    c = Circle(float(c[2]),float(c[0]),float(c[1]))

    d = shapes.readline()
    d = d.split(" ")
    d = Circle(float(d[2]),float(d[0]),float(d[1])) 


# print C and D
    print("Circle C:" , c)
    print("Circle D:" , d)


# compute the circumference of C

    circumference_c = c.circumference()
    print("Circumference of C: ",circumference_c)


# compute the area of D
    area_d = d.area_circ()
    print("Area of D:",area_d)


# determine if P is strictly inside 
    if c.point_inside(p):
    	l = "is"
    else:
    	l = "is not"
    print("P", l, "inside C")


# determine if C is strictly inside D
    if d.circle_inside(c):
    	k = "is"
    else:
    	k = "is not"

    print("C", k, "inside D")


# determine if C and D intersect (non zero area of intersection)
#    print(c.center.x) test to see if you can call other things inside of a class 
    if c.does_intersect(d):
    	j = "does"
    else:
    	j = "does not"
    print("C", j, "intersect D")
# determine if C and D are equal (have the same radius)
    l = ""
    if c != d:
        l = "not"
    print("C is",l,"equal to D")
# create two rectangle objects G and H
    g = shapes.readline()
    g = g.split(" ")
    g = Rectangle(float(g[0]),float(g[1]),float(g[2]),float(g[3]))

    h = shapes.readline()
    h = h.split(" ")
    h = Rectangle(float(h[0]),float(h[1]),float(h[2]),float(h[3]))


# print the two rectangles G and H
    print("Rectangle G:", g)
    print("Rectangle H:", h)

# determine the length of G (distance along x axis)
    print("Length of G:", g.length())

# determine the width of H (distance along y axis)
    print("Width of H:", h.width())

# determine the perimeter of G
    print("Perimeter of G: ", g.perimeter())

# determine the area of H
    print("Area of H:", h.area())

# determine if point P is strictly inside rectangle G
    f = ""
    if not g.point_inside(p):
        f = "not"
    print("P is", f, "inside G")


# determine if rectangle G is strictly inside rectangle H
    if g < h:
    	t = ""
    else:
    	t = "not"

    print("G is " + t + " inside H")
# determine if rectangles G and H overlap (non-zero area of overlap)
    r = ""
    if not g.does_intersect(h):
    	r = "not"
    print("G does " + r +  " overlap H")
# find the smallest circle that circumscribes rectangle G
# goes through the four vertices of the rectangle
    my_circle = Circle()
    print("Circle that circumscribes G:", my_circle.circle_circumscribes(g))

# find the smallest rectangle that circumscribes circle D
# all four sides of the rectangle are tangents to the circle
    my_rect = Rectangle()
    print("Rectangle that circumscribes D:", my_rect.rect_circumscribe(d))


# determine if the two rectangles have the same length and width
    u = "not"
    if g.length() == h.length() and g.width() == h.width():
    	u = ""
    print("Rectangles G is", u, "equal to H") # accidentally typed "to" instead of "equal to"
# close the file geom.txt
    shapes.close()


main()
