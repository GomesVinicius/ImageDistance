from PIL import Image, ImageSequence#https://ezgif.com/video-to-gif/ezgif-3-28fc08005839.mp4

im1 = Image.open('./gif/320x180/bird.gif')
im2 = Image.open('./gif/320x180/vult.gif')
index = 1
euclidean = 0

resultIm1 = []
resultIm2 = []

for frame in ImageSequence.Iterator(im1):
    img1 = frame.convert('LA')
    img1.save('frames/frame1_%d.png' % index)
    px1 = img1.load()
    
    for x in range(img1.width):
        for y in range(img1.height):
            a, b = px1[x, y]
            a = int(a)
            b = int(b) #Sempre 255
            resultIm1.append(a)

    index += 1

for frame in ImageSequence.Iterator(im2):
    img2 = frame.convert('LA')
    img2.save('frames/frame2_%d.png' % index)
    px2 = img2.load()
    
    for x in range(img2.width):
        for y in range(img2.height):
            a, b = px2[x, y]
            a = int(a)
            b = int(b) #Sempre 255
            resultIm2.append(a)

    index += 1

euclidean = (((sum(resultIm1)) - (sum(resultIm2))) ** 2)
print('Resultado:', euclidean ** 0.5)
