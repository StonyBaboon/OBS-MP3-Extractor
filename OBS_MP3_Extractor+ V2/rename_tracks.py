import os

# Get the absolute path to the current script's directory
current_script_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the track names file
track_names_file = os.path.join(current_script_dir, 'track_names.txt')

# Path to the recording directory (assuming the track_extractor.py script saves this information)
recording_dir_file = os.path.join(current_script_dir, 'recording_directory.txt')

def rename_audio_tracks():
    # Read the recording directory from the text file
    with open(recording_dir_file, 'r') as file:
        recording_dir = file.readline().strip()

    # Read the track names from the track_names.txt file
    with open(track_names_file, 'r') as file:
        track_names = [line.strip() for line in file.readlines()]

    # Walk through all subdirectories in the recording directory
    for root, dirs, files in os.walk(recording_dir):
        # Filter files that start with "Track_" and end with ".mp3"
        track_files = [f for f in files if f.startswith("Track_") and f.endswith(".mp3")]

        # Rename each track file according to the user-defined names
        for track_file in track_files:
            # Extract track number from the filename (e.g., Track_1.mp3 -> 1)
            track_number = int(track_file.split('_')[1].split('.')[0]) - 1  # Subtract 1 to match the index (0-based)

            if track_number < len(track_names) and track_names[track_number]:
                # Construct the new name for the track
                old_track_path = os.path.join(root, track_file)
                new_track_name = os.path.join(root, f"{track_names[track_number]}.mp3")

                # Rename the file
                os.rename(old_track_path, new_track_name)
                print(f"Renamed {old_track_path} to {new_track_name}")

# Run the renaming function
if __name__ == "__main__":
    rename_audio_tracks()
