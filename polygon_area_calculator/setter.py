class Foo:

    def __init__(self, width, height):
        self.__width = width
        self.height = height
        self.attr = f"I am {self.__width} wide and {self.height} tall"

    def set_width(self, value):
        self.__width = value

    def get_width(self):
        return self.__width

    def set_height(self, value):
        self.__height = value

    def get_height(self):
        return self.__height

    def get_attr(self):
        return f"I am {self.__width} wide and {self.height} tall"


class Bar(Foo):

    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, value):
        super().set_width(value)
        super().set_height(value)


# foo = Foo(3, 5)
# print(foo.get_width())
# # print(foo.attr)
# print(foo.get_attr())
# foo.set_width(2)
# print(foo.get_width())
# # print(foo.attr)
# print(foo.get_attr())


bar = Bar(3)
print(bar.get_width())
# print(bar.attr)
print(bar.get_attr())
bar.set_width(2)
print(bar.get_width())
print(bar.get_attr())
bar.set_side(4)
print(bar.get_width())
# print(bar.attr)
print(bar.get_attr())
