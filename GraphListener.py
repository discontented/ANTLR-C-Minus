import networkx as nx
import matplotlib.pyplot as plt
from gen.MyCMinusParser import MyCMinusParser
from gen.MyCMinusListener import MyCMinusListener
import antlr4


class ControlNode():
    def __init__(self, label, ctx: antlr4.ParserRuleContext):
        self.label = label
        self.ctx = ctx


class GraphListener(MyCMinusListener):

    # label = None
    # G = None

    def __init__(self):
        self.label = 0
        self.G = nx.Graph()

    def enterVarDeclStat(self, ctx: MyCMinusParser.VarDeclStatContext):
        self.label += 1
        newNode = ControlNode(self.label, ctx)
        print(ctx.getText())
        self.G.add_node(ctx.getText())

    def printNodes(self):
        print("nodes: " + str(self.G.number_of_nodes()))
        nx.draw_shell(self.G, with_labels=True)
        plt.show()