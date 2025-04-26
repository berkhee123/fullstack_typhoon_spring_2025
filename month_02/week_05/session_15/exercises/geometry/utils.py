"""Geometriin dursuudiig asuulsan moduli."""

import math

 # *(x1, y1)
 # \
 #  \C
 #   \
 #    B(x2, y2)


def distance(x1, x2, y1, y2):
    """Xoyr tseg hoorondiin zai."""
    return math.sqrt ((x2 -x1) ** 2 + (y2 - y1) **2)

def midpoint(x1, x2, y1, y2):
    """Xoyr tsegiin dund tseg."""
    return((x1 + x2) / 2, (y1 + y2) / 2)
    