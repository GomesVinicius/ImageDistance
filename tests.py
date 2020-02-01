from PIL import Image, ImageColor

#i1 = Image.open('images/left_50x50.png').convert('LA') / i1.save('images/g_left_50x50.png')
img1 = Image.open('images/g_left_50x50.png')
img2 = Image.open('images/g_right_50x50.png')

px1 = img1.load()
px2 = img2.load()
soma = 0
euclidean = []

for x in range(2):#img1.width):
    for y in range(2):#img1.height):
        a, b = px1[x, y]
        print('Valor de a: ', a)
        print('Valor de b: ', b)
        c, d = px2[x, y]
        print('Valor de c: ', c)
        print('Valor de d: ', d)
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

        calculo = ((((c - a) ** 2) + ((d - b) ** 2)) ** 0.5)

        euclidean.append(calculo)
        print(euclidean)
        soma = sum(euclidean)

print('Resultado:', soma)
