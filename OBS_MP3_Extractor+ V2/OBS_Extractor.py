import obspython as obs
import subprocess
import os

# Get the absolute path to the current script's directory
current_script_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the obs_track_extractor.py script in the same directory
obs_track_extractor_script = os.path.join(current_script_dir, "track_extractor.py")

# Path to the rename_tracks.py script in the same directory
rename_tracks_script = os.path.join(current_script_dir, "rename_tracks.py")

# Variables to store the track names provided by the user
track_names = [""] * 6  # List to store names for up to 6 tracks

# Callback for when the recording stops
def on_event(event):
    if event == obs.OBS_FRONTEND_EVENT_RECORDING_STOPPED:
        # Run the obs_track_extractor.py script using its absolute path
        subprocess.run(["python", obs_track_extractor_script])

        # Save the track names to a text file
        save_track_names()

        # Run the rename_tracks.py script to rename the audio tracks
        subprocess.run(["python", rename_tracks_script])

# Function to save the track names to a text file
def save_track_names():
    track_names_file = os.path.join(current_script_dir, 'track_names.txt')

    with open(track_names_file, 'w') as file:
        for name in track_names:
            file.write(name + '\n')
    print(f"Track names saved to: {track_names_file}")

# Function to define the script's description in OBS
def script_description():
    return "This script runs obs_track_extractor.py when a recording is stopped and allows renaming of up to 6 audio tracks."

# Function to define script properties in OBS (for user input)
def script_properties():
    props = obs.obs_properties_create()

    # Add text fields to allow the user to input names for the tracks (up to 6)
    obs.obs_properties_add_text(props, "track1_name", "Track 1 Name", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_text(props, "track2_name", "Track 2 Name", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_text(props, "track3_name", "Track 3 Name", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_text(props, "track4_name", "Track 4 Name", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_text(props, "track5_name", "Track 5 Name", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_text(props, "track6_name", "Track 6 Name", obs.OBS_TEXT_DEFAULT)

    return props

# Called when script settings are updated
def script_update(settings):
    global track_names

    # Update the track names based on user input (up to 6 tracks)
    track_names[0] = obs.obs_data_get_string(settings, "track1_name")
    track_names[1] = obs.obs_data_get_string(settings, "track2_name")
    track_names[2] = obs.obs_data_get_string(settings, "track3_name")
    track_names[3] = obs.obs_data_get_string(settings, "track4_name")
    track_names[4] = obs.obs_data_get_string(settings, "track5_name")
    track_names[5] = obs.obs_data_get_string(settings, "track6_name")

# Called when script is loaded
def script_load(settings):
    obs.obs_frontend_add_event_callback(on_event)

# Called when script is unloaded
def script_unload():
    obs.obs_frontend_remove_event_callback(on_event)
