from PIL import Image
from PIL import ImageFilter
#from PIL import ImageFont
#from PIL import ImageDraw
filename = "IMAGE3.jpg"
with Image.open(filename) as img:
    img.load()
blur_image=img.filter(ImageFilter.BLUR)
blur_image.show()
""""
bw_image=img.convert('L')
bw_image.show()
size=(400,500)
imgwatermark=img.copy()
imgwatermark.thumbnail(size=(100,100))
imgwatermarkfinal=img.copy()
imgwatermarkfinal.paste(imgwatermark, (0,0))
imgwatermarkfinal.show()
watermarked_image=img.copy()
draw = ImageDraw.Draw(watermarked_image)
font = ImageFont.truetype("arial.ttf",100)
draw.text((0,0),"lokesh",(0,0,0),font=font)
watermarked_image.show()
cropped_img = img.crop((100,100,1200,2000))

print(cropped_img.size)
#print(img.size)
print(type(img))
print(isinstance(img,Image.Image))
#img.show()
#cropped_img.show()
low_res_img=img.resize(
    (img.width//3, img.height //3))
print(low_res_img.size)
#low_res_img.show()
#img.show()
#converted_img = img.transpose(Image.TRANSPOSE)
converted_img.show()
converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
rotated_img=img.rotate(-45)
rotated_img.show()
rotated_img_expand=img.rotate(45, expand=True)
rotated_img_expand.show()"""