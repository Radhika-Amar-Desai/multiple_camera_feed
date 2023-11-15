import cv2

# Open an external camera (you may need to change the camera index)
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_filename = 'output_video.avi'
fps = 30.0
resolution = (640, 480)
out = cv2.VideoWriter(output_filename, fourcc, fps, resolution)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Write the frame to the output video file
    out.write(frame)

    # Display the resulting frame
    cv2.imshow('Video Recording', frame)

    # Break the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything when the job is done
cap.release()
out.release()
cv2.destroyAllWindows()
