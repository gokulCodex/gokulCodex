import cv2
import numpy as np

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Allow the camera to warm up
cv2.waitKey(1000)

# Capture the background frame (assuming the background is static)
ret, background = cap.read()

# Flip the background frame
background = np.flip(background, axis=1)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame
    frame = np.flip(frame, axis=1)

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the color range for detecting the red cloak
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    
    # Create masks to detect the red color
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2

    # Refine the mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

    # Invert the mask to get the non-cloak area
    mask_inv = cv2.bitwise_not(mask)

    # Segment the cloak part out of the frame using the mask
    cloak = cv2.bitwise_and(background, background, mask=mask)

    # Segment the non-cloak part of the frame
    non_cloak = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Combine the cloak and non-cloak parts
    final_output = cv2.addWeighted(cloak, 1, non_cloak, 1, 0)

    # Display the result
    cv2.imshow("Invisibility Cloak", final_output)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
