import wx
import guiPer2


class panelDashB(guiPer2.panelDashboard):
    def __init__(self, parent):
        guiPer2.panelDashboard.__init__(self, parent)
        self.SetSize(parent.GetSize())


class MyGUI(guiPer2.MyFrame2):
    def __init__(self, parent):
        guiPer2.MyFrame2.__init__(self, parent)

    def btnLoginOnButtonClick(self, event):
        username = self.inputUserName.GetValue()
        password = self.inputPass.GetValue()

        print("username:", username)
        print("password:", password)

        if username == "rafi" and password == "1234":
            wx.MessageBox("login sukses", "info", wx.OK | wx.ICON_INFORMATION)
            print("Login sukses")
            self.m_panel5.Hide()
            # self.panelDashboard = guiPer2.panelDashB(parent=self)
            self.panelDashboard.Show()
        else:
            wx.MessageBox("login gagal", "Error", wx.OK | wx.ICON_ERROR)
            print("Login gagal")

    def MyFrame2OnSize(self, event):
        self.panelDashboard.SetSize(self.GetSize())
        self.panelDashboard.SetSize(self.GetSize())


app = wx.App()
frame = MyGUI(parent=None)
frame.Show()
app.MainLoop()
