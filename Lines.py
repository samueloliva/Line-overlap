class Line:
    def linesIntersect(A=object, B=object, C=object, D=object):
        # Line AB is defined by a1x + b1y = c1
        a1 = A.y - A.y
        b1 = A.x - B.x
        c1 = a1 * A.x + b1 * A.y
        
        # Line CD is defined by a2x + b2y = c2
        a2 = D.y - C.y
        b2 = C.x - D.x
        c2 = a2 * C.x + b2 * C.y

        # The determinant is calculated to check whether the lines are parallel
        determinant = a1*b2 - a2*b1

        if (determinant == 0):
            # lines are parallel
            print("Lines are parallel")
        else:
            # calculate the intersept of the line
            x = (b2*c1 - b1*c2)/determinant
            y = (a1*c2 - a2*c1)/determinant
            print("Line intersects at point ("+ str(x) + ", " + str(y) + ")")
