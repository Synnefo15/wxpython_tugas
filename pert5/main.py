
import grafik_Wx
import wx

# * metode 1
# import cara pertama dengan langsung pake "from ... import"
# from grafik_Wx import grafik_frame


# class MyGui(grafik_frame):
#     def __init__(self, parent):
#         grafik_frame.__init__(self, parent)


# * Metode 2
# import cara ke2 dengan hanya pake "import"


class MyGui(grafik_Wx.grafik_frame):
    def __init__(self, parent):
        grafik_Wx.grafik_frame.__init__(self, parent)
        self.ukuranfont = 10

    def panel_grafik1OnPaint(self, event):
        event.Skip()
        dc = wx.PaintDC(self.panel_grafik1)
        # setPen harus ditaruh sebelum DrawLine
        dc.SetPen(wx.Pen(wx.Colour(255, 0, 0),
                  width=4, style=wx.PENSTYLE_SOLID))
        dc.DrawLine(0, 0, 300, 300)
        # set kotak
        dc.SetPen(wx.Pen(wx.Colour(0, 255, 0),
                  width=4, style=wx.PENSTYLE_SOLID))
        dc.SetBrush(wx.Brush(wx.Colour(0, 0, 255),
                    style=wx.BRUSHSTYLE_CROSS_HATCH))
        dc.DrawRectangle(250, 25, 200, 100)
        # set lingkaran
        dc.SetPen(wx.Pen(wx.Colour(12, 134, 10), width=10,
                  style=wx.PENSTYLE_SOLID))
        dc. SetBrush(wx.Brush(wx.Colour(10, 40, 39,),
                     style=wx.BRUSHSTYLE_SOLID))
        dc.DrawCircle(40, 100, 50)

        # buat text
        font = wx.Font(self.ukuranfont, wx.ROMAN, wx.ITALIC, wx.NORMAL)
        dc.SetFont(font)
        dc.DrawText('hallo rfai', wx.Point(350, 300))

        def input_font_sizeOnChange(self, event):
            self.ukuranfont = self.input_font_size.GetValue()
            self.Refresh()


app = wx.App()
frame = MyGui(parent=None)
frame.Show()
app.MainLoop()
