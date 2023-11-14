import cv2

# Open a connection to the camera (0 by default, which is the default camera)
cap = cv2.VideoCapture(0)

# Get the default frames per second (fps) of the camera
fps = cap.get(cv2.CAP_PROP_FPS)

# Get the default width and height of the frames
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # You can use other codecs like MJPG, XVID, etc.
out = cv2.VideoWriter('output.avi', fourcc, fps, (frame_width, frame_height))

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Write the frame to the output video file
    out.write(frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and writer objects
cap.release()
out.release()

# Destroy all OpenCV windows
cv2.destroyAllWindows()

