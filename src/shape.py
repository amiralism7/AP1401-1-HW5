class Point:
    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y
        pass
    def __str__(self):
        return f"x: {self.x}, y: {self.y}"
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def length(self):
        return (self.x**2 + self.y**2)**0.5
    pass

class Shape:
    def __init__(self) -> None:
        self.vertices = []
        
    def add_vertex(self, p:Point) -> None:
        self.vertices.append(p)
        
    def __str__(self):
        return f"number of vertices: {len(self.vertices)}"
    
    def perimeter(self) -> float:
        if len(self.vertices) == 0:
            raise RuntimeError("no vertex added yet")
        elif len(self.vertices) == 2:
            return (self.vertices[1] - self.vertices[0]).length()
        else:
            p = 0
            for i in range(len(self.vertices)):
                p += (self.vertices[i] - self.vertices[i-1]).length()
            return p

class Line(Shape):
    def __init__(self, p1:Point, p2:Point) -> None:
        Shape.__init__(self)
        self.add_vertex(p1)
        self.add_vertex(p2)
        pass

    def __str__(self):
        return f"""Line:
        p1: ({self.vertices[0].__str__()})
        p2: ({self.vertices[1].__str__()})"""

    def area(self) -> float:
        return 0


class Triangle(Shape):
    def __init__(self, p1:Point, p2:Point, p3:Point) -> None:
        Shape.__init__(self)
        area = (1/2)*(p1.x*(p2.y - p3.y) + p2.x*(p3.y - p1.y) + p3.x*(p1.y - p2.y))
        if area**2 < 0.000001:
            raise RuntimeError("vertices on one line")
        
        
        self.add_vertex(p1)
        self.add_vertex(p2)
        self.add_vertex(p3)
        pass
    def __str__(self):
        return f"""Triangle:
        p1: ({self.vertices[0].__str__()})
        p2: ({self.vertices[1].__str__()})
        p3: ({self.vertices[2].__str__()})"""
    def area(self) -> float:
        p1 = self.vertices[0]
        p2 = self.vertices[1]
        p3 = self.vertices[2]
        area = (1/2)*(p1.x*(p2.y - p3.y) + p2.x*(p3.y - p1.y) + p3.x*(p1.y - p2.y))
        return abs(area)

class Rectangle(Shape):
    def __init__(self, p1:Point, p2:Point) -> None:
        Shape.__init__(self)
        self.add_vertex(p1)
        self.add_vertex(p2)
        pass
    def __str__(self):
        p1 = Point(self.vertices[0].x, self.vertices[1].y)
        p2 = Point(self.vertices[1].x, self.vertices[0].y)
        return f"""Triangle:
        p1: ({self.vertices[0].__str__()})
        p2: ({self.vertices[1].__str__()})
        p3: ({p1.__str__()})
        p3: ({p2.__str__()})"""
    def area(self) -> float:
        return abs((self.vertices[0].x - self.vertices[1].x) * (self.vertices[0].y - self.vertices[1].y))