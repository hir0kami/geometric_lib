
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
```
radius1 = 5
area1 = area(radius1)
print(f"Площадь круга с радиусом {radius1} равна {area1:.2f}")
Площадь круга: 78.54
```

- Rectangle: `S = ab`
```
length1 = 10
width1 = 5
area1 = area(length1, width1)
print(f"Площадь прямоугольника с длиной {length1} и шириной {width1} равна {area1}.")
Площадь прямоугольника: 50
```

- Square: `S = a²`
```
side1 = 4
area1 = area(side1)
print(f"Площадь квадрата со стороной {side1} равна {area1}.")
# Площадь квадрата: 16
```

- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter
```
a = 3
b = 4
c = 5
triangle_area = area(a, b, c)
print(f"Площадь треугольника со сторонами {a}, {b} и {c} равна {triangle_area:.2f}")
Площадь треугольника: 6.00
```

## Perimeter
- Circle: `P = 2πR`
```
radius = 5
result = perimeter(radius)
print(f"Периметр круга с радиусом {radius} равен {result:.2f}")
Периметр круга: 31.42
```

- Rectangle: `P = 2a + 2b`
```
length = 5  # длина
width = 3   # ширина
result = perimeter(length, width)
print(f"Периметр прямоугольника со сторонами {length} и {width} равен {result}.")
Периметр прямоугольника: 16
```

- Square: `P = 4a`
```
side_length = 5
print(perimeter(side_length)) 
Периметр квадрата: 20
```

- Triangle: `P = a + b + c`
```
side1 = 3
side2 = 4
side3 = 5
print(perimeter(side1, side2, side3))  # 12
Периметр треугольника: 12
```

## L-03
- Circle and square added (8ba9aeb)
- Docs added (d078c8d)

## L-04
- Triangle added (d080c78)
- Doc updated for triangle (51c40eb)
- Add calculate.py (d76db2a)
- Update docs for calculate.py (b5b0fae)
- Add rectangle.py (3049431)

## L-05
- Add user agreement (438b89a)
- Update docs. Add user agreement info (86edb1c)

