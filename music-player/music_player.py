#libraries
import wx
import wx.media

class MusicPlayerApp(wx.Frame):
    def __init__(self, parent=None, id=-1):
        # the main
        wx.Frame.__init__(self, parent, id, 'Music Player using Python', size=(600, 300))
        self.panel = wx.Panel(self)

        mySizer = wx.BoxSizer(wx.VERTICAL)

        # Create media control to play audio
        self.mc = wx.media.MediaCtrl(self.panel)
        mySizer.Add(self.mc, 0, wx.ALL | wx.EXPAND, 5)

        # Create the play button and disable it initially
        self.playButton = wx.Button(self.panel, -1, label='Play', size=(80, -1))
        mySizer.Add(self.playButton, 0, wx.ALL | wx.CENTER, 5)
        self.playButton.Disable()  # Disable the play button initially
        self.Bind(wx.EVT_BUTTON, self.onPlay, self.playButton)

        # Create the load button to choose a song
        loadButton = wx.Button(self.panel, -1, label='Load', size=(80, -1))
        mySizer.Add(loadButton, 0, wx.ALL | wx.CENTER, 5)
        self.Bind(wx.EVT_BUTTON, self.onLoadFile, loadButton)

        # Create the pause button to pause the playback
        pauseButton = wx.Button(self.panel, -1, label='Pause', size=(80, -1))
        mySizer.Add(pauseButton, 0, wx.ALL | wx.CENTER, 5)
        self.Bind(wx.EVT_BUTTON, self.onPause, pauseButton)

        # Create the stop button to stop the playback
        stopButton = wx.Button(self.panel, -1, label='Stop', size=(80, -1))
        mySizer.Add(stopButton, 0, wx.ALL | wx.CENTER, 5)
        stopButton.Bind(wx.EVT_BUTTON, self.onStop, stopButton)

        # Create the seeker to show progress and allow seeking
        self.slider = wx.Slider(self.panel, -1, 0, 0, 100, size=(300, -1))  # Set initial range 0 to 100
        self.Bind(wx.EVT_SLIDER, self.onSeek, self.slider)
        mySizer.Add(self.slider, 0, wx.ALL | wx.CENTER, 5)  # Move the seeker below the buttons

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.onTimer, self.timer)

        self.panel.SetSizer(mySizer)

        # Set background colors
        self.panel.SetBackgroundColour('#f0f0f0')
        self.playButton.SetBackgroundColour('#e9e9e9')
        loadButton.SetBackgroundColour('#e9e9e9')
        pauseButton.SetBackgroundColour('#e9e9e9')
        stopButton.SetBackgroundColour('#e9e9e9')

        # Set font and color for the heading
        font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.heading = wx.StaticText(self.panel, label='Music Player using Python', size=(300, 40), style=wx.ALIGN_CENTRE)
        self.heading.SetForegroundColour('#007acc')
        self.heading.SetFont(font)

        # Add the heading and status label to the sizer
        mySizer.Insert(0, self.heading, 0, wx.ALL | wx.EXPAND, 5)
        self.status_label = wx.StaticText(self.panel, label="No song loaded", size=(300, 20), style=wx.ALIGN_CENTRE)
        mySizer.Insert(1, self.status_label, 0, wx.ALL | wx.EXPAND, 5)

        self.Show()

    def onLoadFile(self, event):
        # Open a file dialog to choose a song
        wildcard = "*.mp3;*wav"
        style = wx.FD_OPEN
        fileDialog = wx.FileDialog(self, "Choose a file", wildcard=wildcard, style=style)
        if fileDialog.ShowModal() == wx.ID_OK:
            # Load the chosen song and update the status label
            path = fileDialog.GetPath()
            self.mc.Load(path)
            self.status_label.SetLabel(f"Loaded Song: {fileDialog.GetFilename()}")
            self.playButton.Enable()  # Enable the play button after loading the song

        fileDialog.Destroy()

    def onPlay(self, event):
        # Play the loaded song and start the timer
        self.mc.Play()
        self.timer.Start(100)
        audio_length = self.mc.Length()
        self.slider.SetRange(0, audio_length)

    def onPause(self, event):
        # Pause the playback
        self.mc.Pause()

    def onStop(self, event):
        # Stop the playback and reset the seeker position
        self.mc.Stop()
        self.slider.SetValue(0)

    def onTimer(self, event):
        # Update the seeker position based on the current playback time
        updateslider = self.mc.Tell()
        self.slider.SetValue(updateslider)

    def onSeek(self, event):
        # Seek to the position specified by the seeker/slider
        dragslider = self.slider.GetValue()
        self.mc.Seek(dragslider)

if __name__ == '__main__':
    app = wx.App()
    frame = MusicPlayerApp()
    app.MainLoop()
