import cv2
image = cv2.imread('/Users/MichaelRyan/Downloads/Dog.jpg')

b = image.copy()
# set green and red channels to 0
b[:, :, 1] = 0
b[:, :, 2] = 0
width = image.shape[1]
height = image.shape[0]
avg=0
for pxy in range(height):
    for pxx in range(width):
        avg += int(image[pxy][pxx][0])
print("blue " + str(avg/(width*height)/255) + "%")

g = image.copy()
# set blue and red channels to 0
g[:, :, 0] = 0
g[:, :, 2] = 0
avg=0
for pxy in range(height):
    for pxx in range(width):
        avg += int(image[pxy][pxx][1])
print("green " + str(avg/(width*height)/255) + "%")

r = image.copy()
# set blue and green channels to 0
r[:, :, 0] = 0
r[:, :, 1] = 0
avg=0
for pxy in range(height):
    for pxx in range(width):
        avg += int(image[pxy][pxx][2])
print("red " + str(avg/(width*height)/255) + "%")

edges = cv2.Canny(image,100,200)

# RGB - Blue
cv2.imwrite('blue.png', b)

# RGB - Green
cv2.imwrite('green.png', g)

# RGB - Red
cv2.imwrite('red.png', r)

# Canny
cv2.imwrite('canny.png',edges)
