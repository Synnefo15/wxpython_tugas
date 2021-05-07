import wx
import wxControl


class KonversiUmur(wxControl.MyFrame2):
    def __init__(self, parent):
        wxControl.MyFrame2.__init__(self, parent)

    # def m_buttonUbah(self, event):
    #     nama_lengkap = str(self.m_textCtrl-namaDpn.GetValue() +
    #                        self.m_textCtrl-namaBlk.GetValue())
    #     self.m_textCtrl-namaFull.SetValue(nama_lengkap)


gui = wx.App()
frame = KonversiUmur(parent=None)
frame.Show()
gui.MainLoop()
