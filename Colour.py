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

        self._red = red
        self._green = green
        self._blue = blue


    def red(self):
        """Returns red component"""
        return self._red


    def green(self):
        """Returns green component"""
        return self._green


    def blue(self):
        """Returns blue component"""
        return self._blue


    def rgb(self):
        """Returns array of [red, green, blue] components"""
        return (self._red, self._green, self._blue)


