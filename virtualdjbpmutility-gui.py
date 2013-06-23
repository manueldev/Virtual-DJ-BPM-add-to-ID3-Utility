import wx
import wxTest.gui

class Interfaz(wxTest.gui.gui):
	def __init__(self, parent):
		wxTest.gui.gui.__init__(self, parent)

class InterfazHandler():
	def __init__(self):
			app = wx.App(False)
			frame = Interfaz(None)
			frame.Show(True)
			app.MainLoop()

graficos = InterfazHandler()