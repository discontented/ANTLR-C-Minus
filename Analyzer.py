from gen.MyCMinusParser import MyCMinusParser
from gen.MyCMinusListener import MyCMinusListener
from gen.MyCMinusVisitor import MyCMinusVisitor
from Listener import Listener

class Analyzer(MyCMinusListener):
    lv_exit_list = list() # (label, [followingLabel1, fLabel2, ...])
    lv_entry_list = list()

    def __init__(self, numLabels, killSet, genSet):
        self.labels = numLabels
        self.killSet = killSet
        self.genSet = genSet

        self.lv_entry_list = [(i + 1, self.killSet[i], self.genSet[i]) for i in range(self.labels)]
        self.lv_exit_list = [[i, i+1] for i in range(1, self.labels + 1)]
        self.lv_exit_list[-1][-1] = "{empty}"

    def enterConditionalStat(self, ctx:MyCMinusParser.ConditionalStatContext):
        statList = ctx.parentCtx
        # print(statList.statement())
        # print(len(statList.statement()))

        label_index = ctx.__getattribute__("label") - 1

        # print(i)
        if isinstance(ctx.conditionalStatement(), MyCMinusParser.IfStatementContext):
            firstStatementLabel = ctx.children[0].statement()[0].statementList().statement()[0].__getattribute__(
                "label")
            secondStatementLabel = ctx.children[0].statement()[1].statementList().statement()[0].__getattribute__(
                "label")
            # Last statement within if block
            last_if_label = ctx.children[0].statement()[0].statementList().statement()[-1].__getattribute__("label")

            self.lv_exit_list[label_index] = ((ctx.__getattribute__("label"), firstStatementLabel, secondStatementLabel))

            if ([last_if_label, secondStatementLabel] in self.lv_exit_list):
                self.lv_exit_list.pop(self.lv_exit_list.index([last_if_label, secondStatementLabel]))



            # Gets statement following if/else
            follow_stat_label = statList.statement()[statList.statement().index(ctx) + 1].__getattribute__("label")
            self.lv_exit_list.insert(last_if_label - 1, (last_if_label, follow_stat_label))
            # self.lv_exit_list[last_if_label] = (last_if_label, follow_stat_label)

        elif(isinstance(ctx.conditionalStatement(), MyCMinusParser.WhileStatementContext)):
            firstStatementLabel = ctx.children[0].statement().statementList().statement()[0].__getattribute__("label")
            nextIndex = statList.statement().index(ctx) + 1
            if(nextIndex < len(statList.statement())):
                # if a statement exists after the while block
                nextLabel = statList.statement()[nextIndex].__getattribute__("label")
                # self.lv_exit_list.append((ctx.__getattribute__("label"), nextLabel))
                self.lv_exit_list[label_index] = ((ctx.__getattribute__("label"), firstStatementLabel, nextLabel))
                # Get very last statement of while block and changes its control flow to the while loop condition.
                lastStatementLabel = ctx.children[0].statement().statementList().statement()[-1].__getattribute__("label")
                self.lv_exit_list[lastStatementLabel - 1] = (lastStatementLabel, label_index + 1)


    # def enterWhileStatement(self, ctx:MyCMinusParser.WhileStatementContext):
    #     lastStatementLabel = ctx.statement().statementList().statement()[-1].__getattribute__("label")
    #     conditionLabel = ctx.parentCtx.__getattribute__("label")
    #     self.lv_exit_list[lastStatementLabel] = (lastStatementLabel, conditionLabel)


    def isValidType(self, ctx):
        if(isinstance(ctx, MyCMinusParser.VarDeclStatContext)):
            return True
        elif(isinstance(ctx, MyCMinusParser.AssignmentContext)):
            return True
        else:
            return False

    def LVentry(self):
        for i in range(len(self.lv_entry_list)):
            label = self.lv_entry_list[i][0]
            killSetVar = self.lv_entry_list[i][1][1]
            genSetVar = self.lv_entry_list[i][2][1]
            print("LV_entry(%s) = LV_exit(%s) - %s U %s" % (label, label, killSetVar, genSetVar))

    def LVexit(self):
        len_lst = len(self.lv_exit_list)
        for i in range(len_lst):
            # print("LV_exit(%s) = LV_out(%s) U LV_out(%s)" % (self.lv_exit_list[i][0], self.lv_exit_list[i][1], self.lv_exit_list[i][2]))
            if i != len_lst - 1:
                innr_tuple_len = len(self.lv_exit_list[i])

                if innr_tuple_len > 2:
                    print("LV_exit(%s) = " % self.lv_exit_list[i][0], end="")
                    for j in range(1, innr_tuple_len):
                        print("LV_entry(%s) " % self.lv_exit_list[i][j], end="")

                        if j > 0 and j < innr_tuple_len - 1:
                            print("U ", end="")

                        elif j == innr_tuple_len - 1:
                            print()

                else:
                    print("LV_exit(%s) = LV_entry(%s) " % (self.lv_exit_list[i][0], self.lv_exit_list[i][1]))
            else:
                print("LV_exit(%s) = LV_entry(%s) " % (self.lv_exit_list[i][0], "{empty}"))


    def print_cfg(self):
        for node in self.lv_exit_list:
            if isinstance(node, tuple):
                tup_len = len(node)
                for i in range(1, tup_len):
                    print([node[0], node[i]])
            else:
                print(node)

    def return_cfg(self):
        cfg = list()
        for node in self.lv_exit_list:
            if isinstance(node, tuple):
                tup_len = len(node)
                for i in range(1, tup_len):
                    cfg.append([node[0], node[i]])
            else:
                cfg.append(node)
        return cfg







