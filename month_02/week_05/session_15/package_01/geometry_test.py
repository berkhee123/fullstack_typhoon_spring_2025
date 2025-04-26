"""geometry paketiig turshih."""

# Paketiig importloh 
import geometry
from geometry import shapes, utils

# Klassuudiig shuud ashiglah ( init.py-d importloson uchir)
circle - geometry.Circle(5, 3, 4)
print(f"Toirgiin talbai: {circle.area():.2f}")
print(f"Toirgiin perimetr: {circle.perimeter():.2f}")
print(
    f"""Toirgiin tovoos koordinatiin ehlel hurtelh zai:
    {circle.distance_from_origin():.2f}"""
)

# Todorhoi modulias importloh 

rect = shapes.Rectangle(4, 6)
print(f"Tegsh ontsogtiin talba: {rect.area()}")
print(f"Tegsh ontsogtiin perimetr: {rect.perimeter()}")

# Funktsiig ashiglah 
dist = utils.distance(0, 0, 3, 4)
mid = utils.midpoint(0, 0, 6, 8)
print(f"Zai: {dist}")
print(f"Dund tseg: {mid}")



