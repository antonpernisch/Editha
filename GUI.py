import wx
from wx.core import ID_ANY
from wx.adv import Animation, AnimationCtrl

class WindowClass:

    def __init__(self, parent, title):
        self.frame = wx.Frame(parent, title = title, size = (800,600), style = wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)

        self.frame.Bind(wx.EVT_CLOSE, self.Quit, self.frame)

        self.frame.Center()

        self.panel()

        self.frame.Show()
    def panel(self):
        panel = wx.Panel(self.frame)

        my_sizer = wx.BoxSizer(wx.VERTICAL)
        anim = Animation("C:/Users/ernes/Desktop/programming/Edith/mic recording.gif")
        ctrl = AnimationCtrl(panel, wx.ID_ANY, anim, pos=(50,70))
        ctrl.Play()
        
        my_sizer.Add(ctrl, 0, wx.ALL | wx.CENTER, 5)
        my_sizer.Add(0, wx.ALL | wx.EXPAND, 5)
        confButton = wx.Button(panel, wx.ID_ANY, 'Speak')
        my_sizer.Add(confButton, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(my_sizer)

    def Quit(self, e):
        yesNoBox = wx.MessageBox("Are you sure?", "Question", wx.YES_NO | wx.ICON_QUESTION)
        if yesNoBox == wx.YES:
            self.frame.Destroy()

def main():

    app = wx.App()

    WindowClass(None, title='Edith')

    app.MainLoop()
main()
