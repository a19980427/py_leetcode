from typing import List


class Solution:
    def validTicTacToe(self, board) -> bool:
        map_cnt = {'X': 0, 'O': 0, ' ': 0}
        win = {'X': False, 'O': False}

        for line in board:
            for ch in line:
                map_cnt[ch] += 1

        # 先手检查
        print(map_cnt)
        if map_cnt['X'] < map_cnt['O'] or map_cnt['X'] - map_cnt['O'] > 1:
            return False

        # 胜利检查,最多一人获胜
        self.horizontal_check(board, win)
        self.vertical_check(board, win)
        self.slant_check(board, win)

        print(win)

        # X已经赢了,O就不能再下
        if win['X']:
            return map_cnt['X'] > map_cnt['O'] and not win['O']

        # O赢了,下子数必须和X相同
        if win['O']:
            return map_cnt['X'] == map_cnt['O']

        return True

    def horizontal_check(self, board, win):
        temp = [0] * 3
        for i in range(3):
            for j in range(3):
                temp[j] = board[i][j]
            unique = set(temp)
            if len(unique) == 1 and temp[0] != ' ':
                win[temp[0]] = True

    def vertical_check(self, board, win):
        temp = [0] * 3
        for i in range(3):
            for j in range(3):
                temp[j] = board[j][i]
            unique = set(temp)
            if len(unique) == 1 and temp[0] != ' ':
                win[temp[0]] = True

    def slant_check(self, board, win):
        center = board[1][1]
        if center != ' ':
            if (center == board[0][0] == board[2][2]) or (center == board[0][2] == board[2][0]):
                win[center] = True
