# Dropzone Action Info
# Name: Blog Processor
# Description: Finally, the baseblog processor comes to Swift 3. Usage: change postPath to your blog path in content folder in dropbox. Drag the textbundle you make (in Ulysses or Bear) onto the action.
# Handles: Files
# Creator: Nicholash Lash
# URL: soundsmitten.com
# Events: Dragged
# KeyModifiers: Command, Option, Control, Shift
# SkipConfig: No
# RunsSandboxed: No
# Version: 1.0
# MinDropzoneVersion: 3.5

import time
import subprocess

def dragged():
    tbundle = items[0]
    postPath = '/Users/njlash/Dropbox/content-soundsmitten/01-blog'
    testPath = '/Users/njlash/Desktop'
    command_process = subprocess.call(['./ssblogproc', tbundle, postPath])
    dz.finish("Processed blog post")

