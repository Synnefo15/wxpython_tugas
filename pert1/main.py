import wx
import helloWXGui


class subClass(helloWXGui.MyFrame1):
    def __init__(self, parent):
        helloWXGui.MyFrame1.__init__(self, parent)

    # def m_button1OnButtonClick(self, event):
        print("123")

    def m_buttonSimpanOnButtonClick(self, event):
        nama = self.m_textNama.GetValue()
        alamat = self.m_textAlamat.GetValue()
        email = self.m_textEmail.GetValue()

        print("nama:", nama)
        print("alamat:", alamat)
        print("email:", email)


# harus ada
app = wx.App()
frame = subClass(parent=None)
frame.Show()
# menahan tampilan
app.MainLoop()
