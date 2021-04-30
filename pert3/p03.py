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
## Class DashboardFrame
###########################################################################

class DashboardFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Dashboard", pos = wx.DefaultPosition, size = wx.Size( 803,732 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer2.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Hari", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		combo_dayChoices = [ u"senin", u"selasa", u"rabi" ]
		self.combo_day = wx.ComboBox( self.m_panel2, wx.ID_ANY, u"Pilih hari", wx.DefaultPosition, wx.Size( 250,-1 ), combo_dayChoices, 0 )
		self.combo_day.SetSelection( 0 )
		fgSizer2.Add( self.combo_day, 0, wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		lb_skillChoices = [ u"html", u"css", u"js" ]
		self.lb_skill = wx.ListBox( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,100 ), lb_skillChoices, 0 )
		fgSizer2.Add( self.lb_skill, 0, wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Deskripsi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer2.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"kdalda\n\ndfss", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		fgSizer2.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
		
		self.m_button1 = wx.Button( self.m_panel2, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		fgSizer2.Add( self.m_button1, 0, wx.ALL, 5 )
		
		self.m_panel3 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		fgSizer2.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel2.SetSizer( fgSizer2 )
		self.m_panel2.Layout()
		bSizer1.Add( self.m_panel2, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		bSizer1.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel6 = wx.Panel( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel5.SetSizer( bSizer3 )
		self.m_panel5.Layout()
		bSizer3.Fit( self.m_panel5 )
		bSizer1.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

