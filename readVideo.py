import cv2

capture = cv2.VideoCapture('videos/bus.mp4')

while True:
    success, frame = capture.read()
    if not success:
        print("Error: Video not found or unable to open.")
        break
    cv2.imshow('Bus', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()