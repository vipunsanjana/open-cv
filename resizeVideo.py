import cv2 


def resize_video(video_path, scale=0.75):
  
    capture = cv2.VideoCapture(video_path)
    
    if not capture.isOpened():
        print("Error: Video file not found!")
        return
    
    while True:
        isTrue, frame = capture.read()
        if not isTrue:
            break
        
        width = int(frame.shape[1] * scale)
        height = int(frame.shape[0] * scale)
        dimensions = (width, height)
        frame_resized = cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)
        
        cv2.imshow('Original Video', frame)
        cv2.imshow('Resized Video', frame_resized)
        
        if cv2.waitKey(20) & 0xFF == ord('d'):
            break
    
    capture.release()
    cv2.destroyAllWindows()


def main():
    
    video_path = 'videos/bus.mp4'
    resize_video(video_path)

if __name__ == "__main__":
    main()    

