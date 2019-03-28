import cv2
im_gray = cv2.imread('cactus.png', cv2.IMREAD_GRAYSCALE)
thresh = 121
im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite('bw_image.png', im_bw)

string = ""

width = im_bw.shape[1]
height = im_bw.shape[0]
for pxy in range(height):
    for pxx in range(width):
        string += str(int((im_bw[pxy][pxx])/255))

print(string)
