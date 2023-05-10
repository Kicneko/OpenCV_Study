#画像処理基礎関数
#関数の詳しくはドキュメントへ
import cv2
import numpy as np

img = cv2.imread("res/lena.png")
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #元の画像はグレーにする、OpenCVではRGB ChannelではなくBGR Channelです。
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) #GaussianBlurの二つ目のksizeは奇数だけ、三つ目はSigma
imgCanny = cv2.Canny(img, 150, 200) 
imgDialation = cv2.dilate(imgCanny,kernel, iterations=1) #膨張 iterationsは膨張の係数を指定する。
imgEroded = cv2.erode(img,kernel,iterations=1) #劣化 使い方は膨張と同じ。

cv2.imshow("Grayimage", imgGray)
cv2.imshow("Blurimage", imgBlur)
cv2.imshow("Cannyimage", imgCanny)
cv2.imshow("Dialationimage", imgDialation)
cv2.imshow("Erodedimage", imgEroded)
cv2.waitKey(0)