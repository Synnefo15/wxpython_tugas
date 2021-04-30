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
## Class panelDashboard
###########################################################################

class panelDashboard ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.panelDashboard = wx.StaticText( self, wx.ID_ANY, u"Dashboard", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.panelDashboard.Wrap( -1 )
		bSizer3.Add( self.panelDashboard, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_loginPage = wx.StaticText( self.m_panel5, wx.ID_ANY, u"login page", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_loginPage.Wrap( -1 )
		bSizer4.Add( self.m_loginPage, 0, wx.ALL, 5 )
		
		self.m_panel6 = wx.Panel( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticUserName = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticUserName.Wrap( -1 )
		fgSizer4.Add( self.m_staticUserName, 0, wx.ALL, 5 )
		
		self.inputUserName = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.inputUserName, 0, wx.ALL, 5 )
		
		self.m_staticPass = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticPass.Wrap( -1 )
		fgSizer4.Add( self.m_staticPass, 0, wx.ALL, 5 )
		
		self.inputPass = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer4.Add( self.inputPass, 0, wx.ALL, 5 )
		
		self.btnLogin = wx.Button( self.m_panel6, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.btnLogin, 0, wx.ALL, 5 )
		
		
		self.m_panel6.SetSizer( fgSizer4 )
		self.m_panel6.Layout()
		fgSizer4.Fit( self.m_panel6 )
		bSizer4.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel5.SetSizer( bSizer4 )
		self.m_panel5.Layout()
		bSizer4.Fit( self.m_panel5 )
		bSizer3.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_SIZE, self.MyFrame2OnSize )
		self.btnLogin.Bind( wx.EVT_BUTTON, self.btnLoginOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def MyFrame2OnSize( self, event ):
		event.Skip()
	
	def btnLoginOnButtonClick( self, event ):
		event.Skip()
	

