
import cv2

# Load the image
imgFile = cv2.imread('/Users/abimbolaopakunle/Downloads/unsplashkids.jpg')



# Check if the image loaded correctly
if imgFile is None:
    print("Error: Image could not be loaded. Check the file path.")
else:
    # Display the image in a loop
    while True:
        cv2.imshow('kidsPhoto', imgFile)

        # Wait for 1 ms and check if "Esc" key is pressed
        if cv2.waitKey(1) & 0xFF == 27:  # 27 is the ASCII code for Esc key
            break

    # Close all OpenCV windows
    cv2.destroyAllWindows()