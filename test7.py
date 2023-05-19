import cv2
import numpy as np

def emptyFuc(x): #空き関数
    pass

img = cv2.imread("res/car.jpg")


cv2.namedWindow("Bar") #空きWidnowを作る
cv2.resizeWindow("Bar",640,260)#Windowのサイズを調整
# cv2.createTrackbar("Min","Bar",0,179,emptyFuc) #トラックバーを作る
#createTrackbarの一つ目は名前、二つ目はどのWindowに付くか、三つ目は初期値、四つ目は最大値、五つ目は呼び出す関数(今はここ気にしない)
# cv2.createTrackbar("Max","Bar",179,179,emptyFuc)
# cv2.createTrackbar("SatuMin","Bar",0,255,emptyFuc)
# cv2.createTrackbar("SatuMax","Bar",255,255,emptyFuc)
# cv2.createTrackbar("ValueMin","Bar",0,255,emptyFuc)
# cv2.createTrackbar("ValueMax","Bar",255,255,emptyFuc)

cv2.createTrackbar("Min","Bar",0,179,emptyFuc)#同上
cv2.createTrackbar("Max","Bar",20,179,emptyFuc)
cv2.createTrackbar("SatuMin","Bar",60,255,emptyFuc)
cv2.createTrackbar("SatuMax","Bar",255,255,emptyFuc)
cv2.createTrackbar("ValueMin","Bar",235,255,emptyFuc)
cv2.createTrackbar("ValueMax","Bar",255,255,emptyFuc)

while True: #トラックバーの位置を獲得ため、ここで繰り返しを使用
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #元画像のRGBスペースはHSVに変換

    hueMin = cv2.getTrackbarPos("Min","Bar") #トラックバーの位置をもらう、一つ目はトラックバーの名前、二つ目はWindowの名前
    hueMax = cv2.getTrackbarPos("Max", "Bar") #同上
    satuMin = cv2.getTrackbarPos("SatuMin", "Bar")
    satuMax = cv2.getTrackbarPos("SatuMax", "Bar")
    valueMin = cv2.getTrackbarPos("ValueMin", "Bar")
    valueMax = cv2.getTrackbarPos("ValueMax", "Bar")
    #print(hueMin,hueMax,satuMax,satuMin,valueMax,valueMin) #Debug用、各トラックバーの値を表示

    minv = np.array([hueMin,satuMin,valueMin]) #numpyのarrayを使ってHSVの各部分の最小値を配列にする
    maxv = np.array([hueMax,satuMax,valueMax]) #numpyのarrayを使ってHSVの各部分の最大値を配列にする
    mask = cv2.inRange(imgHsv,minv,maxv)
    #ここでマスクを作る、cv2ライブラリのinRange()関数を作る。中の引数はそれぞれHSVか画像の変数、さっきに作った二つの配列
    #ここで配列を使って値を入るとはHSV三つの値は整体として操作する(と思う)。

    result = cv2.bitwise_and(img,img,mask=mask) #最後はbitwise_and(ビットごとにAND操作する)で色を検出する
    #AND操作は通常「&」の形で出る、その意味は両方の値は同じ場合はOK、それ以外はすべてNGこと

    cv2.imshow("Original",img)#すべての画像を表示
    cv2.imshow("HSV",imgHsv)
    cv2.imshow("Mask",mask)
    cv2.imshow("Masked Result", result)
    cv2.waitKey(1)