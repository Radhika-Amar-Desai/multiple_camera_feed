import cv2
import sounddevice as sd
import numpy as np
import wave
import threading
import time

# Video parameters
cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Audio parameters
duration = 5  # seconds
sampling_rate = 44100  # Hz
channels = 2

# Create video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_video.avi', fourcc, fps, (frame_width, frame_height))

# Variables for audio recording
audio_data = None

# Function for audio recording and saving
def record_and_save_audio():
    global audio_data
    print("Recording audio...")
    audio_data = sd.rec(int(sampling_rate * duration), samplerate=sampling_rate, channels=channels, dtype=np.int16)
    sd.wait()  # Wait until recording is finished
    print("Audio recording finished.")

    # Save the recorded audio to a WAV file
    audio_file_name = "output_audio.wav"
    wave_file = wave.open(audio_file_name, 'wb')
    wave_file.setnchannels(channels)
    wave_file.setsampwidth(2)  # 2 bytes for 16-bit audio
    wave_file.setframerate(sampling_rate)
    wave_file.writeframes(audio_data.tobytes())
    wave_file.close()
    print(f"Audio saved to {audio_file_name}")

# Function for video recording and saving
def record_and_save_video():
    # Record video and write frames
    while True:
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

# Create threads for audio and video tasks
audio_thread = threading.Thread(target=record_and_save_audio)
video_thread = threading.Thread(target=record_and_save_video)

# Start both threads
audio_thread.start()
video_thread.start()

# Wait for both threads to finish
audio_thread.join()
video_thread.join()

# Release the video capture and writer objects
cap.release()
out.release()

# Destroy all OpenCV windows
cv2.destroyAllWindows()

