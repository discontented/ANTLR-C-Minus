from gen.MyCMinusParser import MyCMinusParser
from gen.MyCMinusListener import MyCMinusListener
from Listener import Listener

class Analyzer(MyCMinusListener):

    def __init__(self, numLabels):
        self.labels = numLabels

