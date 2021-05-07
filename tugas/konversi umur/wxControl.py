# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 612,493 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticTextNamaDpn = wx.StaticText( self, wx.ID_ANY, u"nama depan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextNamaDpn.Wrap( -1 )

		fgSizer4.Add( self.m_staticTextNamaDpn, 0, wx.ALL, 5 )

		self.m_textCtrlNamaDpn = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_textCtrlNamaDpn, 0, wx.ALL, 5 )

		self.m_staticTextNamaBlk = wx.StaticText( self, wx.ID_ANY, u"nama belakang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextNamaBlk.Wrap( -1 )

		fgSizer4.Add( self.m_staticTextNamaBlk, 0, wx.ALL, 5 )

		self.m_textCtrlNamaBlk = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_textCtrlNamaBlk, 0, wx.ALL, 5 )


		bSizer2.Add( fgSizer4, 1, wx.EXPAND, 5 )

		fgSizer6 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticTextUsia = wx.StaticText( self, wx.ID_ANY, u"usia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextUsia.Wrap( -1 )

		fgSizer6.Add( self.m_staticTextUsia, 0, wx.ALL, 5 )

		self.m_textCtrlUsia = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrlUsia, 0, wx.ALL, 5 )

		m_choice2Choices = []
		self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		fgSizer6.Add( self.m_choice2, 0, wx.ALL, 5 )

		self.m_buttonUbah = wx.Button( self, wx.ID_ANY, u"ubah", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_buttonUbah.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_UP, wx.ART_BUTTON ) )
		fgSizer6.Add( self.m_buttonUbah, 0, wx.ALL, 5 )


		bSizer2.Add( fgSizer6, 1, wx.EXPAND, 5 )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticTextHasil = wx.StaticText( self, wx.ID_ANY, u"Hasil konversi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextHasil.Wrap( -1 )

		bSizer5.Add( self.m_staticTextHasil, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		fgSizer5.Add( bSizer5, 1, wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticTextNamaFull = wx.StaticText( self, wx.ID_ANY, u"Nama lengkap", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextNamaFull.Wrap( -1 )

		fgSizer5.Add( self.m_staticTextNamaFull, 0, wx.ALL, 5 )

		self.m_textCtrlNamaFull = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_textCtrlNamaFull, 0, wx.ALL, 5 )

		self.m_staticTextUsiaBln = wx.StaticText( self, wx.ID_ANY, u"usia(bulan)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextUsiaBln.Wrap( -1 )

		fgSizer5.Add( self.m_staticTextUsiaBln, 0, wx.ALL, 5 )

		self.m_textCtrlUsiaBln = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_textCtrlUsiaBln, 0, wx.ALL, 5 )

		self.m_staticTextUsiaHr = wx.StaticText( self, wx.ID_ANY, u"usia(hari)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextUsiaHr.Wrap( -1 )

		fgSizer5.Add( self.m_staticTextUsiaHr, 0, wx.ALL, 5 )

		self.m_textCtrlUsiaHr = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_textCtrlUsiaHr, 0, wx.ALL, 5 )


		bSizer2.Add( fgSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonUbah.Bind( wx.EVT_BUTTON, self.m_buttonUbah )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_buttonUbah( self, event ):
		event.Skip()


