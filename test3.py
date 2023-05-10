#画像にリサイズと切る
import cv2
import numpy as np

img = cv2.imread("res/lunar_cv_test.png")
print(img.shape) #Default Output(700,700,3)、一つ目の700は高さ、二つ目の700は横幅、3はBGRチャンネル数

imgResize = cv2.resize(img,(300,200)) #ここは(横幅,高さ) shape为(高さ,横幅)
print(imgResize.shape)

imgCropped = img[0:200,200:500] #画像のサイズを変わらないうちに切ること。切るはマトリックスを使い、読点前後は高さと横幅の開始と終了位置です



cv2.imshow("lunar_cv_test", img)
cv2.imshow("Resizelunar", imgResize)
cv2.imshow("Croppedlunar", imgCropped)
cv2.waitKey(0)