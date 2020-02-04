from PIL import Image, ImageFilter

#i1 = Image.open('images/left_50x50.png').convert('LA') / i1.save('images/g_left_50x50.png')
img = Image.open('teste.png').convert('LA')

im_sharp = img.filter( ImageFilter.FIND_EDGES )
#ImageFilter.BLUR
#ImageFilter.COUNTOUR
#ImageFilter.DETAIL
#ImageFilter.EDGE_ENHANCE
#ImageFilter.EDGE_ENHANCE_MORE
#ImageFilter.EMBOSS
#ImageFilter.FIND_EDGES
#ImageFilter.SMOOTH
#ImageFilter.SMOOTH_MORE
#ImageFilter.SHARPEN

im_sharp.save( 'testeEMBOSS.png' )

im_sharp.show()

