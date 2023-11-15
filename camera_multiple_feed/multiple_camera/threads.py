import threading
import time

def print_numbers():
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

def print_letters():
    import cv2

    # Open an external camera (you may need to change the camera index)
    cap = cv2.VideoCapture(1)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_filename = 'output_video2.avi'
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


# Create two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads have finished.")
