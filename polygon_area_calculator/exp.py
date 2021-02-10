class Rectangle:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def __repr__(self):
        return f"Rectangle(width={self.__width}, height={self.__height})"

    def set_width(self, value):
        self.__width = value

    def get_width(self):
        return self.__width

    def set_height(self, value):
        self.__height = value

    def get_height(self):
        return self.__height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * self.__width + 2 * self.__height

    def get_diagonal(self):
        return (self.__width ** 2 + self.__height ** 2) ** .5

    def get_picture(self):
        if self.__width > 50 or self.__height > 50:
            return 'Too big for picture.'
        picture = str()
        for row in range(self.__height):
            picture += '*'*self.__width + '\n'
        return picture

    def get_amount_inside(self, shape):
        if shape.get_width() > self.__width or shape.get_height() > self.__height:
            return 0
        x_axis_possibilities = self.__width // shape.get_width()
        y_axis_possibilities = self.__height // shape.get_height()
        amount = max(x_axis_possibilities, y_axis_possibilities)
        print(amount)
        return amount


class Square(Rectangle):

    def __init__(self, side):
        self.__side = side
        super().__init__(side, side)

    def __repr__(self):
        return f"Square(side={self.__side})"

    def set_side(self, side):
        self.__side = side
        super().set_width(side)
        super().set_height(side)

    def get_width(self):
        return self.__side


sq = Square(2)
print(sq)
print(sq.get_picture())

sq = Square(5)
print(sq)
print(sq.get_picture())

sq = Square(3)
print(sq)
print(sq.get_picture())


sq.set_side(2)
print(sq)
print(sq.get_width())
print(sq.get_picture())

sq.set_side(5)
print(sq)
print(sq.get_width())
print(sq.get_picture())

sq.set_side(3)
print(sq)
print(sq.get_width())
print(sq.get_picture())

sq.set_width(2)
print(sq)
print(sq.get_width())
print(sq.get_picture())
