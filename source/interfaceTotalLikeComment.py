import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size = (600, 500))

        self.panel  = MyPanel(self)

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        self.rb1 = wx.RadioButton(self, label = "Like", pos = (20, 180), style = wx.RB_GROUP)
        self.rb2 = wx.RadioButton(self, label = "Comment", pos = (100, 180))

        self.label = wx.StaticText(self, label = "", pos = (20, 200))

        self.textControl = wx.TextCtrl(self, size = (540,20), style = wx.TE_MULTILINE, pos = (20, 220))

        self.btn = wx.Button(self, label = "Sent", pos = (20, 250))

        self.Bind(wx.EVT_RADIOBUTTON, self.onRadioButton)

        self.btn.Bind(wx.EVT_BUTTON, self.on_press)


    def onRadioButton(self, event):
        rb = event.GetEventObject()
        self.label.SetLabelText("Total " + rb.GetLabel() + " : 200")

    def on_press(self, event):
        value = self.textControl.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="FP ProgJar E03")
        self.frame.Show()
        return True

app = MyApp()
app.MainLoop()