import cv2

img = cv2.imread('photos/two.webp')

if img is None:
    print("Error: Image not found or unable to open.")
else:
    cv2.imshow('Two', img)
    cv2.waitKey(0)
  