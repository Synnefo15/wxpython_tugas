import wx
from wxControll import MyFrame2


class MainController(MyFrame2):
    def __init__(self, parent):
        MyFrame1.__init__(self, parent)

    def m_button1OnButtonClick(self, evt):
        print('ombol ditekan')


app = wx.App()
dashboard = MyFrame2(parent=None)
dashboard.Show()
app.MainLoop()
