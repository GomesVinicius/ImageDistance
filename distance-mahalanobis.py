#Desvio Padrão tem que achar a variancia antes
#Variancia tem que pegar a média
#Variancia tem que diminuir a posição pela média e elevar ao 2
#Variancia tem que pegar este resultado e dividir pela media menos um (media - 1)
#Desvio Padrão é a raiz da variancia

from PIL import Image

#i1 = Image.open('images/left_50x50.png').convert('LA') / i1.save('images/g_left_50x50.png')
img1 = Image.open('images/g_left_50x50.png')
img2 = Image.open('images/g_right_50x50.png')

px1 = img1.load()
px2 = img2.load()
px1_x = []
px1_y = []
px2_x = []
px2_y = []
for x in range(2):#img1.width):
    for y in range(2):#img1.height):
        a, b = px1[x, y]
        c, d = px2[x, y]

        px1_x.append(a)
        px1_y.append(b)
        px2_x.append(c)
        px2_y.append(d)

media_px1_x = sum(px1_x) / len(px1_x) #len(img)
media_px1_y = sum(px1_y) / len(px1_y) #len(img)
media_px2_x = sum(px2_x) / len(px2_x) #len(img)
media_px2_y = sum(px2_y) / len(px2_y) #len(img)

v_px1_x = []
v_px1_y = []
v_px2_x = []
v_px2_y = []
for x in range (len(px1_x)):
    v_px1_x.append((px1_x[x] - media_px1_x) ** 2)
    v_px1_y.append((px1_y[x] - media_px1_y) ** 2)
    v_px2_x.append((px2_x[x] - media_px2_x) ** 2)
    v_px2_y.append((px2_y[x] - media_px2_y) ** 2)

variancia_1_x = sum(v_px1_x) / (len(px1_x) - 1)
variancia_1_y = sum(v_px1_y) / (len(px1_y) - 1)
variancia_2_x = sum(v_px2_x) / (len(px2_x) - 1)
variancia_2_y = sum(v_px2_y) / (len(px2_y) - 1)

desvio_padrao_1_x = variancia_1_x ** 0.5
desvio_padrao_1_y = variancia_1_y ** 0.5
desvio_padrao_2_x = variancia_2_x ** 0.5
desvio_padrao_2_y = variancia_2_y ** 0.5

#Mahalanobis acaba de começar:
#raiz((x - media)² / desvio_padrao²)

mahalanobis_1_x = (((sum(px1_x) - media_px1_x) ** 2) / ((desvio_padrao_1_x) ** 2) ** 0.5)
#mahalanobis_1_y = (((sum(px1_y) - media_px1_y) ** 2) / ((desvio_padrao_1_y) ** 2) ** 0.5)
mahalanobis_2_x = (((sum(px2_x) - media_px2_x) ** 2) / ((desvio_padrao_2_x) ** 2) ** 0.5)
#mahalanobis_2_y = (((sum(px2_y) - media_px2_y) ** 2) / ((desvio_padrao_2_y) ** 2) ** 0.5)
print(mahalanobis_1_x)
print(mahalanobis_2_x)
