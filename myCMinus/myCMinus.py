
from antlr4 import *
from MyCMinusListener import MyCMinusListener

class Labeller(MyCMinusListener):
	def enterMainProg(self, ctx):
		print("Entered main: ")