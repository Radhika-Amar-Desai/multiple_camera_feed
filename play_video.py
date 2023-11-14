import cv2

def play_video(video_file_path):
    cap = cv2.VideoCapture(video_file_path)

    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Video Player", frame)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Replace 'your_video_file.avi' with the path to your AVI video file
video_file_path = 'output_video.avi'
play_video(video_file_path)

