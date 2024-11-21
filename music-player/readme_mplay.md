# **Music Player Application using wxPython**


The Music Player Application is a simple GUI-based music player built using wxPython, a Python library for creating native graphical user interfaces. This application allows users to load and play audio files in the mp3 or wav format, pause and resume playback, and stop the audio. It also includes a slider that displays the progress of the playback and allows users to seek to a specific position in the audio.

## **Features**

* Load and play audio files in mp3 or wav format.
* Pause and resume audio playback.
* Stop the audio playback and reset the seeker position.
* Slider to display the progress of the audio playback and enable seeking.

## Requirements

`Python 3.x
wxPython library`
Installation
Install Python 3.x if you haven't already. 

You can download Python from the official website: https://www.python.org/downloads/

Install the wxPython library using pip:


`pip install wxpython`

## **How to Use**

* Run the music_demo.py script to launch the Music Player application.
* The application window will open, showing the title "Music Player using Python" and a heading "Music Player."
* To load a song, click on the "Load" button. A file dialog will appear, allowing you to choose an audio file in the mp3 or wav format.
* After selecting a song, the status label will display "Loaded Song: [Song Name]" and the "Play" button will become enabled.
* Click on the "Play" button to start the audio playback. The seeker/slider will display the progress of the playback.
* To pause the playback, click on the "Pause" button. To stop the playback, click on the "Stop" button. The seeker will reset to the beginning when stopping.
* To seek to a specific position in the audio, drag the seeker/slider to the desired location.

## **Notes**

Make sure to have mp3 or wav audio files available to test the application.

The application's GUI elements have been customized with specific colors and font styles for better visual appeal.

The application provides user feedback through the status label and by enabling/disabling the "Play" button based on whether a song is loaded or not.

The application can be extended with additional features, such as volume control, playlist management, and support for other audio formats.

Credits
This application was developed by G.Sudarshan Sastry as a project using wxPython.

For more information and updates, you can visit Your GitHub Repository.

This README provides a basic template; feel free to customize it further as needed.