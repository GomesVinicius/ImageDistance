from PIL import Image, ImageFilter

#i1 = Image.open('images/left_50x50.png').convert('LA') / i1.save('images/g_left_50x50.png')
img1 = Image.open('images/g_left_50x50.png')
img2 = Image.open('images/g_right_50x50.png')
img1_filter = img1.filter(ImageFilter.SHARPEN)
img2_filter = img2.filter(ImageFilter.SHARPEN)


px1 = img1_filter.load()
px2 = img2_filter.load()
#px1 = img1.load()
#px2 = img2.load()
soma = 0
euclidean = []
parte1 = []
parte2 = []

for x in range(2):#img1.width):
    for y in range(2):#img1.height):
        a, b = px1[x, y]
        print('Valor de A: ', a)
        print('Valor de B: ', b)
        c, d = px2[x, y]
        print('Valor de C: ', c)
        print('Valor de D: ', d)
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        parte1.append(((c - a) ** 2))
        parte2.append(((d - b) ** 2))
        print()

print('Parte 1: ', sum(parte1), '\nParte 1: Valor array:' , parte1)
print()
print('Parte 2: ', sum(parte2), '\nParte 2: Valor array: ', parte2)
euclidean = ((sum(parte1) + sum(parte2)) ** 0.5)
print()
print('Resultado:', euclidean)
