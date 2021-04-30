# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class grafik_frame
###########################################################################

class grafik_frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Grafik", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_toolBar2 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL ) 
		self.ukuran_font = wx.StaticText( self.m_toolBar2, wx.ID_ANY, u"ukuran font", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ukuran_font.Wrap( -1 )
		self.m_toolBar2.AddControl( self.ukuran_font )
		self.input_font_size = wx.SpinCtrl( self.m_toolBar2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 8, 100, 10 )
		self.m_toolBar2.AddControl( self.input_font_size )
		self.m_toolBar2.Realize() 
		
		bSizer1.Add( self.m_toolBar2, 0, wx.EXPAND, 5 )
		
		self.Tab_controll = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.panel_grafik1 = wx.Panel( self.Tab_controll, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Tab_controll.AddPage( self.panel_grafik1, u"grafik 1", True )
		self.panel_grafik2 = wx.Panel( self.Tab_controll, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Tab_controll.AddPage( self.panel_grafik2, u"grafik 2", False )
		
		bSizer1.Add( self.Tab_controll, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.input_font_size.Bind( wx.EVT_SPINCTRL, self.input_font_sizeOnChange )
		self.panel_grafik1.Bind( wx.EVT_PAINT, self.panel_grafik1OnPaint )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def input_font_sizeOnChange( self, event ):
		event.Skip()
	
	def panel_grafik1OnPaint( self, event ):
		event.Skip()
	

