import wx
import wxControl


class konverter(wxControl.MyFrame2):
    def __init__(self, parent):
        wxControl.MyFrame2.__init__(self, parent)

    def m_choiceOpsi(self, event):
        return self.m_choice1.GetSelection()

    def m_buttonConvert(self, event):
        try:
            opsi = self.m_choiceOpsi(event)
            durasi = int(self.m_textCtrl3.GetValue())
            if opsi == 0:
                tahun = durasi
                hari = 30*12*tahun
                windu = tahun/8
                bulan = tahun*12
            elif opsi == 1:
                hari = durasi
                tahun = hari/(30*12)
                windu = hari/(30*12*8)
                bulan = hari/30
            elif opsi == 2:
                windu = durasi
                hari = windu*30*12*8
                tahun = windu*8
                bulan = windu*8*12
            elif opsi == 3:
                bulan = durasi
                hari = bulan*30
                tahun = bulan/12
                windu = bulan/(12*8)

            self.m_textCtrl4.SetValue(str(tahun))
            self.m_textCtrl5.SetValue(str(hari))
            self.m_textCtrl6.SetValue(str(windu))
            self.m_textCtrl7.SetValue(str(bulan))

        except ValueError:
            wx.MassageBox("mohon masukkan angka",
                          "warning", wx.OK | wx.ICON_ERROR)
            if wx.OK:
                self.m_textCtrl3.SetValue("")


app = wx.App()
frame = konverter(parent=None)
frame.Show()
app.MainLoop()
