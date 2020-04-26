from PIL import Image, ImageColor
from scipy.spatial import distance

#i1 = Image.open('images/left_50x50.png').convert('LA') / i1.save('images/g_left_50x50.png')
img1 = Image.open('images/g_left_50x50.png')
img2 = Image.open('images/g_right_50x50.png')

px1 = img1.load()
px2 = img2.load()
v_px1 = []
v_px2 = []
soma = 0
#print(type(px1))
#print(type(v_px1_x), type(v_px1_y))
for x in range(2):#img1.width):
    for y in range(2):#img1.height):
        a, b = px1[x, y]
        v_px1.append(a)
        v_px1.append(b)
        c, d = px2[x, y]                
        v_px2.append(c)
        v_px2.append(d)
        
print('Pixel 1: ',v_px1)
print('Pixel 2: ',v_px2)

teste = distance.euclidean(v_px1, v_px2)
print(teste)
