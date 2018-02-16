from PIL import Image
try:
	img = Image.open("/home/jayjeet/Desktop/image.png")
	img2 = Image.open("/home/jayjeet/Desktop/cropped.png")
	
except IOError:
	pass

# print(img.size) #retrieve the size of the image

# img.save("/home/jayjeet/Desktop/image.png") #to save the image


# img = img.rotate(180) #rotates the image by 180 degrees
# w,h = img.size
# area = (0,0,w/2,h/2) #left and upper coordinates from where to crop and the size of the cropped image is needed
# img = img.crop(area) #cropping an image

# w,h = img.size
# img = img.resize((w//2,h//2)) #for resizing an image
# img.paste(img2, (50, 50)) #pasting one image over one other

# img = img.transpose(Image.FLIP_LEFT_RIGHT)
# print(img.histogram()) #prints the histogram of the image
# print(img.split()) #splits the image into individual bands
# print(img2.mode) #returns the mode in which the image is opened
# print(img.tobitmap()) #converts an image to X11 bitmap 
# img.thumbnail((200,200)) #make a thumbnail out of this image

img.save("/home/jayjeet/Desktop/resizedimage.png")
