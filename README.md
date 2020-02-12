# Line-overlap
A library that checks if two lines overlap

# Usage
'''python

# The following points defined two lines that are parallel
p1 = Point(10,0)
q1 = Point(0,10)
p2 = Point(0,0)
q2 = Point(10,10)
Line.linesIntersect(p1, q1, p2, q2)

# The following points define two lines that are overlapped
p1 = Point(1,1)
q1 = Point(10,1)
p2 = Point(1,2)
q2 = Point(10,2)
Line.linesIntersect(p1, q1, p2, q2)

# The following points defined two lines that are parallel
p1 = Point(0,1)
q1 = Point(0,4)
p2 = Point(1,8)
q2 = Point(1,4)
Line.linesIntersect(p1, q1, p2, q2)


'''
