import math


def area(radius):
    """
    :type radius: int
    """
    return math.pi * (radius ** 2)


radius: str = input("Enter the radius for which you want ot calculate the area:")

print(f"Area is :  {area(int(radius))}")

name = "sanjay"
name.capitalize()