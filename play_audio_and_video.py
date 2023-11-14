import threading

def play_video():
    import play_video

def play_audio():
    import play_audio

# Create threads
thread1 = threading.Thread(target=play_video)
thread2 = threading.Thread(target=play_audio)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()

print("Threads finished.")
