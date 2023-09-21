from collections import namedtuple

Colour = namedtuple("Colour", ["r", "g", "b"])

BACKGROUND = Colour(r=0, g=0, b=0)
SNAKE = Colour(r=255, g=255, b=100)
FOOD = Colour(r=255, g=0, b=65)
TEXT = Colour(r=255, g=255, b=255)
