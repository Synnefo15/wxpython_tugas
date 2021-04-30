import wx
from p03 import DashboardFrame


class DashboardFrameController(DashboardFrame):
    def __init__(self, parent):
        DashboardFrame.__init__(self, parent)
        self.combo_day.Clear()
        self.combo_day.AppendItems('senin')
        self.combo_day.AppendItems('selasa')
        self.combo_day.SetSelection(0)
        # self.SetIcon(wx.Icon(""))
        # self.lb_skill.Clear()
        # self.lb_skill.AppendItems(['english', 'indo', 'malay'])

        # * buat tombol di panel agar posisi dapat diatur
        btnx = wx.Button(self.m_panel4, wx.ID_ANY, u"tombol")
        btnx.SetPosition((100, 20))


app = wx.App()
dashboard = DashboardFrameController(parent=None)
dashboard.Show()
app.MainLoop()
