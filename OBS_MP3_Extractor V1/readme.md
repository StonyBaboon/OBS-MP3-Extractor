# OBS MP3 Extractor

## Description
This project offers two Python scripts that seamlessly integrate with OBS Studio to automatically extract audio tracks from video recordings as soon as the recording ends, providing enhanced workflow automation and audio management.

### Features
- Automatically extracts all audio tracks from recorded video files.
- Supports multiple video formats (e.g., `.mp4`, `.mkv`, `.avi`, `.mov`).
- Organizes extracted tracks into dedicated folders and saves them as `Track_X.mp3`.

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
   - The script will now run automatically when recording stops.

## How to Use
1. **Recording**: Record normally in OBS. When the recording stops, the `track_extractor.py` script is triggered.
2. **Processing**: The script moves the recorded video into a folder and extracts the audio tracks into `Track_X.mp3` files.
3. **Result**: Each video will have a folder with the extracted audio tracks.

## License
This project is licensed under the MIT License.
