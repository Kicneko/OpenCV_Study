#Calling image, video and camera by using cv2 library.
import cv2

#Webcam
webcap = cv2.VideoCapture(1) #0 is default webcam ID, if have 2 or more then write 1,2...
#webcap.set(3, 1280) #Set Width
#webcap.set(4, 720) #Set Heigth
webcap.set(10, 100) #Set Brightness

while True:
    success, img = webcap.read()
    cv2.imshow("WebcamCap",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Video
# cap = cv2.VideoCapture("res/test_video.mp4")
# while True:
#     success, img = cap.read() #Store the video file frame by frame to img variable.
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'): #If press q then break.
#         break

#Image
# print("Package Imported.")
#
# img = cv2.imread("res/lena.png")
#
# cv2.imshow("Output", img)
# cv2.waitKey(0)