import cv2
img = cv2.imread("/home/kerwin/python_script/python_code_template/Data_0226 (1)/Data/Trajectories/0208_1634/raw_images/0.png")
Grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(Grayimg, 220, 255,cv2.THRESH_BINARY)
print(thresh)
imgInfo = thresh.shape
heigh = imgInfo[0]
width = imgInfo[1]
for i in range(0,heigh):
    for j in range(0,width):
        grayPixel = thresh[i,j]
        thresh[i,j]=255-grayPixel
cv2.imwrite("./seg.jpg", thresh)