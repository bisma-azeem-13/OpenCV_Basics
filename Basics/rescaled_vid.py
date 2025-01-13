import cv2

def rescaleFrame(frame, scale=0.75):
  """Rescales a frame to a specified scale.

  Args:
      frame: The frame to be rescaled.
      scale: The scaling factor (default: 0.75).

  Returns:
      The rescaled frame, or None if the original frame is None.
  """
  if frame is not None:
      width = int(frame.shape[1] * scale)
      height = int(frame.shape[0] * scale)
      dimensions = (width, height)
      return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)
  else:
      print("Error: Could not read video frame!")
      return None  # Indicate error by returning None

capture = cv2.VideoCapture("Videos\\3.mp4")

while True:
  isTrue, frame = capture.read()

  # Check if frame is read successfully before resizing
  if frame is not None:
      frame_resized = rescaleFrame(frame, scale=0.5)
      cv2.imshow('Video', frame)
      cv2.imshow("Resized Frame: ", frame_resized)
  else:
      # Handle the case where no frame is available (e.g., break loop)
      break

  if cv2.waitKey(20) & 0xFF == ord('d'):
      break

capture.release()
cv2.destroyAllWindows()