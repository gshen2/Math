import Geo_2D_0227

shapes = {
    1: 'Square',
    2: 'Rectangle',
    3: 'Triangle_1',
}

for i in range(1, len(shapes)+1):
    print(i, shapes[i])

choice = int(input('Enter between 1-%d: ' % (len(shapes))))

print('Welcome to the %s Calculator.' % shapes[choice])


if shapes[choice] == 'Square':
    base = float(input('Base = '))
    print('Area = ', Geo_2D_0227.Square(base).area())
    print('Perimeter = ', Geo_2D_0227.Square(base).perimeter())

elif shapes[choice] == 'Rectangle':
    base = float(input('Base = '))
    height = float(input('Height = '))
    print('Area = ', Geo_2D_0227.Rectangle(base, height).area())
    print('Perimeter = ', Geo_2D_0227.Rectangle(base, height).perimeter())

elif shapes[choice] == 'Triangle_1':
    base = float(input('Base = '))
    height = float(input('Height = '))
    print('Area = ', Geo_2D_0227.Triangle_1(base, height).area())
    print('Perimeter = ', Geo_2D_0227.Triangle_1(base, height).perimeter())
