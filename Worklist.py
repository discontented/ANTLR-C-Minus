class Worklist:

    def __init__(self, cfg, entry_list):
        self.worklist = {}
        self.cfg = cfg
        self.analysis = [set() for i in range(len(entry_list))]
        self.entry_list = entry_list # (label, kill, gen)

        self.start_worklist()
        self.start_analysis()


        # self.transfer_func(set(), self.entry_list[0][1], self.entry_list[0][2])

    def reverse_flow(self):
        let = 'A'
        i = 0
        for tup in reversed(self.cfg[:-1]):
            tup = tuple(reversed(tup))
            self.worklist[chr(ord(let) + i)] = tup
            i += 1

    def transfer_func(self, label):
        # f_1(Analysis[1]) - {} U {}

        kill_set = self.entry_list[label - 1][1]
        gen_set = self.entry_list[label - 1][2]
        analysis_set = self.analysis[label - 1]

        # self.print_transfer(label, analysis_set, kill_set[1], gen_set[1])

        if '{empty}' in gen_set[1]:
            gen_set = (gen_set[0], set())

        if '{empty}' in kill_set[1]:
            kill_set = (kill_set[0], set())


        result = (analysis_set - kill_set[1]).union(gen_set[1])
        self.print_transfer(label, analysis_set, kill_set[1], gen_set[1], result)
        # print(result)
        return result

    def inner_transfer(self, analysis_set, label):
        return self.transfer_func(label, analysis_set, self.entry_list[label - 1][1], self.entry_list[label - 1][2])

    def print_transfer(self, label, analysis_set, kill_set, gen_set, result):
        print("f_%d(Analysis[%d]) = %s - %s U %s = %s\n" % (label, label, analysis_set, kill_set, gen_set, result))

    def start_worklist(self):
        # self.print_set("W", self.worklist)

        print("--- Beginning Worklist Algorithm ---")
        print("Generate worklist algorithm for Live Variable Analysis")
        print("NOTE: The output 'set()' represents an empty set")
        print()
        print("W = {}")
        self.reverse_flow()
        print()
        print("---Populate Worklist---")
        print()
        print("W = ",  end="")
        self.print_set(self.worklist)
        print("\n")

    def start_analysis(self):
        print("---Populate Analysis Set---")
        print(self.analysis)
        print("---End Analysis Population---")
        print()

    def print_set(self, dict_set):
        for key, value in dict_set.items():
            print("%s:%s" % (key, value), end="")

    def print_iteration(self, count, label, follow_label, worklist):
        print("-----Iteration %d------" % count)
        print("L = %d, L' = %d W = " % (label, follow_label), end="")
        self.print_set(self.worklist)
        print()

    def iterate(self):
        count = 1
        while(self.worklist):
            # Pops head element of dictionary
            l, lp = self.worklist.pop(list(self.worklist.keys())[0])
            self.print_iteration(count, l, lp, self.worklist)

            result = self.transfer_func(l)

            if not result.issubset(self.analysis[lp - 1]):
                print("Analysis[%d]: %s" % (lp, self.analysis[lp - 1]))
                print("%s is NOT a subset of %s" % (result, self.analysis[lp - 1]))
                self.analysis[lp - 1] = result
            else:
                print("Analysis[%d]: %s" % (lp, self.analysis[lp - 1]))
                print("%s is a subset of %s " % (result, self.analysis[lp - 1]))

            print()
            count = count + 1


