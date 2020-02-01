#|x1 - x2| + |y1 - y2|
from PIL import Image

img1 = Image.open('images/g_left_50x50.png')
img2 = Image.open('images/g_left_50x50.png')

px1 = img1.load()
px2 = img2.load()
v_px1 = []
v_px2 = []
soma = []

for x in range(2):#img1.width):
    for y in range(2):#img1.height):
        a, b = px1[x, y]
        c, d = px2[x, y]
        print(px1[x, y])
        print(px2[x, y])
        dist_px1 = abs(a - b)
        dist_px2 = abs(c - d)
        print()
        calculo = dist_px1 + dist_px2
        soma.append(calculo)

print('Distancia: ', sum(soma))
