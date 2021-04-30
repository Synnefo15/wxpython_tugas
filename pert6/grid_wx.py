# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class frame_grid
###########################################################################

class frame_grid ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"data mahasiswa", pos = wx.DefaultPosition, size = wx.Size( 799,391 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.p_mahasiswa = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.g_nama = wx.grid.Grid( self.p_mahasiswa, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.g_nama.CreateGrid( 5, 5 )
		self.g_nama.EnableEditing( True )
		self.g_nama.EnableGridLines( True )
		self.g_nama.EnableDragGridSize( False )
		self.g_nama.SetMargins( 0, 0 )
		
		# Columns
		self.g_nama.EnableDragColMove( False )
		self.g_nama.EnableDragColSize( True )
		self.g_nama.SetColLabelSize( 30 )
		self.g_nama.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.g_nama.EnableDragRowSize( True )
		self.g_nama.SetRowLabelSize( 80 )
		self.g_nama.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.g_nama.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer1.Add( self.g_nama, 0, wx.ALL, 5 )
		
		self.b_tambah = wx.Button( self.p_mahasiswa, wx.ID_ANY, u"tambah data", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.b_tambah, 0, wx.ALL, 5 )
		
		
		self.p_mahasiswa.SetSizer( fgSizer1 )
		self.p_mahasiswa.Layout()
		fgSizer1.Fit( self.p_mahasiswa )
		self.m_notebook1.AddPage( self.p_mahasiswa, u"mahasiswa", False )
		self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook1.AddPage( self.m_panel2, u"a page", False )
		
		bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.g_nama.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.g_namaOnGridCmdSelectCell )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def g_namaOnGridCmdSelectCell( self, event ):
		event.Skip()
	

