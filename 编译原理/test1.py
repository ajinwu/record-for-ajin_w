from pprint import pprint
from copy import deepcopy

class SLRAnalyzer:
    def __init__(self, start, productions, new_start='S', point='.', log_level=0):
        self.start = start
        self.new_start = new_start
        self.productions = productions
        self.nonterminals = productions.keys()
        self.log_level = log_level

        self.overs = set()
        self.get_overs()

        self.jinghao = '#'
        self.first = {nontermainal: {} for nontermainal in self.nonterminals}
        self.follow = {nontermainal: set() for nontermainal in self.nonterminals}
        self.get_first_follow()

        self.items = {key: list() for key in self.nonterminals}
        self.point = point
        self.get_items()

        self.status_list = [self.closure({(self.new_start, self.point + self.start)}), ]
        self.analyse_table = dict()
        self.last_index = 0
        self.index = 0
        self.acc = 'acc'
        self.get_analyse_table()

        self.language_type = self.is_lr0()
        if self.language_type not in [0, 1]:
            exit('unsupported language!')
        if self.language_type == 1:
            print('lr0')
        else:
            print('slr1')

    # 求first的函数
    def get_first(self, nontermainal):
        ret_dict = {}
        for right in self.productions[nontermainal]:
            if (nontermainal, right) in self.first_first:
                ret_dict = self.first[nontermainal]
                continue
            if right != '':
                if right[0] in self.overs:
                    ret_dict.update({right[0]: right})
                else:
                    for sign in right:
                        if sign in self.nonterminals:
                            first_ = self.first[sign]
                            ret_dict.update({key: right for key in first_.keys()})
                            if '' not in first_.keys():
                                break
            else:
                ret_dict.update({'': ''})
        return ret_dict

    # 求first集和follow集
    def get_first_follow(self):
        # 求first第一轮，产生式右部首字符为终结符号
        self.first_first = set()
        for nontermainal in self.nonterminals:
            for right in self.productions[nontermainal]:
                if right != '' and right[0] in self.overs:
                    self.first[nontermainal][right[0]] = right
                    self.first_first.add((nontermainal, right))
        # 求first第二轮
        while True:
            old_first = deepcopy(self.first)
            for nontermainal in self.nonterminals:
                self.first[nontermainal].update(self.get_first(nontermainal))
            if old_first == self.first:
                break
        # 起始符号follow集
        self.follow[self.start].add(self.jinghao)
        # 循环直到follow集不再变化
        while True:
            old_follow = deepcopy(self.follow)
            for nontermainal in self.nonterminals:
                for right in self.productions[nontermainal]:
                    for i, sign in enumerate(right):
                        if sign in self.overs:
                            continue
                        if i == len(right) - 1:
                            self.follow[sign] |= self.follow[nontermainal]
                        elif right[i + 1] in self.overs:
                            self.follow[sign].add(right[i + 1])
                        else:
                            next_set = {key for key in self.first[right[i + 1]].keys()}
                            next_set_without_null = {key for key in self.first[right[i + 1]].keys() if key != ''}
                            self.follow[sign] |= next_set_without_null
                            if '' in next_set:
                                self.follow[sign] |= self.follow[nontermainal]
            if old_follow == self.follow:
                break
        if self.log_level >= 2:
            print('follow set:')
            pprint(self.follow)

    def get_overs(self):
        for nonterminal in self.nonterminals:
            for right in self.productions[nonterminal]:
                for sign in right:
                    if sign not in self.nonterminals:
                        self.overs.add(sign)
        if self.log_level >= 2:
            print('over sign set:')
            pprint(self.overs)

    def get_items(self):
        self.items[self.new_start] = [self.point + self.start, self.start + self.point]
        for nonterminal in self.nonterminals:
            for right in self.productions[nonterminal]:
                for i in range(len(right)):
                    self.items[nonterminal].append(right[:i] + self.point + right[i:])
                self.items[nonterminal].append(right + self.point)
        if self.log_level >= 2:
            print('items:')
            pprint(self.items)

    def closure(self, production_set):
        ret = production_set.copy()
        for production in production_set:
            right = production[1]
            i = 0
            while i < len(right) and right[i] != self.point:
                i += 1
            if i + 1 < len(right) and right[i + 1] in self.nonterminals:
                for item in self.items[right[i + 1]]:
                    if self.point == item[0]:
                        ret.add((right[i + 1], item))
        if ret == production_set:
            return ret
        else:
            return self.closure(ret)

    def go(self, production_set, sign):
        new_production_set = set()
        for production in production_set:
            right = production[1]
            i = 0
            while i < len(right) and right[i] != self.point:
                i += 1
            if i + 1 < len(right) and right[i + 1] == sign:
                new_right = list(right)
                temp = new_right[i]
                new_right[i] = new_right[i + 1]
                new_right[i + 1] = temp
                new_production_set.add((production[0], ''.join(new_right)))
                i += 1
        return self.closure(new_production_set)

    def get_analyse_table(self):
        while True:
            receive_sign_dict = {}
            for (left, right) in self.status_list[self.index]:
                i = 0
                while i < len(right) and right[i] != self.point:
                    i += 1
                if i + 1 < len(right):
                    if right[i + 1] not in receive_sign_dict.keys():
                        receive_sign_dict[right[i + 1]] = {(left, right)}
                    else:
                        receive_sign_dict[right[i + 1]].add((left, right))
                else:
                    if left == self.new_start:
                        self.analyse_table[self.index] = {self.jinghao: [self.acc, ]}
                    else:
                        production_index = 0
                        for left_ in self.nonterminals:
                            for right_ in self.productions[left_]:
                                if (left, right.replace(self.point, '')) == (left_, right_):
                                    self.analyse_table[self.index] = {
                                        over: [production_index, 'r', (left_, right_)]
                                        for over in (self.follow[left_])
                                    }
                                production_index += 1

            for sign, production_set in receive_sign_dict.items():
                new_status = self.go(production_set, sign)
                new_dfa = []
                if new_status not in self.status_list:
                    self.status_list.append(new_status)
                    self.last_index += 1
                    new_dfa.append(self.last_index)
                else:
                    new_dfa.append(self.status_list.index(new_status))
                for production in production_set:
                    new_dfa.append(production)

                if self.index not in self.analyse_table.keys():
                    self.analyse_table[self.index] = {sign: new_dfa}
                else:
                    self.analyse_table[self.index].update({sign: new_dfa})
            self.index += 1
            if self.index > self.last_index:
                break
        if self.log_level >= 1:
            print('stauts list:')
            pprint(self.status_list)
            print('analyse table:')
            pprint(self.analyse_table)

    def is_lr0(self):
        ret = 1
        for status in self.status_list:
            guiyue_items = list()
            yijin_items = list()
            for left, right in status:
                i = 0
                while i < len(right) and right[i] != self.point:
                    i += 1
                if i + 1 == len(right):
                    if right[i - 1] != self.new_start and left != self.new_start:
                        guiyue_items.append(self.follow[left])
                elif right[i + 1] in self.overs:
                    yijin_items.append(right[i + 1])
            if len(guiyue_items) >= 2 or len(guiyue_items) > 0 and len(yijin_items) > 0:
                ret = 0
                jihe = set()
                for nonterminal in guiyue_items:
                    if nonterminal in jihe:
                        return -1
                    else:
                        jihe |= nonterminal
                for sign in yijin_items:
                    if sign in jihe:
                        return -1
                    else:
                        jihe.add(sign)
        return ret

    def analyse_lr(self, string):
        string += self.jinghao
        status_stack = [0, ]
        sign_stack = [self.jinghao,]
        string_index = 0
        while self.analyse_table[status_stack[-1]][string[string_index]][0] != self.acc:
            if 'r' != self.analyse_table[status_stack[-1]][string[string_index]][1]:
                if self.log_level >= 1:
                    print(status_stack, sign_stack)
                status_stack.append(self.analyse_table[status_stack[-1]][string[string_index]][0])
                sign_stack.append(string[string_index])
                string_index += 1
            else:
                # act
                left = self.analyse_table[status_stack[-1]][string[string_index]][2][0]
                right = self.analyse_table[status_stack[-1]][string[string_index]][2][1]
                if self.log_level >= 1:
                    print(status_stack, sign_stack, left, right)
                for i in range(len(right)):
                    sign_stack.pop()
                    status_stack.pop()
                if self.log_level >= 1:
                    print(status_stack, sign_stack, left, right)
                status_stack.append(self.analyse_table[status_stack[-1]][left][0])
                sign_stack.append(left)
                if self.log_level >= 1:
                    print(status_stack, sign_stack, left, right)
            if string[string_index] not in self.analyse_table[status_stack[-1]].keys():
                return 0
        return 1

    def analyse(self, string):
        print('analysing: ' + string)
        if self.analyse_lr(string) == 1:
            print('ok  ', string)
        else:
            print('fail', string)


