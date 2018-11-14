
from antlr4 import *
from myCMinus.MyCMinusListener import MyCMinusListener

class Labeller(MyCMinusListener):
	def enterMainProg(self, ctx):
		print("Entered main: ")