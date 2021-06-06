import wx
import speech_recognition as sr
from GUI import WindowClass
class Main:
    def __init__(self):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()
    
    def listen(self):
        with self.mic as source:
            print("Speak something")
            audio = self.r.listen(source)
            try:
                text = self.r.recognize_google(audio)
                print("You said : {}".format(text))
            except:
                print("Your audio input was not detected")
def main():
    app = wx.App()
    WindowClass(None, title='Edith')
    app.MainLoop()
main()
