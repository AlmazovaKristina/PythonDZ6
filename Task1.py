import math
q = 0
ax = int(input('Введите координату X первой точки:'))
ay = int(input('Введите координату Y первой точки:'))
az = int(input('Введите координату Z первой точки:'))
bx = int(input('Введите координату X второй точки:'))
by = int(input('Введите координату Y второй точки:'))
bz = int(input('Введите координату Z второй точки:'))

sqrt = lambda ax,ay,az,bx,by,bz: math.sqrt((bx - ax) ** 2 + (by - ay) ** 2 + (bz - az) ** 2)
print('%.2f' % sqrt(ax,ay,az,bx,by,bz))

