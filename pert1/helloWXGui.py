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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Belajar WXpython", pos = wx.DefaultPosition, size = wx.Size( 500,573 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel4, wx.ID_ANY, u"Form registrasi" ), wx.VERTICAL )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticNama = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticNama.Wrap( -1 )
		fgSizer3.Add( self.m_staticNama, 0, wx.ALL, 5 )
		
		self.m_textNama = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_textNama, 0, wx.ALL, 5 )
		
		self.m_staticAlamat = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticAlamat.Wrap( -1 )
		fgSizer3.Add( self.m_staticAlamat, 0, wx.ALL, 5 )
		
		self.m_textAlamat = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_textAlamat, 0, wx.ALL, 5 )
		
		self.m_staticEmail = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticEmail.Wrap( -1 )
		fgSizer3.Add( self.m_staticEmail, 0, wx.ALL, 5 )
		
		self.m_textEmail = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_textEmail, 0, wx.ALL, 5 )
		
		self.m_buttonSimpan = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_buttonSimpan, 0, wx.ALL, 5 )
		
		
		sbSizer2.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		
		self.m_panel4.SetSizer( sbSizer2 )
		self.m_panel4.Layout()
		sbSizer2.Fit( self.m_panel4 )
		bSizer1.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_buttonSimpan.Bind( wx.EVT_BUTTON, self.m_buttonSimpanOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_buttonSimpanOnButtonClick( self, event ):
		event.Skip()
	

