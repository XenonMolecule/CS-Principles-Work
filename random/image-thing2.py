import cv2
img = cv2.imread('cactus.png')

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

string = ""

width = img_rgb.shape[1]
height = img_rgb.shape[0]
for pxy in range(height):
    for pxx in range(width):
        for color in range(3):
            string += '{0:08b}'.format(int(img_rgb[pxy][pxx][color]))

print(string)
