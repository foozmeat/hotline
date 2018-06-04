from random import choice

from kivy.graphics.context_instructions import Color


def in_sps(value):
    return f"{value}sp"


def random_color():
    red = choice(range(0, 2))
    green = choice(range(0, 2))
    blue = choice(range(0, 2))

    return Color(red, green, blue, 0.5)
