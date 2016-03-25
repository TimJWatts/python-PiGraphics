"""Colour class"""


class Colour(object):
    """RGB Colour"""

    def __init__(self, red, green, blue):
        """Call as x=Colour(R,G,B) where values between 0-255 inclusive"""
        if red < 0 or red > 255:
            raise ValueError('red needs to be between 0 and 255 inclusive')
        if green < 0 or green > 255:
            raise ValueError('green needs to be between 0 and 255 inclusive')
        if blue < 0 or blue > 255:
            raise ValueError('blue needs to be between 0 and 255 inclusive')

        self.red = red
        self.green = green
        self.blue = blue
