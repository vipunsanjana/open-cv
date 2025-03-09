import cv2


def resize_image(image_path, scale=0.75):

    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return
    
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dimensions = (width, height)
    
    resized_img = cv2.resize(img, dimensions, interpolation=cv2.INTER_AREA)
    
    cv2.imshow('Original Image', img)
    cv2.imshow('Resized Image', resized_img)
    cv2.waitKey(0)
    

def main():
    
    image_path = 'photos/two.webp'
    resize_image(image_path)

if __name__ == "__main__":
    main()    

