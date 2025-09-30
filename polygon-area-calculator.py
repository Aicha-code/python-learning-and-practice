class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        if new_width <= 0:
            raise ValueError("Width must be a non-negative value.")
        self.width = new_width
        

    def set_height(self, new_height):
        if new_height <= 0:
            raise ValueError("Height must be a non-negative value.")
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return ((self.width**2) + (self.height**2)) ** 0.5

    def get_picture(self):
        shape = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for i in range(self.height):
            shape += "*" * self.width + "\n"
        return shape

    def get_amount_inside(self, other):
        number = (self.width // other.width) * (self.height // other.height)
        return number

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, new_side):
        if new_side <= 0:
            raise ValueError("Side must be a non-negative value.")
        self.width = new_side
        self.height = new_side

    def set_width(self, new_width):
        if new_width <= 0:
            raise ValueError("Width must be a non-negative value.")
        self.set_side(new_width)

    def set_height(self, new_height):
        if new_height <= 0:
            raise ValueError("Height must be a non-negative value.")
        self.set_side(new_height)

    def get_picture(self):
        return super().get_picture()

    def __str__(self):
        return f"Square(side={self.width})"


def main():
    print("\nThis is a polygon area calculator built with Python, using inheritance.")
    print(
        "You can do different things by creating Rectangle and Square objects and calling their different methods.\n"
    )
    # enjoy yourself playing with the code


if __name__ == "__main__":
    main()
