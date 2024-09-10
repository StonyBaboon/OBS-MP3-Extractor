import os
import shutil
import subprocess

# Function to search for and read the basic.ini file and extract the RecFilePath value
def find_and_read_basic_ini(root_dir):
    for root, dirs, files in os.walk(root_dir):
        if 'basic.ini' in files:
            basic_ini_path = os.path.join(root, 'basic.ini')
            print(f"Found basic.ini at: {basic_ini_path}")
            
            # Open and read the basic.ini file
            with open(basic_ini_path, 'r') as file:
                for line in file:
                    if line.startswith("RecFilePath="):
                        # Extract the value after 'RecFilePath='
                        rec_file_path_value = line.split('=', 1)[1].strip()
                        print("RecFilePath value:", rec_file_path_value)
                        return rec_file_path_value
    print("basic.ini file not found.")
    return None

# Function to read the recording directory from the recording_directory.txt file
def get_recording_directory():
    script_directory = os.path.dirname(__file__)
    recording_file_path = os.path.join(script_directory, 'recording_directory.txt')

    with open(recording_file_path, 'r') as file:
        recording_dir = file.readline().strip()
    return recording_dir

# Function to extract audio tracks using ffmpeg
def extract_audio_tracks(video_path, output_dir):
    video_name = os.path.splitext(os.path.basename(video_path))[0]

    # Use ffmpeg to get the number of audio tracks
    result = subprocess.run(
        ['ffmpeg', '-i', video_path, '-hide_banner'],
        stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True
    )
    
    # Count how many audio tracks there are (based on "Stream #...: Audio:")
    audio_streams = [line for line in result.stderr.splitlines() if "Stream #" in line and "Audio:" in line]
    num_audio_tracks = len(audio_streams)

    # Extract each audio track individually
    for i in range(num_audio_tracks):
        track_output_path = os.path.join(output_dir, f'Track_{i+1}.mp3')
        subprocess.run(
            ['ffmpeg', '-i', video_path, '-map', f'0:a:{i}', '-q:a', '0', track_output_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        print(f"Audio track {i+1} extracted to: {track_output_path}")

# Main function to process videos
def process_videos(recording_dir):
    # Check if the directory exists
    if not os.path.isdir(recording_dir):
        print(f"The directory {recording_dir} does not exist.")
        return

    # Iterate over the files in the directory
    for file_name in os.listdir(recording_dir):
        # Check if the file is a video (common extensions)
        if file_name.endswith(('.mp4', '.mkv', '.avi', '.mov')):
            video_path = os.path.join(recording_dir, file_name)

            # Create a folder with the video file name (without extension)
            video_name = os.path.splitext(file_name)[0]
            video_folder = os.path.join(recording_dir, video_name)

            if not os.path.exists(video_folder):
                os.makedirs(video_folder)
                print(f"Folder created: {video_folder}")

            # Move the video file to the new folder
            new_video_path = os.path.join(video_folder, file_name)
            shutil.move(video_path, new_video_path)
            print(f"Video moved to: {new_video_path}")

            # Extract the audio tracks and save them as Track_X.mp3
            extract_audio_tracks(new_video_path, video_folder)

    print("Processing complete. No more video files remaining.")

# Run the main script
if __name__ == "__main__":
    # Get the APPDATA directory
    appdata_dir = os.getenv('APPDATA')
    
    # Define the starting path to search for the basic.ini file
    obs_studio_dir = os.path.join(appdata_dir, 'obs-studio', 'basic')

    # Run the function to find and read the basic.ini and extract RecFilePath
    rec_file_path_value = find_and_read_basic_ini(obs_studio_dir)

    # If RecFilePath is found, save it to a text file
    if rec_file_path_value:
        # Get the directory where the script is located
        script_directory = os.path.dirname(__file__)

        # Path where the RecFilePath will be saved
        output_file_path = os.path.join(script_directory, 'recording_directory.txt')

        # Save the RecFilePath to the recording_directory.txt file
        with open(output_file_path, 'w') as output_file:
            output_file.write(rec_file_path_value)
        print(f"RecFilePath saved at: {output_file_path}")
        
        # Now that we have the recording path, process the videos
        process_videos(rec_file_path_value)
    else:
        print("No RecFilePath found to save.")

