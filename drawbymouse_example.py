import cv2
import numpy as np

# Variable
# True while mouse button down, False while mouse button up
drawing = False

# Using tuples
ix, iy = -1, -1

# Function to draw rectangle
def draw_rectangle(event, x, y, flags, params):
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img[:] = np.zeros((512, 512, 3), np.uint8)  # Clear the previous rectangle on mouse move
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing', draw_rectangle)

while True:
    cv2.imshow('my_drawing', img)
    
    # Break the loop when 'Esc' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:  # 27 is the ASCII code for Esc key
        break

# Close all OpenCV windows
cv2.destroyAllWindows()