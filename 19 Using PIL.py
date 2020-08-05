import PIL.Image
image1 = PIL.Image.open("image1.jpg")
print(image1.size)
print(image1.format)

height,width=image1.size
left = width/5
top = height/5
right = 4 * width/5
bottom = 4 * height/5

cropped_image1 = image1.crop((left, top, right, bottom))

#These are temporary and show till the Program Runs.
cropped_image1.show()
image1.show()

new_size = (300, 300) 
resized_image1 = cropped_image1.resize(new_size)
# To save an image in storage
resized_image1.save("resized_image1.jpg")


input("Press Any key to exit... ")