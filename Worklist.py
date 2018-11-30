class Worklist:

    def __init__(self, cfg, entry_list):
        self.worklist = {}
        self.cfg = cfg
        print(cfg)
        self.analysis = {}
        self.entry_list = entry_list # (label, kill, gen)

        self.start_worklist()


        # self.transfer_func(set(), self.entry_list[0][1], self.entry_list[0][2])

    def reverse_flow(self):
        let = 'A'
        i = 0
        for tup in reversed(self.cfg[:-1]):
            tup = tuple(reversed(tup))
            self.worklist[chr(ord(let) + i)] = tup
            i += 1

    def transfer_func(self, label, analysis_set, kill_set, gen_set):
        # f_1(Analysis[1]) - {} U {}
        self.print_transfer(label, analysis_set, kill_set[1], gen_set[1])

        if '{empty}' in gen_set[1]:
            gen_set = (gen_set[0], set())

        if '{empty}' in kill_set[1]:
            kill_set = (kill_set[0], set())

        result = (analysis_set - kill_set[1]).union(gen_set[1])
        print(result)
        return result

    def inner_transfer(self, analysis_set, label):
        return self.transfer_func(label, analysis_set, self.entry_list[label - 1][1], self.entry_list[label - 1][2])

    def print_transfer(self, label, analysis_set, kill_set, gen_set):
        print("f_%d(Analysis[%d])=%s-%s U %s" % (label, label, analysis_set, kill_set, gen_set))

    def start_worklist(self):
        # self.print_set("W", self.worklist)
        self.reverse_flow()
        self.print_set(self.worklist)

    def print_set(self, dict_set):

        for key, value in dict_set.items():
            print("%s:%s" % (key, value))

