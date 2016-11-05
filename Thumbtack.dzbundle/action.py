# Dropzone Action Info
# Name: Thumbtack
# Description: Add a .webloc to Pinboard using Pushpin. Be sure to use Python 3 via Homebrew. Unfortunately I believe you'll need the heavy heavy PyObjC. Therefore, it's probably only useful for me. Sorry about that!
# Handles: Files, Text
# Creator: Nicholas Lash
# URL: http://soundsmitten.com
# Events: Clicked, Dragged
# KeyModifiers: Command, Option, Control, Shift
# SkipConfig: No
# RunsSandboxed: No
# Version: 1.0
# MinDropzoneVersion: 3.5
# PythonPath: /usr/local/bin/python3

import time
import applescript
import os


getURLFromWebloc = applescript.AppleScript('''
          on run {x}
            tell application "Finder"
            set theFile to x as POSIX file
            return location of file theFile
            end tell
          end run
        ''')
        
thumbtackScript = applescript.AppleScript('''
  on run {x}
    tell application "Thumbtack"
      add url (x as text)
    end tell
  end run
  ''')

def dragged():
    for file in items:
      if os.environ["dragged_type"] == "files":
          file = getURLFromWebloc.run(file)
      thumbtackScript.run(file)

    dz.finish("Task Complete")
    dz.url(False)

def clicked():
    
    # This method gets called when a user clicks on your action
    dz.finish("You clicked me!")
    dz.url(False)
