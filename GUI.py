import wx
from wx.adv import Animation, AnimationCtrl

class WindowClass:

    def __init__(self, parent, title):
        from Main import Main
        self.recognizer = Main()
        self.speaking = False #flags 
        self.frame = wx.Frame(parent, title = title, size = (800,600), style = wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
        self.frame.Bind(wx.EVT_CLOSE, self.Quit, self.frame)
        self.frame.Center()
        self.panel()
        self.frame.Show()

    def panel(self):
        panel = wx.Panel(self.frame)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        anim = Animation("mic_recording.gif")
        self.gif = AnimationCtrl(panel, wx.ID_ANY, anim)
        
        my_sizer.Add(self.gif, 0, wx.ALL | wx.CENTER, 5)
        my_sizer.Add(0, wx.ALL | wx.EXPAND, 5)
        self.confButton = wx.Button(panel, wx.ID_ANY, 'Speak')
        self.confButton.Bind(wx.EVT_BUTTON, self.Speak, self.confButton)
        my_sizer.Add(self.confButton, 0, wx.BOTTOM | wx.CENTER, 20)
        panel.SetSizer(my_sizer)
        

    def Quit(self, e):
        yesNoBox = wx.MessageBox("Are you sure?", "Question", wx.YES_NO | wx.ICON_QUESTION)
        if yesNoBox == wx.YES:
            self.frame.Destroy()

    def Speak(self, e):
        if self.speaking:
            self.confButton.SetLabel("Speak")
            self.gif.Stop()
        else:
            self.confButton.SetLabel("Listening")
            self.gif.Play()
            self.recognizer.listen()
        self.speaking = not self.speaking
