"""Sprite class"""


import unicornhat as unicorn


class Sprite(object):
    """RGB Colour"""

    def __init__(self, arrayofarrarycolours):
        """"""
        self._pixels = arrayofarrarycolours
        self._cols = len(self._pixels)
        # Massive assumption here - need a bit of checking of all the rows.
        self._rows = len(self._pixels[0])


    def put(self, column, row):
        """ Put sprite at (column,row)"""
        # Clear pixel buffer
        c = 0
        while c < 8:
            r = 0
            while r < 8:
                unicorn.set_pixel(c, r, int(0), int(0), int(0))
                r += 1
            c += 1

        c = 0
        while c < self._cols:
            r = 0
            while r < self._rows:
                unicorn.set_pixel(column + c, row + r, \
                        self._pixels[c][r].red, \
                        self._pixels[c][r].green, \
                        self._pixels[c][r].blue)
                r += 1
            c += 1

        unicorn.show()

