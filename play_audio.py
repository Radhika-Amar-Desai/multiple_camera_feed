import pygame

def play_audio(file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        # Add a delay to ensure the audio plays before the program exits
        pygame.time.wait(5000)  # Adjust the time as needed

    finally:
        pygame.mixer.quit()
        pygame.quit()

# Replace 'your_audio_file.mp3' with the path to your audio file
audio_file_path = 'output_audio.wav'
play_audio(audio_file_path)

