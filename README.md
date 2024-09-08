
# OBS MP3 Extractor

## Description
This project provides two Python scripts designed to work in tandem with OBS Studio to automatically extract audio tracks from recorded video files whenever a recording stops.

### `track_extractor.py`
- Searches for the OBS `basic.ini` configuration file, extracts the `RecFilePath` value to determine where recordings are saved, and processes video files by moving them to a dedicated folder and extracting the audio tracks as individual MP3 files using `ffmpeg`.

### `obs_auto_track_extractor.py`
- Integrated into OBS Studio, this script listens for when a recording stops and automatically runs the `track_extractor.py` script, which extracts audio tracks from the video recording.

## Features
- Automatically extracts all audio tracks from video recordings as individual MP3 files.
- Supports multiple video formats (e.g., `.mp4`, `.mkv`, `.avi`, `.mov`).
- Automatically organizes video files into folders for better management.
- Seamlessly integrates with OBS Studio, running the audio extraction process upon recording completion.

## How to Use

### Requirements
1. **OBS Studio**: The scripts are designed to work with OBS.
2. **Python 3.x**: Make sure Python is installed and added to your system's PATH.
3. **FFmpeg**: FFmpeg must be installed and accessible in your system's PATH.

### Setup Steps

#### 1. Install FFmpeg:
Make sure FFmpeg is installed and added to your PATH. You can verify this by running:

```bash
ffmpeg -version
```

#### 2. Download the Scripts:
Download or clone the repository containing the following scripts:
- `track_extractor.py`
- `obs_auto_track_extractor.py`

#### 3. Configure `track_extractor.py`:
- `track_extractor.py` will locate your OBS recording directory by searching for the `basic.ini` file in the OBS `AppData` folder.
- It will read the `RecFilePath` and use that location to search for video files, moving them into folders and extracting the audio tracks.

#### 4. Add `obs_auto_track_extractor.py` to OBS:
- In OBS, go to `Tools` > `Scripts`.
- Ensure the Python environment is properly set up in `Python Settings`.
- Click the `+` button and select the `obs_auto_track_extractor.py` file.
- The script is now active and will trigger `track_extractor.py` when recording stops.

## Usage Guide

1. **Recording**: Record normally in OBS. When the recording stops, the `track_extractor.py` script is triggered.
2. **Processing**: The script will move the recorded video into a folder and extract the audio tracks into `Track_X.mp3` files.
3. **Result**: You will have a folder for each video with the extracted audio tracks.

### Example
For a video named `sample_video.mp4` with two audio tracks, after the process:
- `sample_video/Track_1.mp3`
- `sample_video/Track_2.mp3`

## Troubleshooting

- **FFmpeg not found**: Ensure FFmpeg is installed and in the PATH. Verify with `ffmpeg -version`.
- **Python script errors**: Ensure Python 3.x is installed and added to the PATH.

## License
This project is licensed under the MIT License. Feel free to modify and use it in your projects.
