import os
import random
import time
import subprocess

SEQUENTIAL_FOLDER_PATH="./media/sequential"
RANDOM_FOLDER_PATH="./media/random"
START_FILE_PATH="./media/iniciando.mp3"
FINISH_FILE_PATH="./media/finalizando.mp3"
MINUTES_TO_REST=1

def play_video(file_path):
    """
    Plays a single MP4 video file with audio using FFmpeg's ffplay.
    
    :param file_path: Path to the MP4 file.
    """
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    
    command = ["ffplay", "-autoexit", "-fs", file_path]
    subprocess.run(command)

def play_standart_initial_poses():
    mp4_files = [f for f in sorted(os.listdir(SEQUENTIAL_FOLDER_PATH)) if f.endswith(".mp3")]
    
    if not mp4_files:
        print("No MP3 files found in the specified folder.")
        return
    
    for video_file in mp4_files:
        video_path = os.path.join(SEQUENTIAL_FOLDER_PATH, video_file)
        play_video(video_path)

def play_other_poses_randomly():
    mp4_files = [f for f in os.listdir(RANDOM_FOLDER_PATH) if f.endswith(".mp3")]
    
    if not mp4_files:
        print("No MP3 files found in the specified folder.")
        return
    
    random.shuffle(mp4_files)
    
    for video_file in mp4_files:
        video_path = os.path.join(RANDOM_FOLDER_PATH, video_file)
        play_video(video_path)

def main():
    for _ in range(3):
        play_video(START_FILE_PATH)
        play_standart_initial_poses()
        play_other_poses_randomly()
        play_video(FINISH_FILE_PATH)
        time.sleep(MINUTES_TO_REST * 60)

if __name__ == "__main__":
    main()
