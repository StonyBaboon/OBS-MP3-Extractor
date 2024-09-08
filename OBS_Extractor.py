import obspython as obs
import subprocess
import os

# Get the absolute path to the current script's directory
current_script_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the obs_track_extractor.py script in the same directory
obs_track_extractor_script = os.path.join(current_script_dir, "track_extractor.py")

# Callback for when the recording stops
def on_event(event):
    if event == obs.OBS_FRONTEND_EVENT_RECORDING_STOPPED:
        # Run the obs_track_extractor.py script using its absolute path
        subprocess.run(["python", obs_track_extractor_script])

# Called when script is loaded
def script_load(settings):
    obs.obs_frontend_add_event_callback(on_event)

# Called when script is unloaded
def script_unload():
    obs.obs_frontend_remove_event_callback(on_event)

# Function to define the script's description in OBS
def script_description():
    return "This script runs obs_track_extractor.py when a recording is stopped."
