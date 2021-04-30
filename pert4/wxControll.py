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
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.RESIZE_BORDER|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 898,482 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_splitter1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter1.Bind( wx.EVT_IDLE, self.m_splitter1OnIdle )
		
		self.m_panel3 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 10,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel3.SetBackgroundColour( wx.Colour( 255, 128, 64 ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button1 = wx.Button( self.m_panel3, wx.ID_ANY, u"tombol", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button1, 0, wx.ALL, 5 )
		
		
		self.m_panel3.SetSizer( bSizer2 )
		self.m_panel3.Layout()
		self.m_panel4 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel4.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )
		
		self.m_splitter1.SplitVertically( self.m_panel3, self.m_panel4, 87 )
		bSizer1.Add( self.m_splitter1, 1, wx.EXPAND, 5 )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.m_button1OnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_button1OnButtonClick( self, event ):
		event.Skip()
	
	def m_splitter1OnIdle( self, event ):
		self.m_splitter1.SetSashPosition( 87 )
		self.m_splitter1.Unbind( wx.EVT_IDLE )
	

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
	
	def __del__( self ):
		pass
	

