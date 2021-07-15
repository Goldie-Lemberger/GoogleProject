import initialization_pkg


class AutoComplete:
    def __init__(self):
        i = initialization_pkg.Initialization()

        self.data = i.get_tree()

    def get_best_k_completions(self, search_str):

        sol = self.data.query(search_str,score =0)

        if len(sol) < 5:
            sol += self.one_score_reduction(search_str)[:5 - len(sol)]

        if len(sol) < 5:
            sol += self.two_score_reduction(search_str, 5 - len(sol))[:5 - len(sol)]

        if len(sol) < 5:
            sol += self.three_score_reduction(search_str)[:5 - len(sol)]

        if len(sol) < 5:
            sol += self.four_score_reduction(search_str, 5 - len(sol))[:5 - len(sol)]

        if len(sol) < 5:
            sol += self.five_score_reduction(search_str)[:5 - len(sol)]

        if len(sol) < 5:
            sol += self.six_score_reduction(search_str, 5 - len(sol))[:5 - len(sol)]

        if len(sol) < 5:
            sol += self.eight_score_reduction(search_str, 5 - len(sol))[:5 - len(sol)]

        if len(sol) < 5:
            sol += self.ten_score_reduction(search_str, 5 - len(sol))[:5 - len(sol)]

        return sol[:5]

    def one_score_reduction(self, search_str):
        index = 4
        return self.replace_character(search_str, index,score =1)

    def two_score_reduction(self, search_str, length):
        index = 4
        sol = self.delete_character(search_str, index,score =2)
        if len(sol) < length - 1:
            sol += self.add_character(search_str, index,score =2 )
        if len(sol) < length - 1:
            sol += self.replace_character(search_str, index - 1, score =2)
        return sol

    def three_score_reduction(self, search_str):
        index = 2
        return self.replace_character(search_str, index,score =3)

    def four_score_reduction(self, search_str, length):
        index = 3
        sol = self.delete_character(search_str, index, index + 1,score =4)
        if len(sol) < length - 1:
            sol += self.add_character(search_str, index, index + 1, score =4)
        if len(sol) < length - 1:
            sol += self.replace_character(search_str, 1, score =4)
        return sol

    def five_score_reduction(self, search_str):
        return self.replace_character(search_str, 0,score =5)

    def six_score_reduction(self, search_str, length):
        index = 2
        sol = self.delete_character(search_str, index, index + 1,score = 6)
        if len(sol) < length - 1:
            sol += self.add_character(search_str, index, index + 1,score =6)
        return sol

    def eight_score_reduction(self, search_str, length):
        index = 1
        sol = self.delete_character(search_str, index, index + 1,score =8)
        if len(sol) < length - 1:
            sol += self.add_character(search_str, index, index + 1,score =8)
        return sol

    def ten_score_reduction(self, search_str, length):
        index = 0
        sol = self.delete_character(search_str, index, index + 1,score =10)
        if len(sol) < length - 1:
            sol += self.add_character(search_str, index, index + 1,score =10)
        return sol

    def add_character(self, search_str, start, end=None,score = 0):
        sol = []
        end = len(search_str) if end == None else end
        for i in range(start, end):
            search = search_str[:i] + '*' + search_str[i:]
            sol += self.data.query(search,score)
        return sol

    def delete_character(self, search_str, start, end=None,score = 0):
        sol = []
        end = len(search_str) if end == None else end
        for i in range(start, end):
            search = search_str[:i] + search_str[i + 1:]
            sol += self.data.query(search,score)
        return sol

    def replace_character(self, search_str, index, end=None,score = 0):
        sol = []
        end = len(search_str) if end == None else end
        for i in range(index, end):
            search = search_str[:i] + '*' + search_str[i + 1:]
            sol += self.data.query(search,score)
        return sol
