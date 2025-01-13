import cv2

def changeRes(width, height):
    """Sets the desired width and height for the video capture object.

    Args:
        width: The desired width of the video frames.
        height: The desired height of the video frames.
    """
    capture.set(3, width)  # 3 represents the width property
    capture.set(4, height)  # 4 represents the height property

capture = cv2.VideoCapture(0)  # Use 0 for the default camera

# Check if video capture was successful
if not capture.isOpened():
    print("Error: Could not open camera!")
    exit()

# Set desired dimensions (example: 640x480)
desired_width = 640
desired_height = 480
changeRes(desired_width, desired_height)

while True:
    isTrue, frame = capture.read()

    # Check if frame is read successfully
    if frame is not None:
        cv2.imshow('Video', frame)

    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
capture.release()
cv2.destroyAllWindows()