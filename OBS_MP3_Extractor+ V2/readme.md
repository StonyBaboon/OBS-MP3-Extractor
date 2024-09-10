# OBS MP3 Extractor +

## Description
This project provides a set of Python scripts designed to integrate with OBS Studio, enabling automatic extraction and renaming of audio tracks from recorded video files whenever a recording stops. Version 2 introduces a user-friendly interface within OBS that allows users to customize the names of extracted audio tracks, offering more control and flexibility over audio management.

### Features
- Automatically extracts and renames all audio tracks from recorded video files.
- Allows users to define custom track names within the OBS interface.
- Supports multiple video formats (e.g., `.mp4`, `.mkv`, `.avi`, `.mov`).
- Organizes extracted tracks into dedicated folders and renames them according to user input.

## Requirements
1. **OBS Studio**: The scripts are designed to work with OBS.
2. **Python 3.x**: Ensure Python is installed and added to your system's PATH.
3. **FFmpeg**: FFmpeg must be installed and accessible in your system's PATH.

## Installation

1. Download or clone the repository.
2. Ensure FFmpeg is installed and accessible in your system's PATH.
3. Add the `obs_auto_track_extractor.py` script to OBS:
   - Go to `Tools` > `Scripts` in OBS.
   - Add the `obs_auto_track_extractor.py` file.
   - Configure custom track names via the OBS interface.
   - The script will now automatically rename tracks and run when recording stops.

## How to Use
1. **Recording**: Record normally in OBS. When the recording stops, the `track_extractor.py` script is triggered, and the `rename_tracks.py` script runs to rename the extracted tracks.
2. **Custom Track Naming**: Use the OBS interface to assign custom names to the audio tracks.
3. **Processing**: The script moves the recorded video into a folder, extracts the audio tracks, and renames them based on user input.
4. **Result**: Each video will have a folder with the extracted and renamed audio tracks.

## License
This project is licensed under the MIT License.
