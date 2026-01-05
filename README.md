# Mp4-Translate-to-Gif

# Video to GIF Converter

A simple and easy-to-use video-to-GIF conversion tool. This is a Python-based graphical user interface (GUI) application designed to quickly turn video clips into GIF animations.

## Features

* Supports converting videos in MP4, AVI, MOV, and other common formats into GIFs
* Customizable GIF parameters:

  * Clip duration (seconds)
  * Frame rate (FPS)
  * Output width (pixels)
* User-friendly graphical interface with intuitive operation
* Real-time conversion status display

## How to Use

1. Click the **“Browse”** button to select the video file you want to convert
2. Choose the location where the GIF file will be saved
3. (Optional) Configure conversion parameters:

   * **Duration**: Set the GIF length (default: 5 seconds)
   * **FPS**: Set the frame rate (default: 15 frames per second)
   * **Width**: Set the output GIF width (default: 720 pixels)
4. Click the **“Convert”** button to start the conversion
5. Wait for the process to finish; the conversion status will be shown in real time

## Requirements

* Python 3.6 or higher
* Required libraries:

  * `tkinter`: GUI framework
  * `moviepy`: Video processing library

## Installation

1. Make sure Python 3.6 or later is installed
2. Install the required dependency:

   ```bash
   pip install moviepy
   ```
3. Run the application:

   ```bash
   python GUI.py
   ```

## Notes

* Supported video formats: MP4, AVI, MOV
* Conversion time depends on video size and selected parameters
* Adjust FPS and width settings as needed to balance GIF quality and file size