# lr0
# start = 'E'
# productions = {
#     'E': ['aEb', 'aEc', 'ab']
# }
# string_list = ['ab', 'aab', 'aabb', 'aabc']

# 书上slr1
# start = 'L'
# productions = {
#     'L':['E,L', 'E'],
#     'E':['a','b']
# }
# string_list = ['a,b,a', 'aa', 'b,a,a,b']

# 书上slr1
# start = 'B'
# productions = {
#     'B':['bD;Te',],
#     'D': ['D;d','d'],
#     'T': ['s;T', 's']
# }
# string_list = ['bd;se', 'bd;s;se']

# 非srl1或lr0
# start = 'E'
# productions = {
#     'E': ['Eab', 'bR'],
#     'R': ['E', 'a'],
# }
# string_list = ['ba', 'aab']

# lr0
# start = 'E'
# productions = {
#     'E': ['aA', 'bB'],
#     'A': ['cA', 'd'],
#     'B': ['cB', 'd']
# }
# string_list = ['ad', 'bcd', 'ab']

# 实验slr1
start = 'A'
productions = {
    'A': ['V=E', ],
    'E': ['E+T', 'E-T', 'T'],
    'T': ['T*F', 'T/F', 'F'],
    'F': ['(E)', 'i'],
    'V': ['i', ],
}
string_list = ['i=i+i', 'i=(i-i)*i/(i+i)', 'i==i*i']
analyzer = SLRAnalyzer(start, productions, log_level=0)
for string in string_list:
    analyzer.analyse(string)