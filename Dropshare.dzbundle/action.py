# Dropzone Action Info
# Name: Dropshare
# Description: Drop files into Dropshare 4
# Handles: Files, Text
# Creator: Nicholas Lash
# URL: http://soundsmitten.com
# Events: Dragged
# KeyModifiers: Command, Option, Control, Shift
# SkipConfig: No
# RunsSandboxed: No
# Version: 1.0
# MinDropzoneVersion: 3.5

import subprocess
import time

def dragged():
  for file in items:    
    command_process = subprocess.call(['open', file, '-a', '/Applications/Dropshare 4.app'])
    dz.finish(file)
    
