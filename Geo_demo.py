import Geo_2D

shapes = {
    1: 'Square',
    2: 'Rectangle',
    3: 'Triangle_BH',
    4: 'Triangle_SSS',
    5: 'Trapezoid',
    6: 'Circle',
}

for i in range(1, len(shapes)+1):
    print(i, '-', shapes[i])

choice = int(input('Enter between 1-%d: ' % len(shapes)))

print('Welcome to the %s Calculator.' % shapes[choice])

if shapes[choice] == 'Square':
    base = float(input('Base = '))
    print('Area = ', Geo_2D.Square(base).area())
    print('Perimeter = ', Geo_2D.Square(base).perimeter())

elif shapes[choice] == 'Rectangle':
    base = float(input('Base = '))
    height = float(input('Height = '))
    print('Area = ', Geo_2D.Rectangle(base, height).area())
    print('Perimeter = ', Geo_2D.Rectangle(base, height).perimeter())

elif shapes[choice] == 'Triangle_BH':
    base = float(input('Base = '))
    height = float(input('Height = '))
    print('Area = ', Geo_2D.Triangle_BH(base, height).area())
    print('Perimeter = ', Geo_2D.Triangle_BH(base, height).perimeter())

elif shapes[choice] == 'Triangle_SSS':
    s_1 = float(input('Side_1 = '))
    s_2 = float(input('Side_2 = '))
    s_3 = float(input('Side_3 = '))
    print('Area = ', Geo_2D.Triangle_SSS(s_1, s_2, s_3).area())
    print('Perimeter = ', Geo_2D.Triangle_SSS(s_1, s_2, s_3).perimeter())

elif shapes[choice] == 'Trapezoid':
    top = float(input('Top = '))
    bottom = float(input('Bottom = '))
    height = float(input('Height = '))
    print('Area = ', Geo_2D.Trapezoid(top, bottom, height).area())
    print('Perimeter = ', Geo_2D.Trapezoid(top, bottom, height).perimeter())

elif shapes[choice] == 'Circle':
    radius = float(input('Radius = '))
    print('Area = ', Geo_2D.Circle(radius).area())
    print('Perimeter = ', Geo_2D.Circle(radius).circumference())
