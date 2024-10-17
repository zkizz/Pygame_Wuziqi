import time
import copy
import numpy as np
from ai import AI1Step  # 确保正确导入 AI1Step

class Gomoku:
    def __init__(self):
        self.g_map = [[0 for y in range(15)] for x in range(15)]  # 初始化棋盘
        self.cur_step = 0  # 当前步数
        self.max_search_steps = 3

    def move_lstep(self, input_by_window=False, pos_x=None, pos_y=None):
        if input_by_window:
            if 0 <= pos_x <= 14 and 0 <= pos_y <= 14:
                if self.g_map[pos_x][pos_y] == 0:
                    self.g_map[pos_x][pos_y] = 1
                    self.cur_step += 1
                    return
        else:
            while True:
                try:
                    pos_x = int(input('x:'))  # 用户输入
                    pos_y = int(input('y:'))
                    if 0 <= pos_x <= 14 and 0 <= pos_y <= 14:
                        if self.g_map[pos_x][pos_y] == 0:
                            self.g_map[pos_x][pos_y] = 1
                            self.cur_step += 1
                            return
                except ValueError:
                    continue

    def game_result(self, show=False):
        # 判断游戏结果
        for x in range(11):
            for y in range(11):
                if self.g_map[x + 4][y] == 1 and self.g_map[x + 3][y + 1] == 1 and self.g_map[x + 2][y + 2] == 1 and \
                        self.g_map[x + 1][y + 3] == 1 and self.g_map[x][y + 4] == 1:
                    if show:
                        return 1, [(x + t, y + 4 - t) for t in range(5)]
                    return 1
                if self.g_map[x + 4][y] == 2 and self.g_map[x + 3][y + 1] == 2 and self.g_map[x + 2][y + 2] == 2 and \
                        self.g_map[x + 1][y + 3] == 2 and self.g_map[x][y + 4] == 2:
                    if show:
                        return 2, [(x + t, y + 4 - t) for t in range(5)]
                    return 2

        for x in range(11):
            for y in range(15):
                if self.g_map[x][y] == 1 and self.g_map[x + 1][y] == 1 and self.g_map[x + 2][y] == 1 and \
                        self.g_map[x + 3][y] == 1 and self.g_map[x + 4][y] == 1:
                    if show:
                        return 1, [(x0, y) for x0 in range(x, x + 5)]
                    return 1
                if self.g_map[x][y] == 2 and self.g_map[x + 1][y] == 2 and self.g_map[x + 2][y] == 2 and \
                        self.g_map[x + 3][y] == 2 and self.g_map[x + 4][y] == 2:
                    if show:
                        return 2, [(x0, y) for x0 in range(x, x + 5)]
                    return 2

        for x in range(15):
            for y in range(11):
                if self.g_map[x][y] == 1 and self.g_map[x][y + 1] == 1 and self.g_map[x][y + 2] == 1 and self.g_map[x][y + 3] == 1 and self.g_map[x][y + 4] == 1:
                    if show:
                        return 1, [(x, y0) for y0 in range(y, y + 5)]
                    return 1
                if self.g_map[x][y] == 2 and self.g_map[x][y + 1] == 2 and self.g_map[x][y + 2] == 2 and self.g_map[x][y + 3] == 2 and self.g_map[x][y + 4] == 2:
                    if show:
                        return 2, [(x, y0) for y0 in range(y, y + 5)]
                    return 2

        for x in range(11):
            for y in range(11):
                if self.g_map[x][y] == 1 and self.g_map[x + 1][y + 1] == 1 and self.g_map[x + 2][y + 2] == 1 and \
                        self.g_map[x + 3][y + 3] == 1 and self.g_map[x + 4][y + 4] == 1:
                    if show:
                        return 1, [(x + t, y + t) for t in range(5)]
                    return 1
                if self.g_map[x][y] == 2 and self.g_map[x + 1][y + 1] == 2 and self.g_map[x + 2][y + 2] == 2 and \
                        self.g_map[x + 3][y + 3] == 2 and self.g_map[x + 4][y + 4] == 2:
                    if show:
                        return 2, [(x + t, y + t) for t in range(5)]
                    return 2

        for x in range(15):
            for y in range(15):
                if self.g_map[x][y] == 0:
                    if show:
                        return 0, [(-1, -1)]
                    return 0
        if show:
            return 3, [(-1, -1)]
        return 3

    def ai_move_lstep(self):
        for x in range(15):
            for y in range(15):
                if self.g_map[x][y] == 0:
                    self.g_map[x][y] = 2
                    self.cur_step += 1
                    return

    def ai_play_1step_py_python(self):
        ai = AI1Step(self, self.cur_step, True)
        st = time.time()
        ai.search(0, [set(), set()], self.max_search_steps)
        ed = time.time()
        print('生成了%d个节点，用时%.4f，评价用时%.4f' % (len(ai.method_tree), ed - st, ai.t))
        if ai.next_node_dx_list[0] == -1:
            raise ValueError('ai.next_node_dx_list[0] == -1')
        ai_ope = ai.method_tree[ai.next_node_dx_list[0]].ope
        if self.g_map[ai_ope[0]][ai_ope[1]] != 0:
            raise ValueError('self.game_map[ai_ope[0]][ai_ope[1]] = %d' % self.g_map[ai_ope[0]][ai_ope[1]])
        self.g_map[ai_ope[0]][ai_ope[1]] = 2
        self.cur_step += 1

    def ai_play_1step(self):
        self.max_search_steps = 2
        self.ai_play_1step_py_python()

    def show(self, res):
        for y in range(15):
            for x in range(15):
                if self.g_map[x][y] == 0:
                    print('  ', end='')
                elif self.g_map[x][y] == 1:
                    print('〇', end='')
                elif self.g_map[x][y] == 2:
                    print('×', end='')
                if x != 14:
                    print('-', end='')
            print('\n', end='')
            for x in range(15):
                print('|  ', end='')
            print('\n', end='')

        if res == 1:
            print('玩家获胜!')
        elif res == 2:
            print('电脑获胜!')
        elif res == 3:
            print('平局!')

    def play(self):
        while True:
            self.move_lstep()  # 玩家下一步
            res = self.game_result()  # 判断结果
            if res != 0:  # 如果已经结束，则显示结果，退出循环
                self.show(res)
                return
            self.ai_move_lstep()  # 电脑下一步
            res = self.game_result()
            if res != 0:
                self.show(res)
                return
            self.show(0)
