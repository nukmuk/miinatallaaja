import math


def calculate_square_area(side_length):
    return side_length**2


def calculate_sector_area(radius, angle):
    return math.pi * radius**2 * angle / 360


def calculate_catheti_length(hypotenuse):
    return hypotenuse / math.sqrt(2)


def calculate_figure_area(x):
    square = calculate_square_area(x)
    triangle = calculate_square_area(calculate_catheti_length(x)) / 2
    circle = calculate_sector_area(calculate_catheti_length(x), 45)
    square2 = calculate_square_area(2 * calculate_catheti_length(x))
    circle2 = calculate_sector_area(2 * calculate_catheti_length(x), 270)
    return square + circle + square2 + circle2 + triangle


# def calculate_figure_area(x):
# all calculations to get the area of the figure
# are done inside this function, using the
# other functions for intermediate results

# main program that prompts for x,
# calls the calculation function and
# prints the rounded result

a = float(input())
# b = float(input())
print(round(calculate_figure_area(a), 4))
