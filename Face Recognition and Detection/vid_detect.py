import cv2 as cv

# Function to rescale the frame
def rescaleFrame(frame, scale=0.99):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Load the Haar Cascade classifier
haar_cascade_path = "haar_face.xml"  # Ensure the path is correct
haar_cascade = cv.CascadeClassifier(haar_cascade_path)

# Check if the Haar Cascade classifier is loaded correctly
if haar_cascade.empty():
    print("Error: Could not load Haar Cascade classifier. Check the file path.")
    exit()

# Provide the path to your video file
video_path = "Videos\\1.mp4"  # Replace with your video file path

# Initialize video capture with the video file
cap = cv.VideoCapture(video_path)

# Check if the video capture is opened successfully
if not cap.isOpened():
    print(f"Error: Could not open video file at {video_path}. Check if the file exists and the path is correct.")
    exit()

# Set the desired window size
window_width = 800  # Adjust as needed
window_height = 600  # Adjust as needed

# Create a named window with the specified size
cv.namedWindow("Detected Faces", cv.WINDOW_NORMAL)
cv.resizeWindow("Detected Faces", window_width, window_height)

while True:
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        print("End of video or could not read frame. Exiting...")
        break  # Exit if no frame is read (end of video or error)

    # Rescale the frame
    resized_frame = rescaleFrame(frame, scale=0.5)  # Adjust scale as needed

    # Convert the frame to grayscale
    gray = cv.cvtColor(resized_frame, cv.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces_rect:
        cv.rectangle(resized_frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

    # Display the frame with detected faces
    cv.imshow("Detected Faces", resized_frame)

    # Exit on 'q' key press
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv.destroyAllWindows()
cv.waitKey(0)