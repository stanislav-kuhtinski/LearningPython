__author__ = 'stanislav-kuhtinski'

import math


class Shape(object):
    def __init__(self, *sides):
        number_of_sides = len(sides)

        if (number_of_sides < 1) and (number_of_sides > 4):
            raise ValueError('Error, cannot init the figure, sides quantity should be from 2 to 4')
        else:
            if number_of_sides == 1:
                self.sides = [n for n in sides] * 4  # Using list comprehension <listcomp>
            elif number_of_sides == 2:
                self.sides = [n for n in sides] * 2
            else:
                self.sides = [n for n in sides]

    def get_object_perimeter(self):
        return sum(self.sides)

    def print_sides(self, comment='Sides are'):
        print(comment, ' sides are: ', self.sides)

    def print_perimeter(self, figure_name='figure'):
        print('The perimeter of the {} is {}'.format(figure_name, self.get_object_perimeter()))


class Rectangle(Shape):
    def calculate_area(self):
        return self.sides[0] * self.sides[1]

    def print_rectangle_area(self):
        print('Area of a Rectangle is {}'.format(self.calculate_area()))


class Square(Rectangle):  # Square is a special kind of rectangle
    def print_square_area(self):
        print('Area of a Square is {}'.format(self.calculate_area()))


class Triangle(Shape):
    def __init__(self, *sides):
        number_of_sides = len(sides)
        if number_of_sides != 3:
            raise ValueError('Error, cannot init a triangle!')
        else:
            self.sides = [n for n in sides]

        self.sides.sort()

        larger_side = self.sides[len(self.sides) - 1]  # The last side is the largest
        two_sides_sum = self.sides[0] + self.sides[1]

        if two_sides_sum <= larger_side:
            raise ValueError(
                'Error, cannot init a triangle!')

    def calculate_area(self):
        half_perimeter = self.get_object_perimeter() / 2
        return math.sqrt(
            half_perimeter * (half_perimeter - self.sides[0]) * (half_perimeter - self.sides[1]) * (
                    half_perimeter - self.sides[2]))

    def print_triangle_area(self):
        print('Area of a Triangle is {}'.format(self.calculate_area()))


class Polygon(Shape):
    def __init__(self, *sides):
        number_of_sides = len(sides)
        if number_of_sides != 4:
            raise ValueError('Error, cannot init a Polygon!')
        else:
            self.sides = [n for n in sides]

        self.sides.sort()

        larger_side = self.sides[len(self.sides) - 1]  # The last side is the largest
        three_sides_sum = self.sides[0] + self.sides[1] + self.sides[2]

        if three_sides_sum <= larger_side:
            raise ValueError(
                'Error, cannot init a Polygon!')

    def calculate_area(self):
        return ('Cannot be calculated')

    def print_triangle_area(self):
        print(self.calculate_area())


rect = Rectangle(1, 2)
rect.print_sides('Reactangle')
rect.print_perimeter('Reactangle')
rect.print_rectangle_area()

print('\n')
sqr = Square(5)
sqr.print_sides('Square')
sqr.print_perimeter('Square')
sqr.print_square_area()

print('\n')
sqr = Triangle(3, 5, 4)
sqr.print_sides('Triangle')
sqr.print_perimeter('Triangle')
sqr.print_triangle_area()

print('\n')
plgn2 = Polygon(5, 2, 4, 7)
plgn2.print_sides('Polygon')
plgn2.print_perimeter('Polygon')
plgn2.print_triangle_area()