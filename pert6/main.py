import wx
import grid_wx
import renderer


class MyGui(grid_wx.frame_grid):
    def __init__(self, parent):
        grid_wx.frame_grid.__init__(self, parent)
        self.g_nama.SetCellValue(0, 0, 'test')
        self.g_nama.SetCellValue(0, 2, 'test')
        self.g_nama.SetCellTextColour(0, 2, wx.BLUE)
        self.g_nama.SetCellBackgroundColour(0, 0, wx.YELLOW)
        self.AddButtonEditDelete()

    def g_namaOnGridCmdSelectCell(self, event):
        col = event.GetCol()
        row = event.GetRow()
        print('---'*5)
        print(' row:', row, '\n col:', col)

    def AddButtonEditDelete(self):
        imgEdit = wx.Bitmap("edit.PNG", wx.BITMAP_TYPE_PNG)
        imgDelete = wx.Bitmap("delete.PNG", wx.BITMAP_TYPE_PNG)
        colEdit = 3
        colDelete = 4
        self.rdEdit = renderer.MyImageRenderer(imgEdit)
        self.rdDelete = renderer.MyImageRenderer(imgDelete)
        for row in range(self.g_nama.GetNumberRows()):
            self.g_nama.SetCellRenderer(row, colEdit, self.rdEdit)
            self.g_nama.SetRowSize(row, imgEdit.GetHeight() + 4)
            self.g_nama.SetColSize(colEdit, imgEdit.GetWidth() + 4)
            self.g_nama.SetCellRenderer(row, colDelete, self.rdDelete)
            self.g_nama.SetRowSize(row, imgDelete.GetHeight() + 4)
            self.g_nama.SetColSize(colDelete, imgDelete.GetWidth() + 4)


# * buat buka apps
app = wx.App()
frame = MyGui(parent=None)
frame.Show()
app.MainLoop()
